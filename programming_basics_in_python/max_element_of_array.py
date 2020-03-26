import math
import argparse
import numpy as np


# Function to find maximum element from an array
def max_element_of_array(array, length_of_array):
    """
        array : the array entered by user to find the maximum element from.
        length_of_array : array length to iterate over to.
    """
    
    # Store maximum number in an array to a variable which is always the first element.
    max_num = array[0]

    # Iterate from the 1st element as the 0th(first) element of array is already assigned to the max_num variable.
    for i in range(0, length_of_array):

    # Check if current array element is greater than max_num
        if array[i] > max_num :

        # If yes then update max_num
            max_num  = array[i]

    # Return the maximum number obtained from the iterataion above
    return max_num

if __name__ == "__main__":

    # Implement argparse to accept command line arguements to choose methods.
    parser = argparse.ArgumentParser(description='This program finds the maximum number from an array')

    # Accept length of array as input in the beginning.
    parser.add_argument('--length', type=int, help='Define length of array')
    args = parser.parse_args()

    # Accept the input numbers as list.
    inp_list = list(map(int,input("\nEnter the numbers : ").strip().split()))[:args.length] 

    # Convert above list to array using numpy
    out_array = np.asarray(inp_list)

    print('The entered array : ',out_array)

    max_out = max_element_of_array(out_array, args.length)
    
    print('Maximum number is : ', max_out)

    



    