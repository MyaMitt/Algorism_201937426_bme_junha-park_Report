import numpy as np

class Node:
    def __init__(self, key):
        self.__key = key
        self.__left: Node = None
        self.__right: Node = None

    def __str__(self) -> str:
        return (f'node(key: {self.get_key()})')
    
    def print_tree(self, print_list:list = []):
        if self.get_right():
            self.get_right().print_tree(print_list)
        else:
            print_list.append('none_right')

        print_list.append(self.get_key())

        if self.get_left():
            self.get_left().print_tree(print_list)
        else:
            print_list.append('none_left') 

    def get_key(self):
        return self.__key
    
    def set_left(self, link):
        self.__left = link

    def get_left(self):
        return self.__left
    
    def set_right(self, link):
        self.__right = link

    def get_right(self):
        return self.__right
    
    def insert_child(self, key):
        if self.search(key):
            print(f'error, find key {key}, binary tree is can not insert same key')
            raise

        if self.get_key() < key:
            if self.get_right():
                self.get_right().insert_child(key)
            else:
                node = Node(key)
                self.set_right(node)
        else:
            if self.get_left():
                self.get_left().insert_child(key)
            else:
                node = Node(key)
                self.set_left(node)
    

    def search(self, key):
        if self.get_key() == (key):
            return self

        elif self.__key < key:
            if self.get_right():
                return self.get_right().search(key)
            else:
                return False
            
        else:
            if self.get_left():
                return self.get_left().search(key)
            else:
                return False

    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.dim = 0

    def show_tree(self):
        
        list = []
        self.root.print_tree(list)

        for i in list:
            tap = 0
            if isinstance(i, (int, np.int32)):
                focus = self.root
                while focus:
                    if focus.get_key() == i:
                        break
                    elif focus.get_key() < i:
                        focus = focus.get_right()
                    else:
                        focus = focus.get_left()

                    tap +=1
                if focus.get_right():
                    print('\t'*tap,'  /')
                print('\t'*tap, i)
                if focus.get_left():
                    print('\t'*tap,'  \\')
            else:
                #print()
                pass

    
    def append(self, key):
        if self.root:
            # root 가 있을 때
            self.root.insert_child(key)
        else:
            # root 가 없을 때
            self.root = Node(key)

    def append_to_list(self, keys:list):
        for key in keys:
            self.append(key)

    def search(self, key):
        return self.root.search(key)
    
    def delete_node(self, key):
        node = self.search(key)
        if not node:
            print(f'cannot found node, key: {key}')
            return False
        parent = self.get_node_parent(key)
        
        if node == self.root:
            if node.get_left() and node.get_right():
                focus:Node = node.get_right()
                
                checker = False

                while focus.get_left():
                    focus = focus.get_left()
                    checker = True

                if checker:
                    self.get_node_parent(focus.get_key()).set_left(focus.get_right())
                else:
                    self.get_node_parent(focus.get_key()).set_right(focus.get_right())

                self.root = focus

                focus.set_left(node.get_left())
                focus.set_right(node.get_right())

                del node


            elif node.get_left():
                if parent.get_key() < key:
                    parent.set_right(node.get_left())
                else :
                    parent.set_left(node.get_left())
                del node
                
            elif node.get_right():
                if parent.get_key() < key:
                    parent.set_right(node.get_right())
                else :
                    parent.set_left(node.get_right())
                del node
            else:
                if parent.get_key() < key:
                    parent.set_right(None)
                else :
                    parent.set_left(None)
                del node
        else: 
            if node.get_left() and node.get_right():
                focus = node.get_right()
                
                checker = False

                while focus.get_left():
                    focus = focus.get_left()
                    checker = True

                if checker:
                    self.get_node_parent(focus.get_key()).set_left(focus.get_right())
                else:
                    self.get_node_parent(focus.get_key()).set_right(focus.get_right())


                if parent.get_key() < key:
                    parent.set_right(focus)
                else :
                    parent.set_left(focus)

                focus.set_left(node.get_left())
                focus.set_right(node.get_right())

                del node


            elif node.get_left():
                if parent.get_key() < key:
                    parent.set_right(node.get_left())
                else :
                    parent.set_left(node.get_left())
                del node
                
            elif node.get_right():
                if parent.get_key() < key:
                    parent.set_right(node.get_right())
                else :
                    parent.set_left(node.get_right())
                del node
            else:
                if parent.get_key() < key:
                    parent.set_right(None)
                else :
                    parent.set_left(None)
                del node


    def get_node_parent(self, key):
        focus = self.root

        parent = None
        
        while focus.get_key() != key:
            parent = focus
            if focus.get_key() < key:
                focus = focus.get_right()
            else :
                focus = focus.get_left()

        return parent
        

        