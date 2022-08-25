#Write a python script to print first 10 multiples of N

n=int(input('Enter N Value : '))
i=1

while i<11:
    print(n,'*',i,':',n*i)
    i+=1