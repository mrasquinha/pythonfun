__author__ = 'mrasquinha'

class UnionFind(object):

    def __init__(self, N):
        self.no_nodes = N
        self.nodes = []
        self.size = []

        # Init the nodes such that every node is in its own tree with size 1
        # Array convention where element at index i is in a tree
        # with root nodes[i] (Init: node is its own root)
        for i in range(self.no_nodes):
            self.nodes.append(i)
            self.size.append(1)

    def print_tree(self, test_str):
        print test_str,
        for i in range(self.no_nodes):
            print str(self.nodes[i])+" ",
        print

    def union(self, a, b):
        p = self.nodes[a]
        q = self.nodes[b]
        for i in range(self.no_nodes):
            if(self.nodes[i] == p):
                self.nodes[i] = q

    def connected(self, a, b):
        if(self.nodes[a] == self.nodes[b]):
            return True
        else:
            return False

    def root(self,x):
        while(self.nodes[x]!=x):
            x = self.nodes[x]
        return x

    def weighted_union(self, a, b):
        short_tree = self.root(a)
        long_tree = self.root(b)
        # Note: keep trees short and dense; make shorter tree
        # subtree of the root of the long tree
        if(self.size[long_tree] <= self.size[short_tree]):
            #exchange the trees
            tmp = short_tree
            short_tree = long_tree
            long_tree = tmp

        self.nodes[short_tree] = long_tree
        self.size[long_tree] += self.size[short_tree]
        #print str(self.size[p])+" "+str(self.size[q])

    def weighted_connected(self, u, v):
        if (self.root(u) == self.root(v)):
            return True
        else:
            return False

