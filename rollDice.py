'''The simple impletation of rolling a dice. User will randomly enter the number. The output will be the winning result of the participant and 
   the amount of money left in account.'''


# import library to use random.randint( )
import random   

# line number for each separator line in sequence
n = 1  
print ("Welcome to the Rolling 2 Dice Game")  
print(n,"=========================================================.")
n+=1

# you have 100 dollars to start.
yourMoney = 100     

# dealer also has 100 dollars to start.
dealerMoney = 100   
print( "Now, you have ", yourMoney, "dollars to play the game. Dealer also has ", dealerMoney, " dollars.")

# convert to integer for bet
bet = int(input("Enter your bet to roll 2 dice for this complete game (enter 0 to quit): "))  

if bet == 0 :
   # to stop this game and exit immediately
   exit( ) 

# keep running forever until break is encountered.
while True:  
   # dealer rolls the dice twice to get 2 numbers 
   dealer = random.randint(1, 6) + random.randint(1, 6)  

   # you roll the dice twice to get another 2 numbers 
   you = random.randint(1, 6) + random.randint(1, 6) 
   print(n,"=========================================================.")
   n=n+1 
   print("Roll 2 dice twice: Dealer got ", dealer , ", and you got ", you , "." )

  
   if dealer > you:   
       # You lost.
       
       #dealerMoney will be increased by the bet.
       dealerMoney = dealerMoney + bet

       #yourMoney will be deducted by the bet.
       yourMoney = yourMoney - bet

       print("You lost. Now, you have", yourMoney, "dollars, and dealer has", dealerMoney, "dollars")
   elif you > dealer:  
       # You won.  
       #dealerMoney will be decreased by the bet.
       dealerMoney = dealerMoney - bet

       #yourMoney will be increased by the bet.
       yourMoney = yourMoney + bet
    
       print("You won. Now, you have", yourMoney, "dollars, and dealer has", dealerMoney, "dollars")
   else :      
       # you == dealer      
       #It is a tie.
       #Neither you nor dealer will earn or lose the bet.  
       print("It's a tie. Now, you have ", yourMoney, "dollars.")

   if dealerMoney <= 0 or yourMoney <= 0 :   
      # either side has no money to play
      # time to exit the while loop and stop this game now.  Game is really over. 
      break 
   # end of while True loop 

print(n,"=========================================================.")
n+=1

print("Game ends. You have ", yourMoney, " dollars, and dealer has ", dealerMoney, " dollars. ") 
print(n,"=========================================================.")
n+=1

print("Thank you for playing this Rolling 2 Dice Game of")     
print(n,"=========================================================.") 
n+=1
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit: ")