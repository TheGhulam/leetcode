#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path
import subprocess
import requests
import json
from complexity_analyzer import analyze_leetcode_solution

def get_latest_solution_file():
    """Get the most recently modified solution file."""
    try:
        # Get all modified files in the latest commit
        result = subprocess.run(
            ['git', 'diff-tree', '--no-commit-id', '--name-status', '-r', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        
        # Filter for added or modified Python files
        files = result.stdout.splitlines()
        solution_files = [
            f.split('\t')[1] for f in files 
            if (f.startswith('A') or f.startswith('M')) and f.endswith('.py')
        ]
        
        if not solution_files:
            print("No Python solution files found in the latest commit")
            return None
            
        return solution_files[-1]
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in get_latest_solution_file: {e}")
        return None

def extract_problem_slug(file_path):
    """Extract just the problem slug from the top comment following this format:
    #Problem 1122: Relative Sort Array
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract the problem slug from the top comment
        match = re.search(r'#Problem \d+: (.+)', content)
        if match:
            slug = match.group(1).replace(' ', '-').lower()
            print(f"Extracted problem slug: {slug}")
            return slug
        else:
            print("No problem slug found in file")
            return None
    except Exception as e:
        print(f"Error extracting problem slug: {e}")
        return None

def get_problem_details(problem_slug):
    """Fetch problem details from LeetCode API."""
    try:
        # Construct the API URL
        api_url = "https://alfa-leetcode-api.onrender.com/select"
        
        # Make the API request
        response = requests.get(f"{api_url}?titleSlug={problem_slug}")
        response.raise_for_status()
        
        # Parse the response
        problem_data = response.json()

        tags = []
        topic_tags = problem_data.get('topicTags', [])
        if isinstance(topic_tags, list):
            tags = [tag.get('name', '').lower() for tag in topic_tags if isinstance(tag, dict)]
        
        return {
            'number': problem_data.get('questionFrontendId'),
            'title': problem_data.get('questionTitle'),
            'titleSlug': problem_data.get('titleSlug'),
            'difficulty': problem_data.get('difficulty'),
            'question': problem_data.get('question'),
            'exampleTC': problem_data.get('exampleTestcases'),
            'tags': tags,
            'likes': problem_data.get('likes'),
            'dislikes': problem_data.get('dislikes'),
        }

        # Logging
        print(f"Problem Details: {problem_data}")

    except requests.RequestException as e:
        print(f"Error fetching problem details from API: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting problem details: {e}")
        return None

def create_blog_post(problem_info, solution_file):
    """Generate a markdown blog post from the problem info."""
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Create a URL-friendly slug
        slug = f"leetcode-{problem_info['number']}-{problem_info['titleSlug']}"
        
        # Generate leetcode problem URL
        leetcode_url = f"https://leetcode.com/problems/{problem_info['titleSlug']}"
        
        # Read the solution content
        with open(solution_file, 'r', encoding='utf-8') as f:
            solution_content = f.read()

        # Analyze the solution for complexity
        complexity_info = analyze_leetcode_solution(solution_file)
        
        template = f"""---
title: "LeetCode {problem_info['number']}: {problem_info['title']}"
date: {today}
summary: "Leetcode {problem_info['number']}: {problem_info['title']} solution in Python"
tags: ["leetcode", "algorithms", "{problem_info['difficulty']}", "python"]
draft: false
---

## Problem Description

[LeetCode Problem {problem_info['number']}]({leetcode_url})

{problem_info['question']}

**Difficulty:** {problem_info['difficulty']}

**Tags:** {', '.join(problem_info['tags'])}

**Rating:** {problem_info['likes'] / (problem_info['likes'] + problem_info['dislikes']) * 100:.2f}%

## Complexity Analysis

{complexity_info['explanation']}

## Solution

Here's my Python solution to this problem:

```python
{solution_content}
```
"""
        
        # Create blog post file
        post_dir = Path('../blog-repo/src/content/blog')
        post_dir.mkdir(parents=True, exist_ok=True)
        post_file = post_dir / f"{today}-{slug}.md"
        
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(template)
        
        print(f"Successfully created blog post: {post_file}")
        return post_file
    except Exception as e:
        print(f"Error creating blog post: {e}")
        return None

def main():
    try:
        # Get the latest solution file
        solution_file = get_latest_solution_file()
        if not solution_file:
            return
        
        print(f"Processing solution file: {solution_file}")
        
        # Extract problem number from file
        problem_slug= extract_problem_slug(solution_file)
        if not problem_slug:
            print("Could not determine problem slug")
            return
            
        # Fetch problem details from API
        problem_info = get_problem_details(problem_slug)
        if not problem_info:
            print("Could not fetch problem details from API")
            return
        
        # Create and save blog post
        post_file = create_blog_post(problem_info, solution_file)
        if post_file:
            print(f"Blog post creation successful!")
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()