''' the game is about password validation. If the entered password is not missing some regular expressions, the program will notify each 
    missing expressions. '''


# line number for each separator line
from asyncio.windows_events import NULL


n = 1    

print ("Welcome to the PASSWORD game")  
print (n,"============================================================")
n+=1

# pw is a string
pw = input( "Please enter a password (Enter q to quit): ") 

# q is to quit the game and exit this loop
while (pw != "q") :  
   # password is quoted for clarity
   print (n,"============================================================") 
   n+=1
   print("The password you just entered is \"" +  pw + "\"") 

   # count # of problems
   badcount = 0    

   # count # of digits      
   countdigits = 0       

   # count # of 6 special symbols $ % @ ! ? *
   countsymbols = 0  
   
   # count # of lower-case letters
   countlower = 0      

   # count # of upper-case letters 
   countupper = 0    

   # count # of 4-digit years 2020 2019 2018 2017
   countyears = 0    

   # Counting 26 lower case letters:
   countlower += pw.count('a')+pw.count('b')+pw.count('c')+pw.count('d')+pw.count('e')+pw.count('f')+pw.count('g') 
   countlower += pw.count('h')+pw.count('i')+pw.count('j')+pw.count('k')+pw.count('l')+pw.count('m')+pw.count('n') 
   countlower += pw.count('o')+pw.count('p')+pw.count('q')+pw.count('r')+pw.count('s')+pw.count('t')+pw.count('u')
   countlower += pw.count('v')+pw.count('w')+pw.count('x')+pw.count('y')+pw.count('z')

   # Counting 26 upper case letters:   
   countupper += pw.count('A')+pw.count('B')+pw.count('C')+pw.count('D')+pw.count('E')+pw.count('F')+pw.count('G') 
   countupper += pw.count('H')+pw.count('I')+pw.count('J')+pw.count('K')+pw.count('L')+pw.count('M')+pw.count('N') 
   countupper += pw.count('O')+pw.count('P')+pw.count('Q')+pw.count('R')+pw.count('S')+pw.count('T')+pw.count('U')
   countupper += pw.count('V')+pw.count('W')+pw.count('X')+pw.count('Y')+pw.count('Z')

   

   if countupper < 2:    
      print("R1: Your password is not secure since it has less than 2 upper-case letters.")
      badcount += 1  

   if countlower < 2:     
      print("R2: Your password is not secure since it has less than 2 lower-case letters.")
      badcount += 1

   if len(pw) < 7:     
      print ("R3: Your password is not secure since it has less than 7 characters.")
      badcount += 1

   # Counting 10 digits in password
   countdigits += pw.count('0')+pw.count('1')+pw.count('2')+pw.count('3')+pw.count('4') 
   countdigits += pw.count('5')+pw.count('6')+pw.count('7')+pw.count('8')+pw.count('9') 

   if countdigits < 2:     
      print( "R4: Your password is not secure since it has less than 2 digits.")
      badcount += 1

   if len(pw) > 12:        
      print ("R5: Your password is not secure since it has more than 12 characters.")
      badcount += 1

   # space character ' ' check
   if pw.count(' ') > 0 :         
      print( "R6: Your password is not secure since it contains space.")
      badcount += 1

   # isdigit( ) will check whether pw contains only digits.
   if pw.isdigit( ) :    
      print( "R7: Your password is not secure since it contains only digits. ")
      badcount += 1

   # isalpha( ) will check whether pw contains only alphabets.
   if pw.isalpha( ) : 
      print( "R8: Your password is not secure since it contains only alphabets. ")
      badcount += 1

   # Counting 6 special symbols:
   countsymbols += pw.count('$')+pw.count('%')+pw.count('@')+pw.count('!')+pw.count('?')+pw.count('*')
   if countsymbols == 0:       
      print( "R9: Your password is not secure since it contains none of 6 special symbols: $ % @ ! ? *")
      badcount += 1   

   # Counting 4 special years:
   countyears += pw.count('2020')+pw.count('2019')+pw.count('2018')+pw.count('2017') 
   if countyears != 0:     
      print("R10: Your password is not secure since it contains 2020, 2019, 2018, or 2017.")
      badcount += 1   

   # Final check of badcount to see whether password is very secure:
   if badcount == NULL:   
      print( "Congratulations! Your password is very secure!")
   else :
      print( "Your password has the above ", badcount, " problems to be fixed." )
   pw = input( "Please enter a password (Enter q to quit): ")
   
   # end of while loop 

print (n,"============================================================")
n+=1
print("Thank you for playing this PASSWORD game")   
print (n,"============================================================")
n+=1
