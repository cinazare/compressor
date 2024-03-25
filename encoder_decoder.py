from tree_maker import *

def encoder(adress):
    tree_node_dict = get_data_from_txt(adress)
    hufman_code = huffmancode_executer(tree_node_dict)

    # making an strong with my huffman_code string
    hufman_code = hufman_code.split(",")
    del hufman_code[0]


    hufman_code_dict = dict()
    
    for temp in hufman_code:
        temp = temp.split(":")
        hufman_code_dict[int(temp[0].strip())] = temp[1].strip()

    lenth = 0
    for key, value in hufman_code_dict.items():
        lenth +=  tree_node_dict[str(key)] * len(value)
    
    writer(hufman_code_dict, adress, lenth)

    return hufman_code_dict

def writer(huffman_code, adress, lenth):
    commpressed_addres = adress
    for temp in range(1,len(commpressed_addres)):
        
        if commpressed_addres[-1] == "/":
            commpressed_addres = commpressed_addres[:-1]
            break
        
        else:
            commpressed_addres = commpressed_addres[:-1]
     

    dictionary = open(commpressed_addres +'/compressed.bin', "w", encoding="utf-8")

    # writing the dictionary
    for key, value in huffman_code.items(): 
        if chr(key) == "1" or chr(key) == "0":
            dictionary.write("'" + chr(key) + "'" + value)
        else: 
            dictionary.write(chr(key)+value)

    dictionary.write("$" + str(lenth) + "$")
    dictionary.write("\n")

    dictionary.close()
    
    txt = open(adress, "r")
    compress = open(commpressed_addres +'/compressed.bin', "ab")
    
    txt_lines = txt.read()
    
    string = str()
    for letter in txt_lines:
        string += huffman_code[int(ord(letter))]
    

    while True:
        if len(string) % 8 != 0:
            string += "0"
        else:
            break
    bytes = _to_Bytes(string)
    compress.write(bytes)        
        
    print("your file is compressed")
    txt.close()
    compress.close()        





def _to_Bytes(data):
    b = list()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i+8], 2))
    b = bytearray(b)
    return b      







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


