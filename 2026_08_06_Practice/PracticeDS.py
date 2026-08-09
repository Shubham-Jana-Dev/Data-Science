# e, *a = 2,3,45,66,43,6,3
# print(e,"\n",*a)
# 
# def my_function(*a):
# 	print(a)
# #my_function(55,4,66,3,67,8,32)
# def my_second(ss,**kwargs):
# 	print(ss,kwargs)
# #my_second(33,s = 34,r=5,e=4,"Shubham"==45,"ee"=="p")
# print(len(a))
# 
# print(a[3])

# Calculate the avarage score of an arbitery?
def practice_set():
	set1 = {1,2,3,4,5}
	set2 = {4,5,6,7,8,6,5,5}
	set3 = {6,8}
	print(set1.union(set2))
	print(set1.intersection(set2))
	print(set1.symmetric_difference(set2))
	set1.discard(1)
	print(set1)
	set1.remove(2)
	print(set1)
	print(set1.difference(set2))
	print(set2.difference(set1))
	print(set3.issubset(set2))
	print(set1.issubset(set2))
	set1.update(set3)
	print(set1)
	set3.update(set2)
	print(set3)
	set3.clear()
	print(set3)
	print(max(set2))
	import statistics as st
	print(st.mean(list(set2)))
	print(st.mode(list(set2)))
#practice_set();

def practice_list():
	my_list = [1,2,3,4,5,6,7]
	temp = 0
	k = len(my_list) -1
	for j in range(0,len(my_list)//2):
		temp = my_list[k]
		my_list[k] = my_list[j]
		my_list[j] = temp
		k -= 1
	print(my_list)
	reverse_list = []
	for j in range(len(my_list)-1,-1,-1):
		reverse_list.append(my_list[j])
	print(reverse_list)
	list1 = [34,55,66,33,74,90,86]
	list2 = [893,443,653,877,901]
	list2.extend(list1)
	print(list2)
#practice_list()

def two_sum():
	the_list = [13,2,3,47,5,6,7,8,9,5,75634,77,44,8]
	the_result = []
	target = 17
	the_list.sort()
	start = 0
	end = len(the_list) - 1
	while(end>start):
		if((the_list[start] + the_list[end]) > target):
			end -= 1
		elif((the_list[start] + the_list[end]) < target):
			start += 1
		else:
			the_result.append(the_list[start])
			the_result.append(the_list[end])
			break
	print(the_result)
#two_sum()

def practice_dictionary():
	the_dis = {"Shubham":34,"Sujit":44,"Mrinal":56,"Raj":89}
	print(the_dis.keys())
	print(the_dis.values())
	print(the_dis.items())
	the_second = {"Rahul":76,"Fanibhushan":30,"Kiran":20,"Hrishikesh":12}
	the_dis.update(the_second)
	print(the_dis)
	the_dis.pop("Raj")
	print(the_dis)
	the_dis.popitem()
	print(the_dis)
	the_dis.popitem()
	print(the_dis)
	the_dis.popitem()
	print(the_dis)
	the_dis.clear()
	print(the_dis)


#practice_dictionary()
#igggfff

class parent:
	def __init__(self,name):
		self.name = name
class child(parent):
	def __init__(self,age,name):
		self.age = age
		super(). __init__(name)
		print("Name: ",self.name,"\n","Age: ",self.age)


c1 = child(19,"Shubham")





def dont_use_print():
	return "See I hav'nt use the print()."
dont_use_print()
	
	
	
	
	
	
	
	
	