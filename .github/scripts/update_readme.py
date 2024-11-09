import os
import re
import requests
from bs4 import BeautifulSoup

def get_problem_info(problem_number):
    """Fetch problem information from LeetCode"""
    url = f"https://leetcode.com/problems/{problem_number}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title from meta tags or other elements
        title = soup.find('meta', property='og:title')
        if title:
            title = title.get('content')
        
        # Extract difficulty and topics from the page
        # Note: This is a simplified version. You might need to adjust based on LeetCode's actual HTML structure
        difficulty = "Medium"  # Default value
        topics = ["Array"]    # Default value
        
        return {
            "title": title,
            "difficulty": difficulty,
            "topics": topics
        }
    except Exception as e:
        print(f"Error fetching problem info: {e}")
        return None

def extract_complexity(file_content):
    """Extract time and space complexity from file comments"""
    time_match = re.search(r"Time:\s*O\((.*?)\)", file_content)
    space_match = re.search(r"Space:\s*O\((.*?)\)", file_content)
    
    time = time_match.group(1) if time_match else "?"
    space = space_match.group(1) if space_match else "?"
    
    return f"Time: O({time}), Space: O({space})"

def get_difficulty_from_path(file_path):
    """Get difficulty from file path"""
    if "easy" in file_path.lower():
        return "Easy"
    elif "medium" in file_path.lower():
        return "Medium"
    elif "hard" in file_path.lower():
        return "Hard"
    return "Medium"  # default

def update_readme():
    # Read the list of files from the temporary file
    files_path = os.environ.get('LEETCODE_FILES')
    if not files_path or not os.path.exists(files_path):
        print("No files to process")
        return
        
    with open(files_path, 'r') as f:
        new_files = [line.strip() for line in f if line.strip()]
    
    # Read current README content
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the solutions table
    table_match = re.search(r'\|\s*#\s*\|\s*Title\s*\|.*\|\n\|[-|]*\n((?:\|.*\n)*)', content)
    if not table_match:
        print("Could not find solutions table in README")
        return
        
    existing_entries = table_match.group(1).strip().split('\n')
    new_entries = []
    
    for file_path in new_files:
        # Extract problem number from filename
        problem_number = re.search(r'(\d+)\.py$', file_path)
        if not problem_number:
            continue
            
        problem_number = problem_number.group(1)
        
        # Read the solution file to extract complexity
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            complexity = extract_complexity(file_content)
        
        # Get problem information
        problem_info = get_problem_info(problem_number)
        if not problem_info:
            continue
            
        difficulty = get_difficulty_from_path(file_path)
        topics = ", ".join(problem_info["topics"])
        
        # Create table entry
        entry = f"| {problem_number} | [{problem_info['title']}](https://leetcode.com/problems/{problem_number}/) | [Python](./{file_path}) | {difficulty} | {topics} | {complexity} |"
        new_entries.append(entry)
    
    # Combine existing and new entries, sort by problem number
    all_entries = existing_entries + new_entries
    all_entries.sort(key=lambda x: int(re.search(r'\|\s*(\d+)\s*\|', x).group(1)))
    
    # Replace old table with new one
    table_header = "| # | Title | Solution | Difficulty | Topics | Notes |\n|---|-------|----------|------------|---------|-------|\n"
    new_table = table_header + '\n'.join(all_entries) + '\n'
    
    # Update README content
    new_content = re.sub(r'\|\s*#\s*\|\s*Title\s*\|.*\|\n\|[-|]*\n((?:\|.*\n)*)', new_table, content)
    
    # Write updated content back to README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()