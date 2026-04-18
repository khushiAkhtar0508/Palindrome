#WAP TO CHECK THE NUMBER IS PALINDROME OR NOT
n=242
num=n
result=0

while num>0:
    largestdigit=num%10
    result=(result*10)+largestdigit
            #0+4
    num = num//10
if num ==result:
        print("121 is a palindrome")
else:
            print("121 is not a palindrome")
            
    
