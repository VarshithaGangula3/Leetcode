# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def pwd_check(pwd):
    res="Invalid"
    upper_count=0
    num_count=0
    if len(pwd)==10:
        if len(pwd)==len(set(pwd)):
            if pwd.isalnum():
                for i in pwd:
                    if i.isupper():
                        upper_count+=1
                    if i.isnumeric():
                        num_count+=1
                if upper_count>=2:
                    if num_count>=3:
                        res="Valid"
    return(res)

n=int(input())
for i in range(n):
    result = pwd_check(input().strip()) 
    print(result) 
                    
                
            
        
