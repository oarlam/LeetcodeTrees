class Node:
    def __init__(self, left, right, data):
        self.value = data
        self.right = right
        self.left = left



def tree_by_levels(node):

    def recursive_search(node, d = {}, h = 0):
        if node is None:
            return {}
        d.setdefault(h, [])
        d[h] += [node.value]
        recursive_search(node.left, d, h+1)
        recursive_search(node.right, d, h+1)
        return d
    dictionary = recursive_search(node)
    lst = []
    for k in dictionary:
        lst += dictionary[k]
    return lst
