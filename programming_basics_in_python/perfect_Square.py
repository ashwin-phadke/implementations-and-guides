import math 
import argparse

def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
   
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0) , sr
  
# Driver code 
 
def perfectSquareSimple():

   # Initialize variable to iterate over to find perfect square
   ans = 0

   # Initialize a flag to flag if negative numbers are provided by user
   neg_flag = False

   x = int(input("Enter an integer: "))

   # Checking if input is negative as negative numbers cannot be perfect squares by definition. 
   if x < 0:
      neg_flag = True

   #Iterate squaring all possible values to find square root
   while ans**2 < x:
      ans = ans + 1

   # If square of the result of above iteration is equal to the number from user then the number
   # provided by the user is a perfect square.
   if ans**2 == x:
      print("Square root of", x, "is", ans)

   # Some numbers are not hence the condition for that
   else:
      print(x, "is not a perfect square")

   # if it was not then was it a negative number from user(check)
      if neg_flag:
          print("Just checking... did you mean", -x, "?")
   
   return x


   # #MITOCW 6.0001


if __name__ == "__main__":

   #Implement argparse to accept command line arguements to choose methods.
   parser = argparse.ArgumentParser(description='This program shows the two methods to check if a given number is perfect square')

   parser.add_argument('--method', type=str, help='Define method of finding out perfect square')
   # , default='simple'
   args = parser.parse_args()

   #Use simple method
   if args.method == 'simple' : 
      y = perfectSquareSimple()

   #Use math.sqrt() way   
   elif args.method == 'math' :
      x = int(input("Enter a value : "))
      if (isPerfectSquare(x)): 
         print("Yes", x, "Is a perfect square ") 
      else: 
         print("No") 
   
   #User did not define a method , display help string for information
   else:
      print('Enter a valid method to calculate perfect square. \n 1. Simple mathematical calculation (--method simple) \n 2. Using math.sqrt inbuilt function(--method math)')


   


  
