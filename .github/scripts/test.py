import unittest
from complexity_analyzer import analyze_complexity, extract_solution_class

class TestComplexityAnalyzer(unittest.TestCase):
    def test_constant_time(self):
        code = """
class Solution:
    def constantTime(self, nums):
        if not nums:
            return 0
        return nums[0]
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(1)")
        self.assertEqual(space_complexity, "O(1)")

    def test_linear_time(self):
        code = """
class Solution:
    def linearTime(self, nums):
        total = 0
        for num in nums:
            total += num
        return total
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(n)")
        self.assertEqual(space_complexity, "O(1)")

    def test_quadratic_time(self):
        code = """
class Solution:
    def quadraticTime(self, nums):
        result = []
        for i in nums:
            for j in nums:
                result.append(i * j)
        return result
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(n²)")
        self.assertEqual(space_complexity, "O(n)")

    def test_cubic_time(self):
        code = """
class Solution:
    def cubicTime(self, nums):
        result = []
        for i in nums:
            for j in nums:
                for k in nums:
                    result.append(i * j * k)
        return result
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(n^3)")
        self.assertEqual(space_complexity, "O(n)")

    def test_recursive(self):
        code = """
class Solution:
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(2^n)")
        self.assertEqual(space_complexity, "O(1)")

    def test_space_complexity(self):
        code = """
class Solution:
    def complexSpace(self, nums):
        # O(n) space
        dict1 = {x: x*x for x in nums}
        # O(n) space
        list1 = [x*2 for x in nums]
        # O(n) space
        set1 = {x%2 for x in nums}
        return dict1, list1, set1
        """
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(n)")
        self.assertEqual(space_complexity, "O(n)")

    def test_extract_solution_class(self):
        code = """
# Some comments before
class Solution:
    def method(self):
        pass
# Some comments after
class AnotherClass:
    pass
        """
        solution_code = extract_solution_class(code)
        self.assertIsNotNone(solution_code)
        self.assertIn("class Solution", solution_code)
        self.assertNotIn("class AnotherClass", solution_code)
    
    def test_leetcode_medium_33(self):
        with open("../../solutions/medium/33.py", "r") as f:
            code = f.read()
        
        time_complexity, space_complexity = analyze_complexity(code)
        self.assertEqual(time_complexity, "O(log n)")
        self.assertEqual(space_complexity, "O(1)")

def run_tests():
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComplexityAnalyzer)
    
    # Run the tests and capture results
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\nTest Summary:")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)