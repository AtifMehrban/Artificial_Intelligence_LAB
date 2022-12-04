class TreeNode:
    def __init__(self,val):
        #s=Stack()
        self.val=val
        self.left=None
        self.right=None
        
def print_tree(tree,level=0,label='.'):
    print(' ' * (level*2)+label+ ':',tree.val)
    for child,lbl in zip([tree.left , tree.right],['L','R']):
        if child is not None:
            print_tree(child,level+1,lbl)
######################   
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
                
                
    def bfs1(self):
        to_visit=[self]
        while to_visit:
            current=to_visit.pop(0)
            print(current.val)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)



if __name__ == '__main__':
    b=BST(50)
    b.insert(30)
    b.insert(15)
    b.insert(35)
    b.insert(7)
    b.insert(22)

    b.insert(70)
    b.insert(62)
    b.insert(87)

    b.insert(51)
    b.insert(52)
    b.insert(53)
    b.insert(31)
    b.insert(32)
    b.insert(33)
    print_tree(b)
    
    print("bfs algo")
    #1=BST(100)
    #bfs(b1)
    b.bfs1()