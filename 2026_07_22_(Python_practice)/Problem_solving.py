#
'''
//  Problem_solving.py
//  
//
//  Created by Shubham Jana on 23/07/26.
//
'''

def print_even_word():
     my_string = "Hellow my friends Rama"
     my_list = my_string.split(" ")
     for i in my_list:
         if(len(i)%2 == 0):
            print (i,end=" ")
#print_even_word()

def capitalize_last_first_char():
    my_string = "Hellow my school friends"
    my_list = my_string.split(" ");
    for i in my_list:
        for j in range(0,len(i)):
            if(j==0 or j==len(i)-1):
                print(i[j].upper(),end="")
            else:
                print(i[j],end ="")
        print(end=" ")
#capitalize_last_first_char()


def check_char():
    letter = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"

    my_string = "₹=÷^&[]^##"
    flag =  False
    for j in my_string:
        if((j in letter) or (j in numbers)):
            flag = True
        
    if(flag):
        print ("letter and number both are present in the string")
    else:
        print("Ether letter or numbers are absent in the string")
#check_char()

def remove_vowels():
    my_string = "seedtautgiovxdk"
    my_vol = "AEIOU"
    my_blank = ""
    for j in my_string:
        if(j.upper() not in my_vol and j.upper() not in my_blank):
            my_blank = my_blank + j
    print (my_blank)

my_string = "wwskjhiuvnkjuvhwkalkhliuhlkz"
My_set = set()
min_count = 10000000
current_count = 0
min_element = 'j'
for j in my_string:
    My_set.add(j)
print(My_set)
for i in My_set:
    current_count = 0
    for k in my_string:
        if(k == i):
            current_count += 1
            if(current_count < min_count):
                min_count = current_count
                min_element = i
print(min_element)