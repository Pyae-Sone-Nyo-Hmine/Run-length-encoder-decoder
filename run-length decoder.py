def run_length_decoder(in_list):

    in_copy = in_list.copy()

    in_copy.append("/")
    in_copy.append("/")
    in_copy.append("/")
    
    i = 0
    string =""
    for keys in range(len(in_copy) - 3):
        if in_copy[i] != in_copy[i + 1]:
            string += in_copy[i]
            i += 1
        if in_copy[i] == in_copy[i + 1] and type(in_copy[i + 2]) == int :
            string += in_copy[i] * in_copy[i + 2]
            i += 3
            
    return string

