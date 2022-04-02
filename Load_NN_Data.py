from doctest import master
from turtle import shape
from warnings import catch_warnings
import numpy as np
import math as mat
import datetime as dt
import time as t
#testing only
start = dt.datetime(2022, 2, 1)
end = dt.datetime.now()
delta = dt.timedelta(days = 1)
#E = mat.e

class Layer_Dense():
    def __init__(self, n_neurons, n_inputs):
        self.weights = 1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forw(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
class Activation_ReLU():
    def forw(self, inputs):
        self.output = np.max(inputs)
class Activation_Softmax():
    def forw(self, inputs):
        e_val = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probs = e_val / np.sum(e_val, axis=1, keepdims=True)
        self.output = probs

master_list = []
temp = []
master_array = []
count = 0
#open a specific day of formatted numbers for testing
with open("formatted_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as file:
    formatted_list = file.readlines()
    #remove newline chars
    formatted_list = list(filter(("\n").__ne__, formatted_list))
    #iterate through each drawing, format the ends and split into list of ints
    for i in formatted_list:
        i = i[1:]
        i = i[:-2]
        i = [int(j) for j in i.split(",")]
        
        #rid the 21's from the final list 
        if(len(i) < 20):
            print("skip")
        else:
            #convert to numpy arrays
            #append to master list and convert to 2d array, pass on the 21's
            master_list.append(np.array(i))
            try:
                master_array = np.vstack(master_list)
            except ValueError:
                pass

    Masterfinal = np.array(master_array)
    #input layer of 292 rows by 20 columns           
    dense1 = Layer_Dense(292, 20)
    activate1 = Activation_ReLU()
    #20 outputs of 20 predictions
    dense2 = Layer_Dense(20, 20)
    activate2 = Activation_Softmax()
    #outputs
    dense3 = Layer_Dense(20, 6)
    activate3 = Activation_ReLU()

    dense1.forw(Masterfinal)
    activate1.forw(dense1.output)

    dense2.forw(activate1.output)
    activate2.forw(dense2.output)

    print(activate1.output)
    print(activate2.output[:1])
        
        #min_max_list.append(sum(i))
        #print(sum(i))
         #add formatted str list to final list
        #master_list.append(i)
        #print("size of i = {}".format(len(i)))
    #min_max_list.sort()
    #print("lowest of minmax = {}, highest = {}".format(min_max_list[0], min_max_list[-1]))
    #print(master_list)