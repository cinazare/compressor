class TREE:
    def __init__(self, ascii, sequence = 0, right = None, left = None, dad = None):
        self.ascii = ascii
        self.sequence = sequence
        self.right = right
        self.left = left
        self.dad = dad

    def append_to_right(self, other):
        if self.right != None:
            print("the right node is full already")
            return
    
        self.right = other
        other.dad = self
        return
    def append_to_left(self, other):
        
        if self.left != None:
            print("the right node is full already")
            return
    
        self.left = other
        other.dad = self
        return
    

    def display(self):
        if  self.left:
            self.left.display()
            self.right.display()
            print(self.ascii, " : ", self.sequence)
            return
        elif self.right:
            self.right.display()
            print(self.ascii, " : ", self.sequence)
            return
        else:
            print(self.ascii, " : ", self.sequence)
