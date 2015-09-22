from UnionFind import UnionFind

__author__ = 'mrasquinha'

#algos1: Problem 1; 3-9 0-5 3-8 8-5 2-3 6-3
uf= UnionFind(10)
uf.print_tree("Init")
uf.union(3,9)
uf.union(0,5)
uf.union(3,8)
uf.union(8,5)
uf.union(2,3)
uf.union(6,3)
uf.print_tree("Ans1:")

#algos1: Problem 2; 1-6 5-4 9-3 5-9 7-1 6-0 0-8 6-3 2-6
uf2 = UnionFind(10)
uf2.weighted_union(1,6)
uf2.weighted_union(5,4)
uf2.weighted_union(9,3)
uf2.weighted_union(5,9)
uf2.weighted_union(7,1)
uf2.weighted_union(6,0)
uf2.weighted_union(0,8)
uf2.weighted_union(6,3)
uf2.weighted_union(2,6)
uf2.print_tree("Ans2:")

