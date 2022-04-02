#format the keno files for Pandas dataframe
import numpy as np
import datetime as dt
import os.path
from numpy.core.defchararray import index
from numpy.core.fromnumeric import size
import time

def get_file():
    start = dt.datetime(2022, 3, 13)
    end = dt.datetime.now()
    delta = dt.timedelta(days = 1)
    page = 0
    page_max = 0

    while start != end:
        #check if files are there
        formatted_list = []
        list_to_format = []
        if os.path.exists("keno_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
            #open the current file for reading data...
            with open("keno_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as cur_keno_file:
                list_to_format = cur_keno_file.readlines()
                #DOWN WITH THE NEWLINES! 
                list_to_format = list(filter(("\n").__ne__, list_to_format))  
                #remove the last whitespace and booster number, the drawing number and split the string into an integer list
                for i in list_to_format:
                    i = i[:-2]
                    if start.year == 2009:
                        i = i[5:]
                    elif start.year == range(2010, 2019):
                        i = i[6:]
                    else:
                        i = i[7:]   
                    i = [int(j) for j in i.split()]
                    #add formatted str list to final list
                    formatted_list.append(i)
                    #write out the data in readable format and with new filename
                    with open("formatted_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", 'a') as lottery_file:
                        lottery_file.writelines(str(i) + "\n")
                        
            start += delta
        else:
            start += delta  
        print("Finished Formatting data.")    
    return formatted_list

gen_formatted_list = get_file()
