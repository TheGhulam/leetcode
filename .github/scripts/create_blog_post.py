#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path
import subprocess

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

def extract_problem_info(file_path):
    """Extract problem number, title, and difficulty from file comments."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Enhanced patterns with more flexible whitespace handling
        problem_pattern = r'#\s*Problem\s*(?:Number)?\s*:?\s*(\d+)\s*[:-]\s*(.+?)(?=\n|$)'
        difficulty_pattern = r'#\s*Difficulty\s*:?\s*(\w+)(?=\n|$)'
        
        problem_match = re.search(problem_pattern, content, re.IGNORECASE)
        difficulty_match = re.search(difficulty_pattern, content, re.IGNORECASE)
        
        if not problem_match:
            print(f"Warning: Could not extract problem number and title from {file_path}")
        
        number = problem_match.group(1) if problem_match else "Unknown"
        title = problem_match.group(2).strip() if problem_match else Path(file_path).stem
        difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
        
        return {
            'number': number,
            'title': title,
            'difficulty': difficulty,
            'solution': content
        }
    except Exception as e:
        print(f"Error extracting problem info from {file_path}: {e}")
        return None

def create_blog_post(problem_info, solution_file):
    """Generate a markdown blog post from the problem info."""
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        # Create a URL-friendly slug
        # Clean the title for the URL slug
        clean_title = re.sub(r'[^\w\s-]', '', problem_info['title'].lower())
        slug = f"leetcode-{problem_info['number']}-{clean_title.replace(' ', '-')}"
        
        # Generate leetcode problem URL
        leetcode_slug = problem_info['title'].lower().replace(' ', '-')
        leetcode_url = f"https://leetcode.com/problems/{leetcode_slug}"
        
        template = f"""---
title: "LeetCode {problem_info['number']}: {problem_info['title']}"
date: {today}
summary: "Leetcode {problem_info['number']}: {problem_info['title']} solution in Python"
tags: ["leetcode", "algorithms", "{problem_info['difficulty'].lower()}", "python"]
draft: false
---

## Problem Description

[LeetCode Problem {problem_info['number']}]({leetcode_url})

**Difficulty:** {problem_info['difficulty']}

## Solution Approach

Here's my Python solution to this problem:

```python
{problem_info['solution']}
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
        
        # Extract problem information
        problem_info = extract_problem_info(solution_file)
        if not problem_info:
            return
        
        # Create and save blog post
        post_file = create_blog_post(problem_info, solution_file)
        if post_file:
            print(f"Blog post creation successful!")
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()