#Write a Python program to check if a given number is a Fibonacci number using the if condition
n=int(input('enter a number: '))
a,b,c=0,1,0
while c<n:
    c=a+b
    a,b=b,c
if c==n:
    print('yes')
else:
    print('no')