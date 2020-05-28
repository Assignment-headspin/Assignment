arry = [] #array to hold the values
for x in range (1,1000):  # giving the range for calculation
  if ( x % 4 == 0 ) or ( x % 5 == 0 ) : # checking the values which are divisile by  4 or 5
   i = 0
   arry.insert(i,x) # inserting the diviible values to the array 
   i = i + 1
sum = 0
for j in range(0, len(arry)):  #looping to add the elements inside the array  
   sum = sum + arry[j]
print(arry)
print("Sum : " + str(sum))
