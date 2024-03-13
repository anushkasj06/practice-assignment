n = int(input("enter the number to want check"))
ifyes =0
for i in range(1,n+1):
    if(i*i == n):
        ifyes=+1
if(ifyes==1):
    print("This is perfect square number")
else:
    print("This is not a perfect square number")