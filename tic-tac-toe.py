import numpy as np
n = 1  

print ("Welcome to the TicTacToe Game Check of \"Jumai B\"!")

O = 'O'    # player O
X = 'X'    # player X
tlist = [ [ [O,O,O],   # Game 1     		# tlist [ 0 ] to get this game
               [O,O,O],            # tlist is like a 3-dimensional array or list 
               [O,O,O] ] ,
            [ [X,X,X],    # Game 2     		# tlist [ 1 ] to get this game
              [X,X,X], 
              [X,X,X] ] , 
           [ [X,O,X],    # Game 3      		# tlist [ 2 ] to get this game
             [X,X,O], 
             [X,O,O] ] ,          
          [ [X,O,O],     # Game 4      		# tlist [ 3 ] to get this game
            [O,X,O], 
            [X,X,O] ] ,
          [ [X,O,X],     # Game 5      		# tlist [ 4 ] to get this game
            [O,X,O], 
            [X,O,O] ] ,          
          [ [O,X,O],    # Game 6   # It is a tie.   # tlist [ 5 ] to get this game
            [X,O,X],
            [X,O,X] ]  ]

def show(listt):
  for i in listt:
    print(*i, sep = " ")
def checkwin(listtt):
  count = 0
  for p in [X, O]:
    winrow1( listtt, p, count )
    winrow2( listtt, p, count )
    winrow3( listtt, p, count )
    wincol1( listtt, p, count )
    wincol2( listtt, p, count )
    wincol3( listtt, p, count )
    windia1( listtt, p, count )
    windia2( listtt, p, count )

    
def winrow1( t, p, count ):  # show whether row1 wins for player p: 'X' or 'O'
     r = 0   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[r][0]==t[r][1] and t[r][1]==t[r][2] and t[r][2]==p:
       print(p," won by row 1")   # True | False # end of winrow1( )
       count += 1
    
def winrow2( t, p, count ):  # show whether row1 wins for player p: 'X' or 'O'
     r = 1   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[r][0]==t[r][1] and t[r][1]==t[r][2] and t[r][2]==p:
       print(p," won by row 2")   # True | False # end of winrow1( )
       count += 1
def winrow3( t, p, count ):  # show whether row1 wins for player p: 'X' or 'O'
     r = 2   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[r][0]==t[r][1] and t[r][1]==t[r][2] and t[r][2]==p:
       print(p," won by row 3")   # True | False # end of winrow1( )
       count += 1
def wincol1( t, p, count ):  # show whether col1 wins for player p: 'X' or 'O'
     c = 0   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[0][c]==t[1][c] and t[1][c]==t[2][c] and t[2][c]==p:
       print(p," won by column 1")   # True | False # end of winrow1( )
       count += 1
def wincol2( t, p, count ):  # show whether col2 wins for player p: 'X' or 'O'
     c = 1   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[0][1]==t[1][c] and t[1][c]==t[2][c] and t[2][c]==p:
       print(p," won by column 2")   # True | False # end of winrow1( )
       count += 1
def wincol3( t, p, count ):  # show whether col3 wins for player p: 'X' or 'O'
     c = 2   # for board row 1      # p can be ‘X’ or ‘O’  ,  t is the 3x3 game board
     if t[0][c]==t[1][c] and t[1][c]==t[2][c] and t[2][c]==p:
       print(p," won by column 3")   # True | False # end of winrow1( )
       count += 1
def windia1( t, p, count ):  # show whether diagonal1 wins for player p: 'X' or 'O'
     if t[0][0]==t[1][1] and t[1][1]==t[2][2] and t[2][2]==p:
        print(p," won by diagonal 1") # end of windia2( )  
        count += 1

def windia2( t, p, count ):  # show whether diagonal2 wins for player p: 'X' or 'O'
     if t[0][2]==t[1][1] and t[1][1]==t[2][0] and t[2][0]==p:
        print(p," won by diagonal 2")    # end of windia2( )  
        count += 1


for i in range(1, 6+1):  # 6 games to check one by one: i = 1 2 3 4 5 6 
     print(n,"=========================================================.") 
     n+=1
     print("GAME", i ," is as follows:")
     show( tlist[i-1] )      # to show 3x3 game board: index = 0 1 2 3 4 5 in tlist[ index ] 
     checkwin( tlist[i-1] )  # to check all 8 winning situations for both X and O players


G = [ [X,X,X], [X,X,X], [X,X,X] ]   # G is a game board of 3x3
c = 7

while True:
    print(n,"=========================================================.") 
    n+=1
    S = input("Please enter your game board (* to exit)>")
    
    if S == '*':
        print(n,"=========================================================.") 
        n+=1
        print("Thank you for playing the TicTacToe Game Check of Jumai B!")
        break
    elif type(S) == str:
        for s in S:
          stri = list(S)
        for i in range(len(stri)):
            for j in range(len(G)):
              G = stri  
        G = np.reshape(G, (3, 3))
        
        
        print("GAME", c, "is as follows:")
        show(G)
        checkwin(G)
        c += 1

          
        
    else:
        break
print(n,"=========================================================.") 
n+=1       