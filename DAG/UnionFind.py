__author__ = 'mrasquinha'

class UnionFind(object):
    def __init__(self, N):
        self.num_elem = N

        # init the tree such that every elem is its own root
        for i in range(self.num_elem):
            elem[i] = i;

    def print_tree(self, str):
        print(str+"tree is\n")
        for i in range(self.num_elem):
            print(i+"->"+elem[i])


