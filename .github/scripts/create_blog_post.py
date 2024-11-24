#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
import subprocess
import requests
import json
from complexity_analyzer import analyze_leetcode_solution
import time
from datetime import datetime

class BlogPostCreationError(Exception):
    """Custom exception for blog post creation errors"""
    pass

def get_latest_solution_file():
    """Get the most recently modified solution file."""
    try:
        result = subprocess.run(
            ['git', 'diff-tree', '--no-commit-id', '--name-status', '-r', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        
        files = result.stdout.splitlines()
        solution_files = [
            f.split('\t')[1] for f in files 
            if (f.startswith('A') or f.startswith('M')) and f.endswith('.py')
        ]
        
        if not solution_files:
            raise BlogPostCreationError("No Python solution files found in the latest commit")
            
        return solution_files[-1]
    except subprocess.CalledProcessError as e:
        raise BlogPostCreationError(f"Error executing git command: {e}")
    except Exception as e:
        raise BlogPostCreationError(f"Unexpected error in get_latest_solution_file: {e}")

def extract_problem_slug(file_path):
    """Extract problem slug from the top comment."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        match = re.search(r'#Problem \d+: (.+)', content)
        if match:
            slug = match.group(1).replace(' ', '-').lower()
            print(f"Extracted problem slug: {slug}")
            return slug
        else:
            raise BlogPostCreationError("No problem slug found in file")
    except Exception as e:
        raise BlogPostCreationError(f"Error extracting problem slug: {e}")

def get_problem_details(problem_slug, max_retries=3):
    """Fetch problem details from LeetCode API with retry logic."""
    api_url = "https://alfa-leetcode-api.onrender.com/select"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{api_url}?titleSlug={problem_slug}")
            
            if response.status_code == 429:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Rate limit hit. Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise BlogPostCreationError("API rate limit exceeded after all retries")
            
            response.raise_for_status()
            problem_data = response.json()

            if not problem_data:
                raise BlogPostCreationError("Empty response from API")

            tags = []
            topic_tags = problem_data.get('topicTags', [])
            if isinstance(topic_tags, list):
                tags = [tag.get('name', '').lower() for tag in topic_tags if isinstance(tag, dict)]
            
            required_fields = ['questionFrontendId', 'questionTitle', 'titleSlug', 'difficulty', 'question']
            missing_fields = [field for field in required_fields if not problem_data.get(field)]
            if missing_fields:
                raise BlogPostCreationError(f"Missing required fields in API response: {missing_fields}")

            return {
                'number': problem_data['questionFrontendId'],
                'title': problem_data['questionTitle'],
                'titleSlug': problem_data['titleSlug'],
                'difficulty': problem_data['difficulty'],
                'question': problem_data['question'],
                'exampleTC': problem_data.get('exampleTestcases'),
                'tags': tags,
                'likes': problem_data.get('likes', 0),
                'dislikes': problem_data.get('dislikes', 0),
            }

        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise BlogPostCreationError(f"Error fetching problem details from API: {e}")
        except Exception as e:
            raise BlogPostCreationError(f"Unexpected error getting problem details: {e}")

def create_blog_post(problem_info, solution_file):
    """Generate a markdown blog post from the problem info."""
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        slug = f"lc-{problem_info['number']}-{problem_info['titleSlug']}"
        leetcode_url = f"https://leetcode.com/problems/{problem_info['titleSlug']}"
        
        if not os.path.exists(solution_file):
            raise BlogPostCreationError(f"Solution file not found: {solution_file}")

        with open(solution_file, 'r', encoding='utf-8') as f:
            solution_content = f.read()

        complexity_info = analyze_leetcode_solution(solution_file)
        
        # Calculate rating safely
        total_votes = problem_info['likes'] + problem_info['dislikes']
        rating = (problem_info['likes'] / total_votes * 100) if total_votes > 0 else 0
        
        template = f"""---
title: "LeetCode {problem_info['number']}: {problem_info['title']}"
date: {today}
summary: "Leetcode {problem_info['number']}: {problem_info['title']} solution in Python"
tags: ["leetcode", "algorithms", "{problem_info['difficulty'].lower()}", "python"]
draft: false
---

## Problem Description

[LeetCode Problem {problem_info['number']}]({leetcode_url})

{problem_info['question']}

**Difficulty:** {problem_info['difficulty']}

**Tags:** {', '.join(problem_info['tags'])}

**Rating:** {rating:.2f}%

## Complexity Analysis

{complexity_info['explanation']}

## Solution

Here's my Python solution to this problem:

```python
{solution_content}
```
"""
        
        post_dir = Path('../blog-repo/src/content/blog/lc')
        post_dir.mkdir(parents=True, exist_ok=True)
        post_file = post_dir / f"{today}-{slug}.mdx"
        
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(template)
        
        print(f"Successfully created blog post: {post_file}")
        return post_file
    except Exception as e:
        raise BlogPostCreationError(f"Error creating blog post: {e}")

def main():
    try:
        solution_file = get_latest_solution_file()
        print(f"Processing solution file: {solution_file}")
        
        problem_slug = extract_problem_slug(solution_file)
        print(f"Found problem slug: {problem_slug}")
            
        problem_info = get_problem_details(problem_slug)
        print(f"Retrieved problem details for: {problem_info['title']}")
        
        post_file = create_blog_post(problem_info, solution_file)
        print(f"Blog post creation successful: {post_file}")
        
    except BlogPostCreationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()