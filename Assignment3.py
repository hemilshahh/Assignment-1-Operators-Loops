#1
a=[8, 2, 3, 0, 7]
def sum(a):
    add=0
    for i in a:
        add=add+i
    return add
print(sum(a))

#2
str=list(input("Enter a word: "))
def reverse(str):
    reversed=[]
    for i in range(0,len(str)):
        reversed.append(str.pop())
    return "".join(reversed)
print(reverse(str))

#3
str=input("Enter a word: ")
def calc(str):
    ucase=0
    lcase=0
    str=str.replace(" ", "")
    for i in str:
        if i.isupper()==True:
            ucase+=1
        else:
            lcase+=1
    return ucase, lcase
print(calc(str))