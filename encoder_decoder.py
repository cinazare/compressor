from tree_maker import *

def encoder(adress):
    tree_node_dict = get_data_from_txt(adress)
    hufman_code = huffmancode_executer(tree_node_dict)




def huffmancode_executer(tree_node_dict):
    # making tree objects with one node to start an adding them to huffman_list

    huffman_list = list()
    for ascii in tree_node_dict.keys():
        node = TREE(ascii, tree_node_dict[ascii])
        huffman_list.append(node)
    
    
    

    # use an order list to make them in order base on thier sequense
    for x in range(len(huffman_list)):
        for y in range(x, len(huffman_list)):
            
            if huffman_list[x].sequence > huffman_list[y].sequence:
                temp = huffman_list[x]
                huffman_list[x] = huffman_list[y]
                huffman_list[y] = temp

    
    

    huffman_tree_root = huffman_tree_maker(huffman_list)
    
    huffman_code = huffman_code_maker(huffman_tree_root, "")
    
    return huffman_code

def huffman_code_maker(huffman_tree_root, code):

    if huffman_tree_root.left and huffman_tree_root.right:
        return huffman_code_maker(huffman_tree_root.right, code+"0") + huffman_code_maker(huffman_tree_root.left, code+"1")
    
    else:
        return " , " + huffman_tree_root.ascii + " : " +code

def get_data_from_txt(adress):
    
    txt_file = open(adress, 'r')
    lines = txt_file.read()
    
    sequence_dict = dict()
    
    for letter in lines:
        

        if str(ord(letter)) in sequence_dict.keys():
            sequence_dict[str(ord(letter))] += 1

        else:
            sequence_dict[str(ord(letter))] = 1
    

    txt_file.close()
    return sequence_dict


def huffman_tree_maker(huffman_list):
    
    while len(huffman_list) > 1:
        
        littel1 = huffman_list[0]
        littel2 = huffman_list[1]
        del huffman_list[0]
        del huffman_list[0]
        
        new_node = TREE(littel1.ascii + "," + littel2.ascii, littel1.sequence + littel2.sequence)
        new_node.append_to_right(littel1)
        new_node.append_to_left(littel2)
        
        if not huffman_list:
            return new_node


        for index in range(len(huffman_list)):
            if new_node.sequence >= huffman_list[len(huffman_list)-1].sequence:
                huffman_list.append(new_node)
                break    
        
        
            if huffman_list[index].sequence >= new_node.sequence:
                huffman_list.insert(index, new_node)
                break