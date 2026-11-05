# List & Tuples in python

#List = can store value of any dataType.Denoted by [] . Lists are mutable and ordered

languages = ["SQL","Python","Java",True,10.23,True] #creating a list using []
empty_list =[]

#Accessing the list
print(languages[3])
print(len(languages))
print(languages[-1])
print(languages[0:4])

numbers = [10, 20, 30, 40]
numbers[0:2] = [100, 200]
print(numbers)
# [100, 200, 30, 40]

# Remember these slicing patterns
# Syntax	Meaning
# list[:3]	First 3 elements
# list[-2:]	Last 2 elements
# list[::-1]	Reverse the entire list
# list[1:4]	Elements at indices 1, 2 and 3

#changing/updating an item in the list
languages[2] = None
print(languages)

#Adding elements in a list (append(),extend(),insert())
languages.append("Rahul") #append() = adds one item or element at the very end of the list
languages.append(["Trisha"])
languages.append([1,2])
print(languages)
#Invalid = languages.append("Rahul","Mou")

languages.extend([3,4]) #extend() = iterates over the list and adds each elements or items
print(languages)

languages.insert(2,"C++") #insert(index,value/item/elements)
print(languages) #insert() adds a new element in the respective index not replace it

#Removing elements in a list(remove(value/item/element),pop(),clear())
languages.remove("C++")
print(languages)

languages.pop() #pop() = Removes element from the end
print(languages)

#Counting and Searching (count(), index(value,start,stop))
print(languages.count(True)) #count() = No.Of occurences
print(languages.index(3)) #showing me the index position of 3
print(languages.index(True, 4, 6)) #element to be searched,searching beginning index,serching ending index

#Rearranging and Copying(reverse(),sort(),copy())
lang = ["Java", "Python", "SQL"]
print(lang.reverse()) #reverses the list

new_lang = lang.copy() #creates a shallow copy of the list
print(new_lang)

numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

names = ["Ravi", "A", "Karthik"]
names.sort(key=len)
print(names) # ['A', 'Ravi', 'Karthik']
names.sort(reverse=True)
print(names) # ['Ravi', 'Karthik', 'A']

#Tuples = Unlike lists,tuples are immutable but ordered.It has only two methods,i.e,count() and index().It is denoted by ()

t =() #Empty tuple
tup = (1,) #If we want to add only a single element then need to give a coma
print(type(t))

nums = (10,20,10,40,60,80)
print(nums.count(10))
print(nums.index(40))






