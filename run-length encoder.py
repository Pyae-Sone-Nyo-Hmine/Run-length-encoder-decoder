def run_length_encoder(in_string):
    i = 0
    l = []
    in_string+= "/"*10

    for keys in range(len(in_string)-10):
        if in_string[i] != in_string[i+1] and i < len(in_string)-10 and in_string[i]!= "/":
            l.append(in_string[i])
            i += 1
        if in_string[i] == in_string[i+1] and i < len(in_string)-10 and in_string[i]!= "/":
            l.append(in_string[i])
            l.append(in_string[i])
            nl = [1]
            k = 1
            while in_string[i+k-1] == in_string[i + k] and i < len(in_string)-10 and in_string[i]!= "/":
                nl.append(1)
                k += 1

            i += len(nl)

            l.append(len(nl))
            
    return l

