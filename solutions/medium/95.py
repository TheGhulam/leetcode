#Problem 95: Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0: return []

        def generate_trees(start, end):
            trees = []

            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end+1):
                left_subtrees = generate_trees(start, i-1)
                right_subtrees = generate_trees(i+1, end)

                # Connect left and right subtrees with root i
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)

            return trees
        
        return generate_trees(1, n)