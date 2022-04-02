# Keno_Guesser
Use a neural network to guess the next numbers.
1.) Run load_keno_numbers to get all keno drawings up to the current date.
2.) Run format_keno_numbers to remove all tags and whitespaces from the dataset and converts the list to int array
3.) Run simple Keno math to get an idea of how the data looks.
4.) get_keno_modes isn't implemented yet.
5.) Run NNPrep to see harmonic means of the dataset, variance and standard deviation as well ( just data viewing purposes )
6.) Run Load_NN_Data takes formatted numbers and uses relu and softmax activations, loss hasn't been implemented. TODO: Figure out how to implement the output 
    with other files output data from simple keno math and NN Prep to acheive "guesses" of upcoming Keno Drawings based on every pattern/number combination that has       happened before.  For example if the 20 numbers that come up in the new drawing are ( for simplicity ) [1,2,3,....20].  In theory and probablity there is almost 0     chance that the numberset drawn will never happen again.  How to find patterns in the dataset and be able to, with at least a better chance, of predicting between 2     - and 6 total numbers.
