'''An addition game in python. In this, the program will ask for two numbers and their addition.'''


def testAdd(num1, num2, num3) :   

    # 10 points for each game to win or lose
    points = 10    

    # get 3 numbers from the user as input 
    sum = int(input("Please enter the sum of these 3 numbers: " ) )  

    # is sum really correct? Must use int() to convert str to integer 
    if sum == ( int(num1)+int(num2)+int(num3) ) :  

       print("Congratulations! Correct answer! You have earned " + str(points) + "points.") 

       # add points to total for win, list[0] is a global variable 
       list[0] += points     

    # incorrect answer from the user 
    else :  

      print("Sorry, it is not correct! You lost " + str(points) + " points." ) 

      # deduct points from total for loss, list[0] is a global variable   
      list[0] -= points   

   # end of testAdd( ) function ; Indentation controls the begin and end of a function 

# MAIN PROGRAM :   Python does not have main( ) to start the main program. 

# variable to track total number of points for the player 
total_points = 0          

# one-element list to make list[0] a global variable for all functions to update in Python   
list = [total_points]    

print ("Welcome to the Super Numbering game!!") 

# get user’s full name to make this game user-friendly 
your_name = input("Please enter your full name: ")   

print ( your_name + ": Thank you for playing this number game. You have " + str(list[0]) + " points to start. ") 

# Forever loop to keep running until the user says "no" 
while True:     

   # string num1 
   num1 = input("Enter the first number: ")       

   # string num2
   num2 = input("Enter the second number: ")    

   # string num3 
   num3 = input("Enter the third number: ")      

   # show three numbers in strings to the user 
   print ("You just entered 3 numbers: ", num1, num2, num3)   

   # call function testAdd(  ) to check and give award or penalty  
   testAdd(num1, num2, num3)    

   # show the current count of points  
   print("Now, you have " + str(list[0]) + " points in your account!" )   

   # get player's input for continuation 
   play_again = input("Would you like to continue this game? 'yes' or 'no': ")  

   # only "no" will stop this game
   if play_again == "no" :   
      # to leave this while loop and exit the game
      print("Thank you for playing this wonderful game!!!")
      break
   
   # end of while True loop ; Indentation controls the end of while loop 