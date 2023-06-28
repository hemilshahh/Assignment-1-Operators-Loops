number=(1, 2, 3, 4, 5, 6, 7, 8, 9) 
evenCount=0
oddCount=0
for i in number:
  if i%2==0:
    evenCount+=1
  else:
    oddCount+=1

print("Number of even numbers : ",evenCount, "\nNumber of odd numbers : ",oddCount,)