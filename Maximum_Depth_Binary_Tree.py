# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        #if root == None:
        #    return 0
        #return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        queue = [root]
        leaf = []
        path = []
        while len(queue) > 0:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
            if not temp.getLeftBranch() and not temp.getRightBranch():
                leaf.append(temp.getValue())
                path.append(tracePath(temp))
        return max(len(sub) for sub in path)
        
