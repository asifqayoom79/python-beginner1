#Implement Binary tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, node, value):
        if not node:
            return TreeNode(value)
        if value < node.val:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)
        return node
#Find height of a given tree
    def find_height(self, node):
        if not node:
            return -1
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return max(left_height, right_height) + 1
#Perform Preorder_traversal
    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
# Perform inorder_traversal
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)
#Perform Postorder_traversal
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=" ")

#Function to print all the leaves in a given binary tree
    def print_leaves(self, node):
        if not node:
            return
        if not node.left and not node.right:
            print(node.val, end=" ")
        self.print_leaves(node.left)
        self.print_leaves(node.right)
# Implement BFS (Breath First Search)
    def breadth_first_search(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
#Depth First Search(DFS)
    def depth_first_search(self):
        self.preorder_traversal(self.root)
#Find sum of all left leaves in a given Binary Tree
    def sum_left_leaves(self, node, is_left=False):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return (
            self.sum_left_leaves(node.left, True)
            + self.sum_left_leaves(node.right, False)
        )
#Find sum of all nodes of the given perfect binary tree
    def sum_all_nodes(self, node):
        if not node:
            return 0
        return node.val + self.sum_all_nodes(node.left) + self.sum_all_nodes(node.right)
#Count subtress that sum up to a given value x in a binary tree
    def count_subtrees_with_sum(self, node, target_sum):
        if not node:
            return 0
        left_sum = self.sum_all_nodes(node.left)
        right_sum = self.sum_all_nodes(node.right)
        total_sum = node.val + left_sum + right_sum
        count = self.count_subtrees_with_sum(node.left, target_sum) + self.count_subtrees_with_sum(node.right, target_sum)
        if total_sum == target_sum:
            count += 1
        return count
#Find maximum level sum in Binary Tree
    def max_level_sum(self):
        if not self.root:
            return 0
        queue = [self.root]
        max_sum = float('-inf')
        while queue:
            level_sum = sum(node.val for node in queue)
            max_sum = max(max_sum, level_sum)
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        return max_sum
#Print the nodes at odd levels of a tree
    def print_odd_level_nodes(self, node, level=1):
        if not node:
            return
        if level % 2 != 0:
            print(node.val, end=" ")
        self.print_odd_level_nodes(node.left, level + 1)
        self.print_odd_level_nodes(node.right, level + 1)


# Create a binary tree
bt = BinaryTree(10)
bt.insert(bt.root, 5)
bt.insert(bt.root, 15)
bt.insert(bt.root, 3)
bt.insert(bt.root, 7)
bt.insert(bt.root, 12)
bt.insert(bt.root, 18)

print("\nHeight of the tree:", bt.find_height(bt.root))

print("\nPre-order traversal:")
bt.preorder_traversal(bt.root)
print()

print("\nIn-order traversal:")
bt.inorder_traversal(bt.root)
print()

print("\nPost-order traversal:")
bt.postorder_traversal(bt.root)
print()

print("\nLeaves of the tree:")
bt.print_leaves(bt.root)
print()

print("\nBreadth First Search:")
bt.breadth_first_search()
print()

print("\nDepth First Search:")
bt.depth_first_search()
print()

print("\nSum of left leaves:", bt.sum_left_leaves(bt.root))

print("\nSum of all nodes in the tree:", bt.sum_all_nodes(bt.root))

perfect_bt = BinaryTree(1)
perfect_bt.root.left = TreeNode(2)
perfect_bt.root.right = TreeNode(3)
perfect_bt.root.left.left = TreeNode(4)
perfect_bt.root.left.right = TreeNode(5)
perfect_bt.root.right.left = TreeNode(6)
perfect_bt.root.right.right = TreeNode(7)
print("\nSum of nodes in perfect binary tree:", perfect_bt.sum_all_nodes(perfect_bt.root))

print("\nCount of subtrees with sum 8:", bt.count_subtrees_with_sum(bt.root, 8))

print("\nMaximum level sum:", bt.max_level_sum())

print("\nNodes at odd levels:")
bt.print_odd_level_nodes(bt.root)
print()
