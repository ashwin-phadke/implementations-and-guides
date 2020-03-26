import math
import argparse
import numpy as np

def max_element_of_array(array, length_of_array):

    # Store maximum number in an array
    max_num = array[0]


    for i in range(0, length_of_array):
        if array[i] > max_num :
            max_num  = array[i]
    return max_num

if __name__ == "__main__":


    #Implement argparse to accept command line arguements to choose methods.
    parser = argparse.ArgumentParser(description='This program finds the maximum number from an array')

    # length_of_array = int(input('Enter length of array : '))
    # print(length_of_array)
    parser.add_argument('--length', type=int, help='Define length of array')
    args = parser.parse_args()
    inp_list = list(map(int,input("\nEnter the numbers : ").strip().split()))[:args.length] 
    out_array = np.asarray(inp_list)
    print('The entered array : ',out_array)

    max_out = max_element_of_array(out_array, args.length)
    print('Maximum number is : ', max_out)

    



    