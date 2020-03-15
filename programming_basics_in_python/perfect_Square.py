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


#MITOCW 6.0001