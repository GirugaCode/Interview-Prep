'''
Given a binary tree, check whether it is a mirror of itself.

For example, this binary tree is symmetric:

     1
   /   \
  2     2
 / \   / \
3   4 4   3

But the following is not:


    1
   / \
  2   2
   \   \
   3    3

Pseudocode:
If root is empty then I can return true

Check if left node is not equal to the right node
    return false
otherwise
    Get to the left node
    Get the right node
        Check if left nodes right child is not equal to right nodes left child
            return false
        Check if left nodes left child is not equal to right nodes right child
            return false
    Recursivly call the left nodes and right nodes

Return true if all the checks have been made 
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_symmetric(root: Node) -> bool:
    if not root:
        return True
    return helper(root.left, root.right)

def helper(node_left: Node, node_right: Node) -> bool:
    if node_left is None and node_right is None:
        return True

    if node_left is None or node_right is None:
        return False

    if node_left.key != node_right.key:
        return False

    return helper(node_left.left, node_right.right) and helper(node_left.right, node_right.left)


def refactored_is_symmetric(root: Node) -> bool:
    if not root:
        return True

    return helper(root.left, root.right)

def refactored_helper(left_node: Node, right_node: Node) -> bool:
    if not left_node and not right_node:
        return True

    if not left_node or not right_node:
        return False

    if left_node.key != right_node.key:
        return False

    # Get next values
    outer_left, outer_right = left_node.left, right_node.right
    inner_right, inner_left = left_node.right, right_node.left

    # Recursivly compare nodes
    is_outer_symmetrical = helper(outer_left, outer_right)
    is_inner_symmetrical = helper(inner_left, inner_right)

    return is_outer_symmetrical and is_inner_symmetrical



def main():
    symmetric_test_tree = Node(10)

    # 1st level
    symmetric_test_tree.left = Node(11)
    symmetric_test_tree.right = Node(11)

    # 2nd level
    symmetric_test_tree.left.left = Node(12)
    symmetric_test_tree.left.right = Node(13)

    # 2nd level
    symmetric_test_tree.right.left = Node(13)
    symmetric_test_tree.right.right = Node(12)

    asymmetric_test_tree = Node(10)

    # 1st level
    asymmetric_test_tree.left = Node(11)
    asymmetric_test_tree.right = Node(11)

    # 2nd level (Missing right node)
    asymmetric_test_tree.left.left = Node(12)

    # 2nd level
    asymmetric_test_tree.right.left = Node(12)
    asymmetric_test_tree.right.right = Node(12)

    print(refactored_is_symmetric(symmetric_test_tree))

if __name__ == "__main__":
    main()
