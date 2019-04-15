import os
from collections import deque

input_path = os.path.join(os.getcwd(),'8','input.txt')
input_data = open(input_path).read().split(' ')

def build_tree(input_data):
    data = deque(input_data)

    def build_node():
        num_children = int(data.popleft())
        num_metadata = int(data.popleft())
        node = {}
        node['Children'] = []
        node['Metadata'] = []

        for _ in range(num_children):
            node['Children'].append(build_node())

        for _ in range(num_metadata):
            node['Metadata'].append(int(data.popleft()))
        
        return node
        
    root = build_node()
    return root

def sum_metadata(root):
    
    def sum_child_metadata(node):
        subtotal = 0
        for child in node['Children']:
            subtotal += sum_child_metadata(child)
        
        for metadata in node['Metadata']:
            subtotal += metadata

        return subtotal
    
    return sum_node_metadata(root)

def checksum(root):

    def node_checksum(node):
        subtotal = 0

        if len(node['Children']) == 0:
            for metadata in node['Metadata']:
                subtotal += metadata
        else:
            for index in node['Metadata']:
                if index != 0 and index <= len(node['Children']):
                    subtotal += node_checksum(node['Children'][index - 1])

        return subtotal
    
    return node_checksum(tree)

tree = build_tree(input_data)
total = sum_metadata(tree)
print(total)
total = checksum(tree)
print(total)
