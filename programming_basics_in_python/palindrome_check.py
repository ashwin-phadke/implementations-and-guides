#function to check whether the number is palindrome or not
def check_palindrome():
    #get input from user 
    inp_num = input("Enter Number to check palindrome or not : ")

    #check the entire number by reversing it in the list.
    if inp_num[::] == inp_num[::-1]:

    #if the reversed number matches original it is palinrome
        print("Voila! It is palindrome")
        
    #else not
    else:
        print("Well, why not try again")

#just a welcome
print("Hello World")

#execute the function
check_palindrome()




