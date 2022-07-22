n = 1
print("Welcome to the List Sorting/Searching Game of Jumai B!")
def selSort(Lyst):
    for i in range(len(Lyst)):
        min_ele = i
        for j in range(i+1, len(Lyst)):
            if Lyst[min_ele] > Lyst[j]:
                min_ele = j
    # Swap the found minimum element with
    # the first element       
        Lyst[i], Lyst[min_ele] = Lyst[min_ele], Lyst[i]


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

while True:
    Lyst = []
    total = 0
    ave = 0
    print(n,"=========================================================.") 
    n+=1
    num = int(input("Please enter how many integers you would like to play (up to 20, 0 to stop)> "))
    if num == 0:
        print(n,"=========================================================.") 
        n+=1
        print("Thank you for playing this List Sorting/Searching Game of Jumai B")
        break
    elif num < 0:
        continue
    else:
        for i in range(1, num+1):
            n = int(input("Please enter number> "))
            Lyst.append(n)
            selSort(Lyst)
        for i in range(len(Lyst)):
                total = total + Lyst[i]
                ave = total // len(Lyst)
        print ("Your", num, "integers in ascending order are:", Lyst, sep = ' ')
        print("Sum is", total, ", and average is ", ave)
    print(n,"=========================================================.") 
    n+=1
    while True:
        
        number = int(input("Please enter a number to search (-99 to end the search)> "))
        if number == -99:
            break
        else:        
            result = binary_search(Lyst, 0, len(Lyst)-1, number)
            if result != -1:
                print("The number",number, "is found at the position", str(result + 1))
            else:
                print("The number", number, "is not found.")
    