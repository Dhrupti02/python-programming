import numpy as np

print("Welcome to play the Sudoku Game Check of Jumai B!")
S1 = [[1,2,3,4,5,6,7,8,9],
[2,3,4,5,6,7,8,9,1],
[3,4,5,6,7,8,9,1,2],
[4,5,6,7,8,9,1,2,3],
[5,6,7,8,9,1,2,3,4],
[6,7,8,9,1,2,3,4,5],
[7,8,9,1,2,3,4,5,6],
[8,9,1,2,3,4,5,6,7],
[9,1,2,3,4,5,6,7,8]]

S2 = [[1,2,3,4,5,6,7,8,2],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[2,3,4,5,6,7,8,9,1],
[5,6,7,8,9,1,2,3,4],
[8,9,1,2,3,4,5,6,7],
[3,4,5,6,7,8,9,1,2],
[6,7,8,9,1,2,3,4,5],
[9,1,2,3,4,5,6,7,8]]

S3 = [[1,2,3,4,5,6,7,8,2],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[2,3,4,5,6,7,8,9,1],
[5,6,7,8,9,1,2,3,4],
[8,9,1,2,3,4,5,6,7],
[3,4,5,6,7,8,9,1,2],
[6,7,8,9,1,2,3,4,5],
[9,1,2,3,4,5,6,7,8]]

S4 = [[1,2,3,4,5,6,7,8,9],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[2,3,4,5,6,7,8,9,1],
[5,6,7,8,9,1,2,3,4],
[8,9,1,2,3,4,5,6,7],
[3,4,5,6,7,8,9,1,2],
[6,7,8,9,1,8,3,4,5],
[9,1,2,3,4,5,6,7,8]]

boxsize = 3

def RowOK(S, r):  # check Row r in S board is OK or not
    goodlist = [1,2,3,4,5,6,7,8,9]   # a perfect list of 1 thru 9 sorted order
    slist = S[r] 
    #print(slist)    # get row r, which can be 0, 1, …, or 8
    clist = [ ]        # We must make a real copy of the original source list to avoid changing it here.
    for element in slist:
        clist.append(element)   # make a real copy to avoid side effect to the original 9x9 array
    clist.sort( )    # sort the list before comparing with goodlist
    return (clist == goodlist)    # true means OK for row r in S since they are equal
    # end of RowOK( )
def ColumnOK(S, c):  # check Row r in S board is OK or not
    goodlist = [1,2,3,4,5,6,7,8,9]
    S = np.array(S)
    column = S.T
    slist = column[c]
    clist = []
    for ele in slist:
        clist.append(ele)
    clist.sort()
    return (clist == goodlist)

def SquareOK(S):
    countBad = 0
    mats_3x3x9 = [S[3*i:3*i+3] for i in range(3)]
    mats_9x3x3 = [
    [row_1x9[3*i:3*i+3] for row_1x9 in rows_3x9]
    for i in range(3)
    for rows_3x9 in mats_3x3x9]
    
    for mat_3x3 in mats_9x3x3:
        if not sorted([i for row in mat_3x3 for i in row]) == list(range(1,10)):
                    idx = mats_9x3x3.index(mat_3x3)
                    print("Square ", idx+1, " has a problem.")
                    countBad += 1
    return True    

def showGame(S):
    for i in S:
        print(*i, sep = " ")

def checkGame(S):   # check game board S for 9 rows, 9 columns, 9 squares
    countBad = 0   # count how many problems being detected 
    for r in range(9):  # 9 rows check with r = 0 to 8
        if (not RowOK(S, r) ):     # r = 0 to 8 from computer’s view
            print("Row ", r + 1 , " has a problem.")               # Row 1 to 9 from user’s view
            countBad += 1   # increment countBad by 1
          
    for c in range(9):  
            if (not ColumnOK(S, c )):  
             print("Column ", c + 1 , " has a problem.")#  9 columns check: 0 to 8, actually they mean column 1 to 9 for user.
             countBad += 1
    #for q in range(9):  
     #       if (not SquareOK(S, q )):  
      #       print("Square ", q + 1 , " has a problem.")#  9 columns check: 0 to 8, actually they mean column 1 to 9 for user.
       #      countBad += 1
    SquareOK(S)
    if countBad == 0:  # perfect game since nothing is bad 
        print("Congratulations! You won the game.")


n = 1  # line number for each separation line for readability
print( )
print(n,"=============================================================");n=n+1;
print("Your game 1 is as follows: " )
showGame(S1)   # to print 9x9 game board
print( )
print("Your game 1: ")  # show the check result
checkGame(S1)  # to check 9 rows/columns/squares. Total 27 checkings. 
print( )
print(n,"=============================================================");n=n+1;
print( )

print("Your game 2 is as follows: " )
showGame(S2)   # to print 9x9 game board
print( )
print("Your game 2: ")  # show the check result
checkGame(S2)  # to check 9 rows/columns/squares. Total 27 checkings. 
print( )
print(n,"=============================================================");n=n+1;

print( )

print("Your game 3 is as follows: " )
showGame(S3)   # to print 9x9 game board
print( )
print("Your game 3: ")  # show the check result
checkGame(S3)  # to check 9 rows/columns/squares. Total 27 checkings. 
print( )
print(n,"=============================================================");n=n+1;

print( )

print("Your game 4 is as follows: " )
showGame(S4)   # to print 9x9 game board
print( )
print("Your game 4: ")  # show the check result
checkGame(S4)  # to check 9 rows/columns/squares. Total 27 checkings. 
print( )
print(n,"=============================================================");n=n+1;

print("Thank you for playing this Sudoku Game Check of Jumai B!")
print(n,"=============================================================")