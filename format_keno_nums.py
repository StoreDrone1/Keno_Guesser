import numpy as np
import load_keno_nums as load_k_nums

def format_keno_list(curList):
    format_k_list = []
    for r in curList:
        #remove the drawing ID and the last element which is the booster of "0"
        r = r[:-1]
        r = r[5:len(r)]
        #remove all empty elements and separate the list by spaces
        r = r.split(" ")
        r = list(filter(None, r))
        format_k_list.append(r)
    return format_k_list

def convert_list_to_int(curA):
    format_list = []
    for i in range(0, len(curA)):
        for j in range(20):
            curA[i][j] = int(curA[i][j])
            format_list.append(curA[i][j])
    return format_list

#format the list and convert to int    
f_keno_list = np.array(load_k_nums.get_nums())

final_list = convert_list_to_int(f_keno_list)

with open("final_keno_nums.txt", 'w') as file:
    file.writelines(final_list)
    file.close()