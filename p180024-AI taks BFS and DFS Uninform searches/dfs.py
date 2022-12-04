class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
        
class BST(TreeNode): # BSt IS a child class of TREENODE okay.
    def __init__(self,val,parent=None):
        super().__init__(val)
        self.parent=parent
        #self.root=self #root will point to new node created by BSt object  
        
    def insert(self,key):
        if key<self.val:
            if (self.left is None):
                newnode=BST(key, parent=self)
                self.left=newnode
            else:
                self.left.insert(key)
                
        if key>self.val:
            if self.right is None:
                newnode=BST(key,parent=self)
                self.right=newnode
            else:
                self.right.insert(key)
def dfs(self):
    print(self.val)
    if self.left:
        self.left.dfs()
    if self.right:
        self.right.dfs()
TreeNode.dfs=dfs    


def dfs_inorder(self):
   
    if self.left:
        self.left.dfs_inorder()
    print(self.val)
    if self.right:
        self.right.dfs_inorder()
TreeNode.dfs_inorder=dfs_inorder



          
def dfs_postorder(self):
   
    if self.left:
        self.left.dfs_postorder()
    
    if self.right:
        self.right.dfs_postorder()
    print(self.val)
TreeNode.dfs_postorder=dfs_postorder


          
def find_root(self):
    temp=self
    while temp.parent is not None:
        temp=temp.parent
    return temp
BST.find_root=find_root
       
def find_root(self):
    temp=self
    while temp.parent is not None:
        temp=temp.parent
    return temp
BST.find_root=find_root


       
def set_for_parent(self,new_ref):
    if self.parent is None:
        return
    if self.parent.right==self:
        self.parent.right=new_ref
    if self.parent.left==self:
        self.parent.left=new_ref
BST.set_for_parent=set_for_parent
          
          
          
def replace_with_node(self,node):
    self.set_for_parent(node)
    node.parent=self.parent
    self.parent=None
    return node.find_root()
BST.replace_with_node=replace_with_node
          
def delete(self,val):
    if self.parent is None and self.right is None and self.left is None and self.val==val:
        return None
    if self.val==val:
        if self.right is None and self.left is None:
            self.set_for_parent(None)
            return self.find_root()
    
        if self.right is None:
            return self.replace_with_node(self.left)
        if self.left is None:
            return self.replace_with_node(self.right)
        
        successor =self.right.find_min()
        self.val=successor.val
        return self.right.delete(successor.val)
    if val< self.val:
        if self.left is not None:
            return self.left.delete(val)
        else:
            return self.find_root()
    else:
        if self.right is not None:
            return self.right.delete(val)
        else:
            return self.find_root()
BST.delete = delete


def find_value(self,val):
    if self.val==val:
        print("value found : ",self.val)
        return 
    #print(self.val)
    if val<self.val and self.left is None:
        print("No Value")
        return 
    if val>self.val and self.right is None:
        print("No Value")
        return 
    
    if val<self.val and self.left is not None:
        self.left.find_value(val)
    if val>self.val and self.right is not None:
        self.right.find_value(val)
        
    
    
TreeNode.find_value=find_value
########################################################################################

#                                           DFS on Binary Search Tree all in post and root order appalyed 
b=BST(20)
#print(b.val)
b.insert(24)
b.insert(10)
b.insert(1)    

b.dfs()
print("inorder")
b.dfs_inorder()
print("post order")

b.dfs_postorder()

print("find the value")
b.find_value(50)