#
'''
//  SolvedProblems.py
//  
//
//  Created by Shubham Jana on 27/07/26.
//
'''

#Check if string is symmetrical or palindrome
def palindrome_or_symmetrical():
    my_string = input("Enter the string: ")
    if(my_string == my_string[::-1]):
        print(my_string,"is a palindrome.")
    if(my_string[:len(my_string)//2] == my_string[len(my_string)//2:]):
        print(my_string,"is a symmetrical string.")
#palindrome_or_symmetrical()

#Length of String
def length_of_string():
    my_string = input("Enter the string: ")
    print(len(my_string))
#length_of_string()

#Reverse words in a String
def rever_word():
    my_string = input("Enter the string: ")
    my_list = my_string.split(" ")
    for j in my_list:
        for i in range(len(j)-1,-1,-1):
            print(j[i],end="")
        print(end=" ")
#rever_word()

#Remove Letters From a Stringe
def remove_letters():
    my_string =input ("Enter the string: ")
    new_string = ""
    for k in my_string:
        if(k.isalpha()):
            continue
        else:
            new_string = new_string + k
    print(new_string)
#remove_letters()

#Avoid Spaces in string length
def avoid_spaces():
    my_string = input("Enter the string: ")
    new_string = ""
    for j in my_string:
        if(j != " "):
            new_string = new_string + j
    print(new_string)
#avoid_spaces()

# Print even-length words in string
def print_even_word():
     my_string = "Hellow my friends Rama"
     my_list = my_string.split(" ")
     for i in my_list:
         if(len(i)%2 == 0):
            print (i,end=" ")
#print_even_word()

#❌Uppercase Half String

#Capitalize first and last character of each word
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

#Check if string has a letter and number
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


#🔥Accept strings containing all vowels
def all_vowels():
    my_string = input("Enter the string: ")
    my_vowels = "AEIOU"
    current_vowels =""
    my_list = my_string.split(" ")
    current_vowels =""
    vowels_set = set()
    for j in my_list:
        current_vowels =""
        for k in j:
            if(k.upper() in my_vowels and k.upper() not in current_vowels):
                current_vowels += k.upper()
            if(len(my_vowels) == len(current_vowels)):
               vowels_set.add(j)
    for m in my_list:
        if m in vowels_set:
             print(m,end=" ")
#all_vowels()

#🔥Count number of matching characters in a pair of string
def count_matches():
    my_str1 = input("Enter the first string: ")
    my_str2 = input("Enter the second string: ")
    count = 0
    for j in my_str1:
        if j in my_str2:
            count += 1
    print(count)
#count_matches()

#Count number of vowels using sets
def count_vowels():
    my_string = input("Enter the string: ")
    the_vowels = "AEIOU"
    count = 0
    for i in my_string:
        if(i.upper() in the_vowels):
            count += 1
    print(count)
#count_vowels()

#Remove duplicates from a string
def remove_duplicate():
    my_string = input("Enter the string: ")
    my_blank = ""
    for i in my_string:
        if(i not in my_blank):
            my_blank = my_blank + i
    print(my_blank)
#remove_duplicate()

#Least Frequent Character
def least_frequent():
    My_string = input("Enter the string: ")
    counts = {}
    for char in my_string:
        counts[char] = counts.get(char, 0) + 1
    least_frequent = None
    min_count = float('inf')
    for char, count in counts.items():
        if count < min_count:
            min_count = count
            least_frequent = char
    print(f"Least frequent character: '{least_frequent}' (appears {min_count} time)")
#least_frequent()

#Maximum frequency character
def maximum_frequency():
    my_text = input("Enter the string: ")
    counts = {}
    for char in my_text:
        counts[char] = counts.get(char, 0) + 1
        max_frequent = None
    max_count = -1
    for char, count in counts.items():
        if count > max_count:
            max_count = count
            max_frequent = char
    print(f"Maximum frequency character: '{max_frequent}' (appears {max_count} times)")
#maximum_frequency()

#Odd Frequency Characters
def odd_frequecy():
    my_string = input("Enter teh string: ")
    counts = {}
    for char in my_string:
        counts[char] = counts.get(char, 0) + 1
    odd_chars = []
    for char, count in counts.items():
        if count % 2 != 0:
            odd_chars.append(char)
    print("Characters with odd frequencies:", odd_chars)
#odd_frequecy()

# Frequency of numbers
def frequency_of_numbers():
    my_string = input("Enter the string: ")
    count = 0
    for j in my_string:
        if(j.isdigit()):
            count += 1
    print(count)
#frequency_of_numbers()

# Specific Characters Frequency
def count_frequency_of_sepsific_charecter():
    My_string = input("Enter the string: ")
    target = input("Enter the targeted charecter: ")
    count = 0
    for j in My_string:
        if(j == target):
            count += 1
    print(count)
#count_frequency_of_sepsific_charecter()

#Check if a string contains any special character
def Special_charecter():
    My_string = input("Enter the string: ")
    flag = False
    for j in My_string:
        if(j.isdigit() == False and j.isalpha() == False):
            flag = True
    if(flag):
        print ("Special charecter present.")
    else:
        print("Special charecter does'nt present.")
#Special_charecter()

#❌Generating random strings until a given string is generated

#Find words which are greater than length k
def words_greater_then_length():
    My_string = input("Enter the string: ")
    target_length = int(input("Enter the target length: "))
    my_list = My_string.split(" ")
    for j in my_list:
        if(len(j) > target_length):
            print(j,end=" ")
#words_greater_then_length()

# For removing ith character from a string
def remove_charecter_from_ith_position():
    My_string = input("Enter the string: ")
    ith_position = int(input("Enter the ith position: "))
    new_string = ""
    for j in range(0,len(My_string)):
        if(j == ith_position):
            continue
        else:
            new_string = new_string + My_string[j]
    print(new_string)
#remove_charecter_from_ith_position()

# Split and join
def splitting_and_rejoining():
    My_string = input("Enter the String: ")
    splited_string = ""
    joined_string = ""
    for j in My_string:
        splited_string = splited_string +" "+ j
        
    for k in splited_string:
        if(k != " "):
            joined_string = joined_string + k
        else:
            continue
    print("Your Inputed String: ",My_string)
    print("After splitting the string: ",splited_string)
    print("After joining the String again: ",joined_string)
#splitting_and_rejoining()


#Check if a given string is binary string or not
def Binary_String():
    My_string = input("Enter the string: ")
    binary_string = "01"
    flag = True
    for l in My_string:
        if(l not in binary_string):
            flag = False
    if(flag):
        print(My_string," is a binary string. :)")
    else:
        print(My_string," is not a binary string. :(")
#Binary_String()

#Find all close matches of input string from a list
def closet_string():
    my_list = ["Shubham", "Jana", "Mango", "Banana", "Rain", "Train"]
    My_string = input("Enter the string: ")
    count = 0
    current_count = 0
    result_string = ""
    for j in my_list:
        for h in j:
            if (h in My_string):
                current_count += 1
                if(current_count > count):
                    count = current_count
                    result_string = j
        current_count =0
        count = 0
    print("The cloest mstch of",My_string,"is",result_string,".")
#closet_string()

#Find uncommon words from two Strings
def uncomon_word():
    My_string = input("Enter the first string: ")
    my_list = My_string.split(" ")
    second_second_string = input("Enter teh second second string: ")
    second_second_string_list = second_second_string.split(" ")
    for j in my_list:
        if(j not in second_second_string_list):
            print("the uncomon word:",j,end=" ")
    for k in second_second_string_list:
        if(k not in my_list):
            print("the uncomon word:",k,end=" ")
#uncomon_word()

#Swap commas and dots in a String
def Swap_commas_and_dots():
    My_string = input("Enter the string: ")
    result_string = ""
    for j in My_string:
        if(j == ','):
            result_string = result_string + '.'
        elif(j == '.'):
            result_string = result_string + ','
        else:
            result_string = result_string + j
    print(result_string)
#Swap_commas_and_dots()

#Permutation of a string using inbuilt function
import itertools
def Permutations_of_string():
    My_string = input("Enter the string: ")
    pa = [''.join(p) for p in itertools.permutations(My_string)]
    print(pa)
#Permutations_of_string()


#Check for URL in a String
def url_finding():
    My_string = input("Enter the stirng: ")
    if("www." in My_string and ".com" in My_string):
        print("There migth be an URL in",My_string)
    else:
        print("I am 100% sure there is no URL in ",My_string)
#url_finding()

#Execute a String of Code
def RunString():
    My_string = input("Enter the string: ")
    code = eval(My_string)
    print(code)
def RunString2():
    My_string = "print('Hellow World')"
    exec(My_string)
#RunString2()


#Print middle character of a String
def middle_char():
    My_string = input("Enter the stirng: ")
    print(My_string[(len(My_string)//2)])
#middle_char()

#onvert integer to string
def convert_to_str_from_int():
    My_int = int(input("Enter the integer: "))
    My_string = str(My_int)

    My_string = My_string + " Bro bilive me this is a string."
    print(My_string)
#convert_to_str_from_int()


#Convert String to Int
def convert_str_to_int():
    My_string = input("Enter the string: ")
    flag = True
    char = ""
    for j in My_string:
        if(j.isdigit() == False):
            char = char + j
            flag = False
    if(flag):
        print(int(My_string))
    else:
        print("Are you out of your mind? how could we can convert it integer while it has",char)
#convert_str_to_int()

#Split string into list of Characters
def split_str_into_char():
    My_string = input("Enter the string: ")
    my_list =[]
    for j in My_string:
        my_list.append(j)
    print(my_list)
#split_str_into_char()

#Convert a List to String
def Convert_list_to_string():
    my_list  = []
    My_string = ""
    size = int(input("Enter the size of the list: "))
    for i in range(0,size):
        element = input("Enter the element: ")
        my_list.append(element)
    for k in my_list:
        My_string = My_string + k
    print(My_string)
#Convert_list_to_string()

#Convert String to a list
def Convert_str_to_list():
    My_string = input("Enter the String: ")
    my_list = []
    for i in My_string:
        my_list.append(i)
    print(my_list)
#Convert_str_to_list()

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

def my_problem():
    my_string = "seedtautgiovxdk"
    my_vol = "AEIOU"
    my_blank = ""
    for j in my_string:
        if(j.upper() not in my_vol and j.upper() not in my_blank()):
            my_blank = my_blank + j
    print (my_blank)
#print(my_str)

# Remove Letters from a String
def remove_letters():
    my_string =input ("Enter the string: ")
    new_string = ""
    for k in my_string:
        if(k.isalpha()):
            continue
        else:
            new_string = new_string + k
    print(new_string)
#remove_letters()

# Convert a list of Characters into String
def list_of_char_to_str():
    my_str = ""
    size = int(input("Enter the size of the list: "))
    my_list = []
    for i in range(0,size):
        element = input ("Enter the character: ")
        my_list.append(element)
        
    for j in my_list:
        my_str = my_str + j
    print(my_str)
#list_of_char_to_str()

#Convert Object to String
def obj_to_str():
    i = [1, 2, 3]
    my_string = input("Enter the string : ")
    j = str(i) + my_string
    print(j)
#obj_to_str()

#Sort a list of strings
def sort_str():
    my_string = input("Enter the string : ")
    i = my_string.split()
    i.sort()
    print(i)
#sort_str()

#Convert tuple to string
def String_to_tupple():
    my_tupple = ('s','5','3','j','t')
    my_string = ""
    for i in my_tupple:
        my_string = my_string + i
    print(my_string)
#String_to_tupple()

#Check if String is Empty or not
def check_empty_string():
    my_string = "raj"
    if len(my_string)>0:
        print ("the string is not an Empty String ")
    else:
        print("The string is an Empty String")
    print (len(my_string))
#check_empty_string()
    
#Convert String to Set
def string_to_set():
    my_string = input("Enter the string: ")
    my_set = set()
    for j in my_string:
       my_set.add(j)
    print(my_set)
#string_to_set()

#Convert Set to String
def Set_to_string():
    size = int (input ("Enter the size of the set: "))
    my_set = set()
    for i in range (0,size):
        element = input("Enter the element: ")
        my_set.add(element)
    print (my_set)
#Generate possible valid IP addresses from given string

#Check and display vowels
def display_vowels():
    my_string = input("Enter the string: ")
    my_vowels = "AEIOU"
    for j in my_string:
        if(j.upper() in my_vowels):
            print(j,end=" ")
#display_vowels()

#📚Basic Practice Programs

#Repeat the Strings

#📚String Function

#Convert String to LowerCase
def str_to_low():
    my_string = "I AM SHUBHAM :)"
    my_string = my_string.lower()
    print (my_string)
#str_to_low()
    
#Reverse String
def reverse_Str():
    my_string = input ("Enter the string: ")
    rev_string = ""
    for i in range (len(my_string)-1,-1,-1):
        rev_string = rev_string + my_string[i]
    print (rev_string)
#reverse_Str()
    
#Check Palindrome
def check_Palindrome():
    my_string = input ("Enter the string: ")
    rev_string = ""
    for i in range (len(my_string)-1,-1,-1):
        rev_string = rev_string + my_string[i]
    if(my_string == rev_string):
        print (my_string," is a Palindrome string")
    else:
        print (my_string, " is  not Palindrome string")
#check_Palindrome()
     
#🤣Find Pattern

#Decimal number to binary number
def dec_to_bin():
    i = int(input("Enter the string : "))
    j = bin(i)[2:]
    print(j)
#dec_to_bin()

#Binary number to decimal number
def bin_to_dec():
    my_string = input("Enter the string : ")
    i = int(my_string, 2)
    print(i)
#bin_to_dec()

#Reverse Words
def reverse_words():
    my_string = input ("Enter the string: ")
    my_list = my_string.split(" ")
    for j in my_list:
        for i in range(len(j)-1,-1,-1):
           print(j[i],end="")
        print(end=" ")
#reverse_words()
        
#Palindrome String
def check_Palindrome():
    my_string = input ("Enter the string: ")
    rev_string = ""
    for i in range (len(my_string)-1,-1,-1):
        rev_string = rev_string + my_string[i]
    if(my_string == rev_string):
        print (my_string," is a Palindrome string")
    else:
        print (my_string, " is  not Palindrome string")
#check_Palindrome()

#Slice The String
def slice_the_string():
    my_string = input("Enter the string: ")
    print(my_string[:len(my_string)//2])
    print(my_string[len(my_string)//2:])
#slice_the_string()

#Change Case
def Swap_case():
    my_string = input("Enter the string: ")
    new_string = ""
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for j in my_string:
        if(j in lower_case):
            new_string = new_string + j.upper()
        else:
            new_string = new_string + j.lower()
    print(new_string)
#Swap_case()

#Print Alphabets
def print_alpha():
    my_string = input("Enter the string: ")
    for j in my_string:
        if(j.isalpha()):
            print (j,end=" ")
        else:
            continue
#print_alpha()
            
#🔥🔥🔥Advance String Programs

#Convert numeric words to numbers
def numaric_word_to_numbers():
    my_numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    my_string = input("Enter the string: ")
    my_list = my_string.split(" ")
    for k in my_list:
        for j in my_numbers:
            if(k.lower() == j):
                print (my_numbers[j],end="")
#numaric_word_to_numbers()

#Word location in String
def location_of_word():
    my_string = input("Enter the String: ")
    my_list = my_string.split(" ")
    target_word = input("Enter the targeted word: ")
    for j in range(0,len(my_list)):
        if (my_list[j].upper() == target_word.upper()):
            print(target_word," is the ",j,"th word in the string.")
#location_of_word()

#❌Consecutive characters frequency

#Rotate a string
def reotare_a_string():
    my_string = input("Enter the sting: ")
    new_string = my_string[1:] + my_string[:1]
    print(new_string)
#reotare_a_string()
    
#Check if a string can become empty by recursive deletion
def Say_a_big_NO():
    my_string = input("Enter the string: ")
    def delete_element(text):
        new_string = text.replace(text[0],"")
        if(len(new_string) > 0):
            delete_element(new_string)
        else:
            print("Brother the string is empty at least now let it go.")
            text = new_string
        print(text)
    delete_element(my_string)
    print(my_string)
#Say_a_big_NO()
    
#Minimum number of rotations to obtain a string
def rotation_of_string():
    my_string = input("Enter the string : ")
    i = len(my_string)
    for j in range(1, i + 1):
        if my_string[j:] + my_string[:j] == my_string:
            print(j)
            break
#rotation_of_string()

#Words Frequency in String Shorthands
def words_frequency():
    my_string = input("Enter the string: ")
    my_list = my_string.split(" ")
    my_word = {}
    for i in my_list:
        my_word[i] = my_word.get(i,0)+1
    print(my_word)
#words_frequency()

#Successive Characters Frequency
def successive_frequencyP():
    def successive_frequency(text: str):
        if not text:
            return []
        result = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result
    my_string = input("Enter the string: ")
    frequencies = successive_frequency(my_string)
    for char, count in frequencies:
        print(f"'{char}': {count}")
#successive_frequencyP()

#Sort String by K frequency

#Convert Snake case to Pascal case
def Snake_to_Pascal_case():
    my_string = "this_is_my_string_i_am_Shubham_Jana_i_am_from_kolkata"
    my_list = my_string.split("_")
    for i in my_list:
        print(i.capitalize(),end='')
#Snake_to_Pascal_case()

#Avoid Last occurrence of delimitter
def remove_last_delimitter():
    my_string = input("Enter the string: ")
    delimeter = input("Enter the delimitter")
    my_list = my_string.split(delimeter)
    my_list2 = []
    for k in range(0,len(my_list)-1):
        my_list2.append(my_list[k])
    my_list2[len(my_list2)-1] = my_list2[len(my_list2)-1] + my_list[len(my_list)-1]
    for k in my_list2:
        if(k != my_list2[len(my_list2)-1]):
            print(k,end=delimeter)
        else:
            print(k,end=" ")
#remove_last_delimitter()

#Character position of Kth word
my_string = input("Enter the string: ")
kth_pos = int(input("Enter the value of the posithon of the word: ")) - 1
my_list = my_string.split(" ")
count = 0
for k in range(0,len(my_list)-1):
    if (k != kth_pos):
        for j in my_list[k]:
            count += 1
    else:
        break
count = count + k
print("The",kth_pos+1,"word is",my_list[kth_pos],"and its first's charecter index in the string is: ",count)
#Right and Left Shift characters

#Exceptional Split

#Split String on vowels
def split_on_vowels():
    my_string = input("Enter the string: ")
    my_vol = "AEIOU"
    for j in my_string:
        if(j.upper() in my_vol):
            print(end=" ")
        else:
            print(j,end="")
#split_on_vowels()

#Mirror Image of String
def mirror_string():
    my_string = input("Enter the string: ")
    rev_string = ""
    for j in my_string:
        rev_string = j + rev_string
    mirror_image = my_string + rev_string
    print(mirror_image)
#mirror_string()

#Replace multiple words with K
def repalce_multiple_words_K():
    my_string = input("Enter the string: ")
    my_list = my_string.split(" ")
    my_list2 = []
    for j in my_list:
        if(j not in my_list2):
            my_list2.append(j)
        else:
            my_list2.append("K")
    for m in my_list2:
        print(m,end=" ")
#repalce_multiple_words_K()

#Replace Different characters in String at Once
#Multiple indices Replace

#Remove multiple empty spaces
def remove_extar_spaces():
    my_string = "My   Name is  Shubham Jana.  I am 19 years   old."
    my_list = my_string.split(" ")
    for j in my_list:
        if(j != ''):
            print(j,end=" ")
#remove_extar_spaces()

#Remove punctuation
#Similar characters Strings comparison

#Remove K length Duplicates
def remove_k_length_duplicate():
    my_string = input("Enter the string: ")
    my_length = int(input("Enter the length: "))
    my_list = my_string.split(" ")
    my_empty = []
    for h in my_list:
        if(h not in my_empty):
            my_empty.append(h)
        elif(len(h) == my_length):
            continue
        else:
            my_empty.append(h)
    for k in my_empty:
        print(k,end=" ")
#remove_k_length_duplicate()

#Remove suffix
def remove_suffix():
    my_string = input("Enter the string: ")
    my_suffs = ""
    my_list = [""]
    for j in my_string:
        my_suffs = my_suffs + j
        my_list.append(my_suffs)
    for k in range(len(my_list)-1,-1,-1):
        print(my_list[k])
#remove_suffix()

#Find all duplicate characters
def dupliacate_characters():
    my_string = input("Enter the string: ").upper()
    my_set = set()
    blank_string = ""
    for j in my_string:
        if(j in blank_string):
            my_set.add(j)
        else:
            blank_string += j
    print(my_set)
#dupliacate_characters()

# Replace duplicate Occurrence
def replace_duplicate_occurrences():
    my_string = input("Enter the string: ")
    replacement = input("Enter replacement character for duplicates (default '*'): ") or "*"
    seen = set()
    result = []
    for char in my_string:
        if char in seen:
            result.append(replacement)
        else:
            seen.add(char)
            result.append(char)
    final_string = "".join(result)
    print("Result:", final_string)
#replace_duplicate_occurrences()

#Convert string to dictionary

#Check if two strings are Rotationally Equivalent

#Test if string is subset of another
def check_subset():
    my_string = input("Enter the string: ")
    target = input("Enter the string: ")
    if(target in my_string):
        print(target,"is a subset of ",my_string)
    else:
        print(target,"is not a subset of ",my_string)
#check_subset()

#Generate Random binary string
#Convert binary to string
#Reverse Sort a String

#Remove special characters
def remove_special_charecter():
    my_string = input ("Enter the string: ")
    new_string = ""
    for j in my_string:
        if(j.isalpha() or j.isdigit()):
            new_string = new_string + j
        else:
            continue
    print(new_string)
#remove_special_charecter()

#Check validity of a Password
def check_password_validity():
    password = input("Enter the password to validate: ")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False
    special_characters = "!@#$%^&*()-_+=[]{}|;:',.<>?/`~"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        elif char.isspace():
            has_space = True
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not has_upper:
        errors.append("Password must contain at least one uppercase letter.")
    if not has_lower:
        errors.append("Password must contain at least one lowercase letter.")
    if not has_digit:
        errors.append("Password must contain at least one number.")
    if not has_special:
        errors.append("Password must contain at least one special character.")
    if has_space:
        errors.append("Password must not contain spaces.")

    if not errors:
        print(f"'{password}' is a VALID password. :)")
    else:
        print(f"'{password}' is an INVALID password. :(")
        for error in errors:
            print(f" - {error}")
# check_password_validity()

# Add padding
def add_padding():
    my_string = input("Enter the string: ")
    length = int(input("Enter desired total length: "))
    pad_char = input("Enter padding character (default '*'): ") or '*'
    if len(pad_char) > 1:
        pad_char = pad_char[0]
    print("\n--- Padding Results ---")
    print("Left Padded:  ", my_string.rjust(length, pad_char))
    print("Right Padded: ", my_string.ljust(length, pad_char))
    print("Center Padded:", my_string.center(length, pad_char))
    print("Zero Padded:  ", my_string.zfill(length))
#add_padding()

#Print Superscript and Subscript

#Convert binary to String
def bin_to_string():
    binary_str = input("Enter the binary string (space-separated 8-bit blocks): ")
    binary_values = binary_str.split(" ")
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    result_string = "".join(ascii_characters)
    print("Decoded String:", result_string)
# bin_to_string()

#Check if a string is pangram
#Sort a list
#Convert Image to String and vice-versa

#Iter Over words of a String
def iter_over_words():
    my_string = input("Enter the string: ")
    my_list = my_string.split(" ")
    for j in my_list:
        for k in j:
            print(k,end="")
        print("\n")
#iter_over_words()

#Convert case of elements in a list of Strings
def Convert_case_of_element():
    my_string = "I am Shubham Jana"
    my_list = my_string.split(" ")
    for j in my_list:
        print(j.swapcase(),end=" ")
#Convert_case_of_element()

#Sort list of dates given as Strings
#Pad or fill a string by a variable using f-string
#Convert string to DateTime and vice-versa
#Index and Slice Strings
#Split string in groups of n consecutive characters

#📚Programs on SubString

#Check if a Substring is Present
def check_sub_string_present():
    my_string = input("Enter the string: ")
    target_substring = input("Enter the targeted substring: ")
    if (target_substring in my_string):
        print(target_substring,"is present in the string.")
    else:
        print(target_substring,"is not present in the string.")
#check_sub_string_present()

#Substring presence
def substring_presence():
    my_string = input("Enter the string: ")
    target_substring = input("Enter the targeted substring: ")
    if (target_substring in my_string):
        print(target_substring,"is present in the string.")
    else:
        print(target_substring,"is not present in the string.")
#substring_presence()

#Substrings Frequency
#Maximum Consecutive Substring Occurrence
#Maximum occurring Substring
#Possible Substring count

#Replace all occurrences of a substring
def replace_all_substring():
    my_string = input("Enter the stinrg: ") or "abbefjwefwjsdiabbitntigsdwkeiabbouyw"
    targeted_substring = input("Enter the targted Substring: ") or "abb"
    blank_string = ""
    my_list = my_string.split(targeted_substring or "abb")
    for h in my_list:
        blank_string += h
    print(blank_string)
#replace_all_substring()

#Longest Substring Length of K
#Extract Indices of substring matches
#Split by repeating substring

#Remove substring list
def remove_substring():
    my_string = input("Enter the stinrg: ") or "abbefjwefwjsdiabbitntigsdwkeiabbouyw"
    targeted_substring = input("Enter the targted Substring: ") or "abb"
    blank_string = ""
    my_list = my_string.split(targeted_substring or "abb")
    for h in my_list:
        blank_string += h
    print(blank_string)
#remove_substring()

#Remove after substring
def remobe_after_substring():
    my_string = input("Enter the stinrg: ") or "efjwefwjsdiabbitntigsdwkeiabbouyw"
    targeted_substring = input("Enter the targted Substring: ") or "abb"
    blank_string = ""
    my_list = my_string.split(targeted_substring or "abb")
    blank_string = my_list[0] + targeted_substring
    print(blank_string)
#remove_after_substring()

#Remove Redundant Substrings
#Test substring order

#String till Substring
def string_till_substring():
    my_string = input("Enter the stinrg: ") or "efjwefwjsdiabbitntigsdwkeiabbouyw"
    targeted_substring = input("Enter the targted Substring: ") or "abb"
    blank_string = ""
    my_list = my_string.split(targeted_substring or "abb")
    blank_string = my_list[0] + targeted_substring
    print(blank_string)
#string_till_substring()

#Filter Strings combination of K substrings
