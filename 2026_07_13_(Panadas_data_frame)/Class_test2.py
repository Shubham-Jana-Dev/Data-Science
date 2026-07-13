String = "ABCDEFGH"
myString = list(String)
max = len(myString)-1
temp = " "

j = 0
for i in range(len(myString)-1,-1,-1):
    temp = temp + myString[i]

print(temp)

al1 = " "
al2 = " "
j = 0
for i in range(len(temp)-1,0,-2):
    al2 = al2 + temp[i]
for j in range(0,len(temp)):
    if(temp[j] in al2):
        continue
    else:
        al1 = al1 + temp[j]
print(al1,"\n",al2)