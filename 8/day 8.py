
input_data = open('.\\8\\input.txt').read().split(' ')

def build_tree(input_data):
    data = input_data[:]

    def build_node():
        num_children = int(data.pop(0))
        num_metadata = int(data.pop(0))
        node = {}
        node['Children'] = []
        node['Metadata'] = []

        for _ in range(num_children):
            node['Children'].append(build_node())

        for _ in range(num_metadata):
            node['Metadata'].append(int(data.pop(0)))
        
        return node
        
    root = build_node()
    print('Done!')  
    return root

tree = build_tree(input_data)

def sum_metadata(tree):
    
    def sum_child_metadata(node):
        subtotal = 0
        for child in node['Children']:
            subtotal += sum_child_metadata(child)
        
        for metadata in node['Metadata']:
            subtotal += metadata

        return subtotal
    
    return sum_child_metadata(tree)

total = sum_metadata(tree)
print(total)

def checksum(tree):

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

total = checksum(tree)
print(total)