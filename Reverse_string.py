word=list(input("Enter a word: "))
reverse=[]
for i in range(0,len(word)):
    reverse.append(word.pop())
print("".join(reverse)) 
