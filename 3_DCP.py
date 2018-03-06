'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

'''

class BinaryNode(object):

    def __init__(self,id):
        self.id = id
        self.data = id
        self.ptr_left = None
        self.ptr_right = None

    def __str__(self): return str(self.id)

class BinaryTree(object):            

    def __init__(self):
        self.__head = None
        self.items = 0

    def pre_order(self):

        # print yourself, go left, go right

        print('Start Pre Order')
        if not self.__head is None:
            self.__pre_order_helper(self.__head)

    def __pre_order_helper(self,current_node):

        print(current_node)
        
        if current_node.ptr_left:
                self.__pre_order_helper(current_node.ptr_left)

        if current_node.ptr_right:
                self.__pre_order_helper(current_node.ptr_right)

    def in_order(self):

        # keep going left, print yourself, go right

        print('Start In Order')
        if not self.__head is None:
            self.__in_order_helper(self.__head)

    def __in_order_helper(self,current_node):

        if current_node.ptr_left:
            self.__in_order_helper(current_node.ptr_left)
                
        print(current_node)
            
        if current_node.ptr_right:
            self.__in_order_helper(current_node.ptr_right)

    def post_order(self):

        # go left, go right, print yourself on the way back

        print('Start Post Order')
        if not self.__head is None:
            self.__post_order_helper(self.__head)

    def __post_order_helper(self,current_node):

        if current_node.ptr_left:
            self.__post_order_helper(current_node.ptr_left)

        if current_node.ptr_right:
            self.__post_order_helper(current_node.ptr_right)

        print(current_node)

    def add(self,id):

        if self.__head is None:
            self.__head = BinaryNode(id)
            self.items = self.items + 1
        else:
            self.__add_helper(id,self.__head)
            
    def __add_helper(self,id,current_node):
        
        if id < current_node.id:
             if current_node.ptr_left:
                self.__add_helper(id,current_node.ptr_left)
             else:
                current_node.ptr_left = BinaryNode(id)
                self.items = self.items + 1
        else:
            if current_node.ptr_right:
                self.__add_helper(id,current_node.ptr_right)
            else:
                current_node.ptr_right = BinaryNode(id)
                self.items = self.items + 1

        #self.balance_tree()

    def height(self,*args,**kwargs):
        # not implemented properly 
        # 
        #

        if kwargs.get('id'):
            node = self.bfs(kwargs['id'])
            return self.__is_balanced_helper(node)
        elif kwargs.get('node'):
            return self.__is_balanced_helper(kwargs['node'])
        else:
            if self.__head is None:
                return 0
            else:
                return self.__is_balanced_helper(self.__head)

    def is_balanced(self):

        if self.__head is None:
            return True
        else:
            return self.__is_balanced_helper(self.__head)>=0

    def __is_balanced_helper(self,parent):

        if not parent:
            return 0

        left_sub = self.__is_balanced_helper(parent.ptr_left)
        right_sub = self.__is_balanced_helper(parent.ptr_right)

        
        if (left_sub < 0 or
            right_sub < 0 or
            abs(left_sub - right_sub) > 1):
            return -1
        else:
            return max(left_sub,right_sub)+1        

    def bfs(self,id):
        if self.__head is None:
            return None
        else:
            return self.__bfs_helper(self.__head,id)

    def __bfs_helper(self,head_node,id):

        node_queue = []
        node_queue.append(head_node)

        while node_queue:

            current_node = node_queue.pop(0)

            if current_node.id == id:
                return current_node
            else:
                if current_node.ptr_left:
                    node_queue.append(current_node.ptr_left)
                if current_node.ptr_right:
                    node_queue.append(current_node.ptr_right)
        return None

    def dfs(self,id):
        if self.__head is None:
            return None
        else:
            return self.__dfs_helper(self.__head,id)

    def __dfs_helper(self,head_node,id):

        node_stack = []
        node_stack.append(head_node)

        while node_stack:

            current_node = node_stack.pop()

            if current_node.id == id:
                return current_node
            else:
                if current_node.ptr_right:
                    node_stack.append(current_node.ptr_right)
                if current_node.ptr_left:
                    node_stack.append(current_node.ptr_left)
        return None

    def serialize(self):

        # this works with a bin search tree because of the comparison....
        # this would need to either a output inorder and preorder traversals (pre to create the treen, in order to find children nodes)
        # or we could store the null nodes too so that we know when part of the tree ends...
        # solutions somewhat depend on (scope, known data set, etc)

        serialized_string = ['']

        self.__serialize_helper(self.__head,serialized_string)

        return serialized_string[0]

    def __serialize_helper(self,current_node,serialized_string):

        serialized_string[0] = serialized_string[0] + current_node.data

        if current_node.ptr_left:
            self.__serialize_helper(current_node.ptr_left,serialized_string)

        if current_node.ptr_right:
            self.__serialize_helper(current_node.ptr_right,serialized_string)

    def deserialize(self,tree_string):

        [ self.add(item) for item in tree_string ]
        return None





def main():

   
    items = ['F','B','G','A','D','C','E','I','H']
    
    bin_tree = BinaryTree()
    for item in items:
        bin_tree.add(item)

    bin_tree.pre_order()

    first_tree = bin_tree.serialize()
    print("-"*10)

    new_tree = BinaryTree()
    new_tree.deserialize(first_tree)
    new_tree.pre_order()
            
if __name__ == '__main__':
    main()