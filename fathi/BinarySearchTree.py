# class Node:
#     def __init__(self,info):
#         self.info = info
#         self.left = None
#         self.right = None
#     def insert(self,item):
#         if item <self.info:
#             if self.left is None:
#                 self.left =Node(item)
#             else:
#                 self.left.insert(item)
#         else:
#             if self.right is None:
#                 self.right =Node(item)
#             else:
#                 self.right.insert(item)
#     def inorder(self):
#         if self.left is not None:
#             self.left.inorder()
#         print(self.info,end=" ")
#         if self.right is not None:
#             self.right.inorder()


class Node:
    left = None
    info = 0
    right = None

    def __init__(self, info):
        self.info = info


class BST:
    root = None

    def insert(self, item):
        node = Node(item)
        if (self.root == None):
            self.root = node
            return
        post = None
        p = self.root
        while (p != None):
            if (p.info > item):
                post = p
                p = p.left
            elif (p.info < item):
                post = p
                p = p.right
        if (post.info > item):
            post.left = node
        else:
            post.right = node

    def __inorderTraversal(self, p):
        if p != None:
            if p.left is not None:
                self.__inorderTraversal(p.left)
            print(p.info, end=" ")
            if p.right is not None:
                self.__inorderTraversal(p.right)

    def inorder(self):
        p = self.root
        self.__inorderTraversal(p)


test = BST()
for i in range(7):
    x = int(input())
    test.insert(x)
test.inorder()
