


import math
import argparse
import numpy as np

# Function to find maximum consecutive elements in an binary array
def getMaxConsecutiveElement(arr, number):

    # intitialize count
    count = 0

    # initialize max
    result = 0

    for i in range(0, number):

        # Reset count when 0 is found
        if (arr[i] == 0):
            count = 0

        # If 1 is found, increment count
        # and update result if count
        # becomes more.
        else:

            # increase count
            count += 1
            result = max(result, count)

    return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='This program finds the maximum occurences of a number in an array')

    parser.add_argument('--length', type=int, help='Define length of array')

    args = parser.parse_args()

    # Accept the input numbers as list.
    inp_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[
        :args.length]

    # Convert above list to array using numpy
    out_array = np.asarray(inp_list)

    print('The entered array : ', out_array)
	#out_array = [1 , 0, 1 , 1]
	result = getMaxConsecutiveElement(out_array, len(out_array))
 

	print("The number of occurences of  are : ", result)
