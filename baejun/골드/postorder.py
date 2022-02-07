from collections import deque

import sys

from sympy import Q
sys.setrecursionlimit(10 ** 6)
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right=None
        self.parent = None

class binarytree:
    def __init__(self):
        self.root=None

    def insert(self, data):
        newnode=node(data)
        if self.root==None:
            self.root = newnode
        
        else:
            self.curnode=self.root
            
            while True:
                if self.curnode.data > newnode.data:
                    if self.curnode.left !=None:
                        self.curnode=self.curnode.left
                    else:
                        newnode.parent=self.curnode
                        self.curnode.left=newnode
                        break
                else:
                    if self.curnode.right !=None:
                        self.curnode=self.curnode.right
                    else:
                        newnode.parent=self.curnode
                        self.curnode.right=newnode
                        break

    def postorder(self, root):
        stack=deque()
        result =[]
        stack.append(root)
        while stack:
            cur = stack.pop()
            result.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result
    def preorder(self, root):
        queue = deque()
        result =[root]
        queue.append(root)
        while queue:
            cur=queue.popleft()
            if cur.left != None and cur.left not in result: 
                cur=cur.left
                queue.append(cur)
                result.append(cur)
            elif cur.right != None and cur.right not in result :
                cur = cur.right
                queue.append(cur)
                result.append(cur)
            else: 
                if cur.parent == None:
                    break
                cur = cur.parent; queue.append(cur)
            if len(result) ==chk: break

        return result

    def inorder(self, root):
        queue= deque()
        result = []
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.left !=None and cur.left not in result:
                cur = cur.left
                queue.append(cur)
            elif cur.right != None and cur.right not in result:
                cur = cur.right
                queue.append(cur)
            else: 
                result.append(cur)
                if cur not in result and (cur.parent.right== None or cur.parent.left ==None): result.append(cur)
                elif cur not in result and cur.parent.right == cur: result.append(cur)

                cur = cur.parent

                queue.append(cur)
                if len(result) == chk: break

        return result


tree = binarytree()
chk=0
while True:
    try: 
        data = int(sys.stdin.readline())
        tree.insert(data)
        chk+=1
    except:
        chk-=1
        break
data =tree.inorder(tree.root)

while data:
    print(data.pop(0).data)
