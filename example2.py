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

    def delete(self, mark):
        cursore = self.root
        while True:
            if mark == cursore.mark:
                if cursore.left and cursore.right:
                    new = cursore.right
                    while True:
                        if new.left:
                            new = new.left
                        else:
                            break
                    cursore.name, cursore.mark = new.name, new.mark
                    if new.right:
                        new_next = new.right
                        new.name, new.mark, new.left, new.right = new_next.name, new_next.mark, new_next.left, new_next.right
                        del(new_next)
                    else:
                        new_next = new.parent
                        new_next.left = None
                        del(new)
                elif cursore.left or cursore.right:
                    if cursore.left:
                        new = cursore.left
                        cursore.name, cursore.mark, cursore.right, cursore.left = new.name, new.mark, new.right, new.left
                        del(new)
                    else:
                        new = cursore.right
                        cursore.name, cursore.mark, cursore.right, cursore.left = new.name, new.mark, new.right, new.left
                        del(new)
                else:
                    new = cursore.parent
                    if new.right == cursore:
                        new.right = None
                    else:
                        new.left = None
                    del(cursore)
                return f"deleted of mark - {mark} is done "
            if mark > cursore.mark:
                if cursore.right is not None:
                    cursore = cursore.right
                else:
                    return f"can not find mark - {mark}"
            else:
                if cursore.left is not None:
                    cursore = cursore.left
                else:
                    return f"can not find mark - {mark}"


class Node:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.right = None
        self.left = None
        self.parent = None

    def __repr__(self):
        return self.name
