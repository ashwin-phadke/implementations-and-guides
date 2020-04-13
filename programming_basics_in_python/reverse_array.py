import numpy as np
import argparse

# Function to reverse array which will be called recursively
def reverseArray(array, start, end):
    """
    array : input array to reverse
    start : starting index of the array
    end : ending index of the array

    """

    # Check  if you have already gone through the array
    if start >= end:
        return
    
    # Reverse array using this simple python way 
    array[start] , array[end] =  array[end] , array[start]

    # Recursive call to the function
    reverseArray(array, start+1, end-1)



if __name__ == "__main__":
    # Implement argparse to accept command line arguements to choose methods.
    parser = argparse.ArgumentParser(description='This program is to reverse array using recursion')

    # Accept length of array as input in the beginning.
    parser.add_argument('--length', type=int, help='Define length of array')
    args = parser.parse_args()

    # Accept the input numbers as list.
    inp_list = list(map(int,input("\nEnter the numbers : ").strip().split()))[:args.length] 

    # Convert above list to array using numpy
    out_array = np.asarray(inp_list)
    #array = [1, 2, 3, 4, 5, 6]
    print('The entered array : ',out_array)

    reverseArray(out_array, 0, args.length-1)

    print('The reversed array is : ',out_array)
