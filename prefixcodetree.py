'''
class Node
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

'''
class Tree
'''
class Tree:
    def __init__(self):
        self.root = Node(None)
        self.current = None
    def add(self,codeword, symbol):
        self.current = self.root
        for i in range(0, len(codeword) - 1):
            if(codeword[i] == 0):
                if(self.current.left == None):
                    self.current.left = Node(None)
                self.current = self.current.left
            else:
                if(self.current.right == None):
                    self.current.right = Node(None)
                self.current = self.current.right
        end = len(codeword) - 1
        if(codeword[end] == 0):
            self.current.left = Node(symbol)
        else:
            self.current.right = Node(symbol)
    def find(self, sbin):
        message = ""
        self.current = self.root
        for c in sbin:
            if(c == '1'):
                self.current = self.current.right
                #print("right")
            else:
                self.current = self.current.left
                #print("left")
            if(self.current.value != None):
                message+=self.current.value
                self.current = self.root
                
        return message        
            
'''
class PrefixCodeTree
'''
class PrefixCodeTree:
    def __init__(self):
        self.tree = Tree()
    def insert(self, codeword, symbol):
        self.tree.add(codeword, symbol)
    def decode(self, encodedData, datalen):
        sbin = ""
        l = list(encodedData)
        for i in l:
            ssbin = bin(i)[2:].zfill(8)
            sbin+=ssbin
        sbin = sbin[:datalen]
        message = self.tree.find(sbin)
        return message
        
'''
test code
'''
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}

codeTree = PrefixCodeTree()
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd5\x6f\x2e',21)
print(message)