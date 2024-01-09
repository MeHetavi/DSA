class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Main:
  def buildTree(inorder : list[int], postorder:list[int]):
    postorder = list(reversed(postorder))
    root = TreeNode(val = postorder[0])
    if len(inorder) == 1:
        return root
    else:
        i = inorder.index(postorder[0])
        left = inorder[:i]
        right = inorder[i+1:]
        if right != [] :
            root.right = buildTree(right,postorder[1:len(right)+1])
        if left != []: 
            root.left = buildTree(left,postorder[len(right)+1:])    
        return root

    def buildTree(inorder: list[int],preorder: list[int]) :
            root = TreeNode(val = preorder[0])
            if len(inorder) == 1:
                return root
            else:
                i = inorder.index(preorder[0])
                left = inorder[:i]
                right = inorder[i+1:]
                if left != [] :
                    root.left = buildTree(left,preorder[1:len(left)+1])
                if right != []: 
                    root.right = buildTree(right,preorder[len(left)+1:])    
                return root
