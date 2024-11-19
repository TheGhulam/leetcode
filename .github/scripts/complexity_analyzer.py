import ast
import re
from typing import Dict, Optional, Tuple

class ComplexityAnalyzer(ast.NodeVisitor):
    """Analyzes Python code to estimate time and space complexity."""
    
    def __init__(self):
        self.loops_depth = 0
        self.max_loops_depth = 0
        self.has_recursive_call = False
        self.function_name = None
        self.space_complexity = []
        self.current_space_depth = 0
        self.in_comprehension = False
        self.has_binary_search = False
        
    def visit_FunctionDef(self, node):
        """Visit function definition to capture the name and analyze complexity."""
        if self.function_name is None:  # Only analyze the main solution function
            self.function_name = node.name
        self.generic_visit(node)
        
    def visit_For(self, node):
        """Visit for loops to track nesting depth."""
        if not self.in_comprehension:  # Only count explicit for loops
            self.loops_depth += 1
            self.max_loops_depth = max(self.max_loops_depth, self.loops_depth)
        self.generic_visit(node)
        if not self.in_comprehension:
            self.loops_depth -= 1
        
    def visit_While(self, node):
        """Visit while loops to track nesting depth and detect binary search patterns."""
        self.loops_depth += 1
        self.max_loops_depth = max(self.max_loops_depth, self.loops_depth)
        
        # Check for binary search pattern
        if isinstance(node.test, ast.Compare):
            # Look for binary search indicators in the while loop body
            for stmt in ast.walk(node):
                if isinstance(stmt, ast.AugAssign):
                    # Check for updating pointers (l = m + 1 or r = m - 1 pattern)
                    if isinstance(stmt.op, (ast.Add, ast.Sub)):
                        if isinstance(stmt.value, ast.BinOp):
                            if isinstance(stmt.value.op, (ast.Add, ast.Sub)):
                                if hasattr(stmt.value.left, 'id') and stmt.value.left.id == 'm':
                                    if isinstance(stmt.value.right, ast.Num) and stmt.value.right.n == 1:
                                        self.has_binary_search = True
                elif isinstance(stmt, ast.Assign):
                    # Check for mid calculation (m = (l + r) // 2 pattern)
                    if len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
                        if stmt.targets[0].id == 'm':
                            if isinstance(stmt.value, ast.BinOp):
                                if isinstance(stmt.value.op, ast.FloorDiv):
                                    self.has_binary_search = True
                                    
        self.generic_visit(node)
        self.loops_depth -= 1
        
    def visit_Call(self, node):
        """Visit function calls to detect recursion."""
        if isinstance(node.func, ast.Name):
            if hasattr(node.func, 'id') and node.func.id == self.function_name:
                self.has_recursive_call = True
        elif isinstance(node.func, ast.Attribute):
            if hasattr(node.func.value, 'id') and node.func.value.id == 'self':
                if node.func.attr == self.function_name:
                    self.has_recursive_call = True
        self.generic_visit(node)
        
    def visit_ListComp(self, node):
        """Visit list comprehension."""
        self.in_comprehension = True
        self.space_complexity.append(('list', self.current_space_depth))
        self.max_loops_depth = max(self.max_loops_depth, 1)  # At least O(n)
        self.generic_visit(node)
        self.in_comprehension = False
        
    def visit_DictComp(self, node):
        """Visit dictionary comprehension."""
        self.in_comprehension = True
        self.space_complexity.append(('dict', self.current_space_depth))
        self.max_loops_depth = max(self.max_loops_depth, 1)  # At least O(n)
        self.generic_visit(node)
        self.in_comprehension = False
        
    def visit_SetComp(self, node):
        """Visit set comprehension."""
        self.in_comprehension = True
        self.space_complexity.append(('set', self.current_space_depth))
        self.max_loops_depth = max(self.max_loops_depth, 1)  # At least O(n)
        self.generic_visit(node)
        self.in_comprehension = False
        
    def visit_List(self, node):
        """Visit list creation to track space complexity."""
        self.space_complexity.append(('list', self.current_space_depth))
        self.generic_visit(node)
        
    def visit_Dict(self, node):
        """Visit dictionary creation to track space complexity."""
        self.space_complexity.append(('dict', self.current_space_depth))
        self.generic_visit(node)
        
    def visit_Set(self, node):
        """Visit set creation to track space complexity."""
        self.space_complexity.append(('set', self.current_space_depth))
        self.generic_visit(node)

def analyze_complexity(code: str) -> Tuple[str, str]:
    """
    Analyzes the time and space complexity of the given code.
    
    Args:
        code (str): The Python source code to analyze
        
    Returns:
        Tuple[str, str]: Time complexity and space complexity as strings
    """
    try:
        tree = ast.parse(code)
        analyzer = ComplexityAnalyzer()
        analyzer.visit(tree)
        
        # Determine time complexity
        if analyzer.has_recursive_call:
            time_complexity = "O(2^n)"  # Assuming basic recursive pattern
        else:
            if analyzer.max_loops_depth == 0:
                time_complexity = "O(1)"
            elif analyzer.has_binary_search:
                time_complexity = "O(log n)"  # Binary search pattern detected
            elif analyzer.max_loops_depth == 1:
                time_complexity = "O(n)"
            elif analyzer.max_loops_depth == 2:
                time_complexity = "O(n²)"
            else:
                time_complexity = f"O(n^{analyzer.max_loops_depth})"
        
        # Determine space complexity
        if analyzer.has_binary_search:
            space_complexity = "O(1)"  # Binary search typically uses constant space
        elif not analyzer.space_complexity:
            space_complexity = "O(1)"
        else:
            # Count unique data structures at each depth
            max_space = 1
            for _, depth in analyzer.space_complexity:
                max_space = max(max_space, depth + 1)
            
            if max_space == 1:
                space_complexity = "O(n)"
            else:
                space_complexity = f"O(n^{max_space})"
        
        return time_complexity, space_complexity
        
    except Exception as e:
        print(f"Error analyzing complexity: {e}")
        return "O(?)", "O(?)"

def extract_solution_class(code: str) -> Optional[str]:
    """
    Extracts the Solution class from the code.
    
    Args:
        code (str): The complete source code
        
    Returns:
        Optional[str]: The Solution class code if found, None otherwise
    """
    try:
        # More robust regex pattern that handles various formatting
        pattern = r'class\s+Solution\s*(?:\([^)]*\))?\s*:\s*(?:[^\n]*\n(?:(?!class\s+)[^\n]*\n)*)?'
        match = re.search(pattern, code, re.MULTILINE | re.DOTALL)
        if match:
            # Get the matched text and any indented lines that follow
            result = match.group(0)
            remaining_lines = code[match.end():].split('\n')
            for line in remaining_lines:
                if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                    break
                result += line + '\n'
            return result
        return None
    except Exception as e:
        print(f"Error extracting solution class: {e}")
        return None

def analyze_leetcode_solution(file_path: str) -> Dict[str, str]:
    """
    Analyzes a LeetCode solution file and returns complexity information.
    
    Args:
        file_path (str): Path to the solution file
        
    Returns:
        Dict[str, str]: Dictionary containing complexity analysis
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Extract the Solution class
        solution_code = extract_solution_class(code)
        if not solution_code:
            return {
                'time_complexity': 'O(?)',
                'space_complexity': 'O(?)',
                'explanation': 'Could not extract solution code for analysis.'
            }
        
        # Analyze complexity
        time_complexity, space_complexity = analyze_complexity(solution_code)
        
        # Generate explanation
        explanation = f"""The solution has the following complexity characteristics:

- Time Complexity: {time_complexity}
- Space Complexity: {space_complexity}

Note: This is an automated analysis and may not capture all edge cases or specific algorithmic optimizations."""
        
        return {
            'time_complexity': time_complexity,
            'space_complexity': space_complexity,
            'explanation': explanation
        }
        
    except Exception as e:
        print(f"Error analyzing solution: {e}")
        return {
            'time_complexity': 'O(?)',
            'space_complexity': 'O(?)',
            'explanation': f'Error during analysis: {str(e)}'
        }