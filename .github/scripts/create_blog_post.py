#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path
import subprocess

def get_latest_solution_file():
    """Get the most recently modified solution file."""
    result = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'],
                          capture_output=True, text=True)
    files = result.stdout.splitlines()
    solution_files = [f for f in files if f.endswith(('.py', '.java', '.cpp'))]
    return solution_files[-1] if solution_files else None

def extract_problem_info(file_path):
    """Extract problem number, title, and difficulty from file comments."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract problem details from file comments
    problem_pattern = r'#\s*Problem\s*(\d+)\s*:\s*(.+)'
    difficulty_pattern = r'#\s*Difficulty\s*:\s*(.+)'
    
    problem_match = re.search(problem_pattern, content)
    difficulty_match = re.search(difficulty_pattern, content)
    
    number = problem_match.group(1) if problem_match else "Unknown"
    title = problem_match.group(2) if problem_match else Path(file_path).stem
    difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
    
    return {
        'number': number,
        'title': title,
        'difficulty': difficulty,
        'solution': content
    }

def create_blog_post(problem_info):
    """Generate a markdown blog post from the problem info."""
    today = datetime.now().strftime('%Y-%m-%d')
    slug = f"leetcode-{problem_info['number']}-{problem_info['title'].lower().replace(' ', '-')}"
    
    template = f"""---
title: "LeetCode {problem_info['number']}: {problem_info['title']}"
summary: "Solution for LeetCode problem {problem_info['number']}: {problem_info['title']}"
date: {today}
tags: ["leetcode", "algorithms", "{problem_info['difficulty'].lower()}"]
draft: false
---

## Problem Description

[LeetCode Problem {problem_info['number']}](https://leetcode.com/problems/{slug})

Difficulty: {problem_info['difficulty']}

## Solution Approach

Here's my solution to this problem:

```{Path(solution_file).suffix[1:]}
{problem_info['solution']}
```

## Explanation

[Add your explanation of the solution approach here]

## Time and Space Complexity

- Time Complexity: 
- Space Complexity: 

## Key Takeaways

[Add your learning points and insights here]
"""
    
    # Create blog post file
    post_dir = Path('V2.GAHMED/src/content/blog')
    post_dir.mkdir(parents=True, exist_ok=True)
    post_file = post_dir / f"{today}-{slug}.md"
    
    with open(post_file, 'w') as f:
        f.write(template)
    
    return post_file

if __name__ == "__main__":
    # Get the latest solution file
    solution_file = get_latest_solution_file()
    if not solution_file:
        print("No solution files found in the latest commit")
        exit(0)
    
    # Extract problem information
    problem_info = extract_problem_info(f"leetcode/{solution_file}")
    
    # Create and save blog post
    post_file = create_blog_post(problem_info)
    print(f"Created blog post: {post_file}")