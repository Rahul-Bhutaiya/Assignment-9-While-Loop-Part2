#Write a python script to print first N odd natural numbers in reverse order

n=int(input('Enter N Value : '))
i=1

while i<=n:
    print(n*2-1)
    n-=1