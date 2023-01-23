import  sympy
cnt=0
for  i  in   range(10000,100000):
    j=str(i)
    k=j[::-1]  #check  palindrome
    if  j==k  and  sympy.isprime(i)==True: #check   prime  by  sympy.isprime()
        print(i) #print out  5 digit  palindrome primes
        cnt=cnt+1
print(cnt)  #print out  the  number  of  5 digit palindrome primes     
