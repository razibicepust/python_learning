row= int(input("Enter row:"))
m= 1
while m <= row:
    k= row
    while k>=m:
        print("*", end="")
        k= k-1
    print("")
    m= m+1