string = "RamanqeroitergjAAEElfOdkIjvoa"
str1 = " "
str2 = " "
for i in range(1,len(string)):
    if (i%2 == 0):
        str1 = str1 + string[i]
    
    else:
        str2 = str2 + string[i]


upo = str1.upper()
# nn = str2.lower()
print(upo,'\n',str2)

v = "aeiou"
vao = " "
con = " "
for i in range(0,len(str2)):
    if (str2[i] in v.upper() or str2[i] in v):
        vao = vao + str2[i]
    else:
        con = con + str2[i]
print(vao,"\n", con)