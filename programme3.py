N = int(input("enter the limit N:")) # input
arry = [] # blank arrat
if ( N > 0 ):
 i = 0 #initialising  required variables 
 x = 1
 f = 1
 for g in range(N) :
  if ( x <= N ) :
   arry.insert(i,x) 
   x = arry[i] + pow(2,f)    
   i = i + 1
   f = f + 1
else:
  print("0")  
s = 0
for j in range(0, len(arry)):    
   s = s + arry[j]
print(arry)
print(s)  
