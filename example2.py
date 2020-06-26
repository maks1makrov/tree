class Manager:
    def __init__(self, root):
        self.root = root

    def add(self, new_node):
        cursore = self.root
        while True:
            if new_node.mark > cursore.mark:
                if cursore.right is not None:
                    cursore = cursore.right
                else:
                    cursore.right = new_node
                    new_node.parent = cursore
                    break
            else:
                if cursore.left is not None:
                    cursore = cursore.left
                else:
                    cursore.left = new_node
                    new_node.parent = cursore
                    break

    def find(self, mark):
        cursore = self.root
        while True:
            if mark == cursore.mark:
                return cursore
            if mark > cursore.mark:
                if cursore.right is not None:
                    cursore = cursore.right
                else:
                    return None
            else:
                if cursore.left is not None:
                    cursore = cursore.left
                else:
                    return None

    def find_all(self, mark):
        cursore = self.root
        result = []
        while True:
            if mark == cursore.mark:
                result.append(cursore.name)
            if mark > cursore.mark:
                if cursore.right is not None:
                    cursore = cursore.right
                else:
                    return result
            else:
                if cursore.left is not None:
                    cursore = cursore.left
                else:
                    return result


class Node:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.right = None
        self.left = None
        self.parent = None

    def __repr__(self):
        return self.name
