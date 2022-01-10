
# $ content split
# * title
# tm terminal
# td treads
# n note
# ! important
# alternative



#$ list comprehension
#* simple
from typing import ItemsView


temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# in one line
new_temps = [temp / 10 for temp in temps]    #td 1.def a temp and 2."for temp in temps" is a inline for loop 
print(new_temps)




#* with if conditional
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temp != -9999] 
print(new_temps)

#online ex.
txt = "h3110 23 cat 444.4 rabbit 11 2 dog"
x = [int(s) for s in txt.split() if s.isdigit()]
print(x)

#ex. def a func find all int
def get_nums(arr):
    new_arr = [item for item in arr if type(item) is int] 
    return new_arr
    
    


#* if-else conditional
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps ] 
print(new_temps)

#ex.
def get_num(arr):
    new_arr = [item if type(item) is int else 0 for item in arr] 
    return new_arr

#ex. add up all items 
temps = ['221', '234']
new_temps = sum([item if type(item) is int else int(item) for item in temps])
print(new_temps)

#ex. add up item itselves
temps = ['221', '234']
new_temps = [sum([int(c) for c in item]) for item in temps]
print(new_temps)






#$ More about func
#* with multiple arguments
len("abc")      #n test one arguments
isinstance("abc", str)     #n test two arguments

#help(len)
#help(isinstance)

#* make a def with multiple arguments
def area(a, b):
    return a * b

print(area(4, 5))         


#ex. two str
def lis(a, b):
    return str(a) + str(b)

print(lis("ap", "ple"))





#* default & non-default parameters and keyword & non-keyword arguments
def area(a, b=5):           
    return a * b

print(area(4, 5))               #n non-keyword arguments, do not have keyword attached = positional
                                #n because the communication between these 2 arguments to the function definition is based on position
print(area(a = 4, b = 5))       #n keyword arguments



def area(a, b = 6):          #n set b = 6 is default parameter and no need to specify the value of argument when call the function
    return a * b

print(area(a = 4))        #n could set another value to b


#! def area(a = 6, b):   #n default parameter cannot be before non-default parameters





#* arbitrary numbs of non-keyword arguments
len('hello')        #n len can only return 1 argument
isinstance(6, int)   #n isinstance can only return 2
print(3, 4, 5, 6, 7)  #n but print can return many


#! *args non-keyword
def mean(*args):            #n any variable name would work after asterisk   #!
    return args

print(mean(1, 3, 'a', 4))    #n return a tuple!



def mean(*args):            
    return sum(args) / len(args)

print(mean(1, 3, 4))    #n cannot have key word arguments here!



#ex. uppercase & sorted str
def ls(*args):
    arr = [item.upper() for item in args]
    return sorted(arr)

# 
def ls(*args):
    return sorted([item.upper() for item in args])   




#* arbitrary numbs of keyword arguments
#! **kwargs non-keyword
def mean(**kwargs):
    return kwargs

#print(mean(1,2,3))   #n error because this is about a function with an arbitrary num of keyword arguments only
print(mean(a = 1, b = 2, c = 3))    #! the name have to be named arguments 
                                    #n will get dic

#! Functions with an arbitrary number任意函数 of keyword arguments are more readily used than functions with an
#! arbitrary number of known keyword arguments such as a print function like I told you earlier where you
#! can just pass as many arguments without a keyword.





#$ file processing
#* reading the file
myfile = open("fruits.txt")             #n in the same directory
print(myfile.read())                    #n open the file
print(myfile.read())                    #n were expecting print out two times, however, nothing after the cursor(pomegranate) after the first execution of read


#* run two times
myfile = open("fruits.txt") 
content = myfile.read()

print(content)                          #n run 2 times now, because the read method execute only once
print(content) 


#* closing file
myfile = open("fruits.txt") 
content = myfile.read()
myfile.close()                          #n will still get the correct output
#myfile.read()                          #! but cannot read after close


#* better way to read & close
with open("fruits.txt") as myfile:      #n with content manager!
    content = myfile.read()

print(content)                          #n closing the file is not necessary here because the with context manager will apply the close method implicitly.
                                        #n So the file will be closed once these block ends.


#* specify the directory
#ex.with open("file/fruits.txt") as myfile: 
with open("the_basics/files/vegetables.txt", "w") as myfile:    #n "r" means reading, "w" means writing
    content = myfile.write("Tomato")                            #n the vegetables file can be created by executing

with open("the_basics/files/fruits.txt", "w") as myfile:        #n rewrite on the exist file
    myfile.write("Tomato\nCucumber\nOnion")                     #n write more line with "\n" 转行
    myfile.write("Garlic")                                      # can apply more than one method to the open file, but garlic will automatically after onion since no space or \n there. we can add \n at the end of the last line.



#ex. define a function that gets a single string character and a file path as parameters and returns the number of occurrences of that character in the file.
def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)




#* add two more lines
with open("the_basics/files/fruits.txt", "a+") as myfile:       #n cannot append contents to an exist file with "x", but "a"
    myfile.write("\nOkra")
    myfile.seek(0)                                              #! at last, we need this step to put the cursor at the zero postion(from last line to the beginning) once again so that it can read
    content = myfile.read()

print(content)                                                  #n but it is not readable, we need use "a+" to read write append at the same time


#ex. repeat the file
with open("data.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content) 