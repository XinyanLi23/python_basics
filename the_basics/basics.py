# 主题
# * 系列主题
# tm terminal
# td treads
# n note
# $ important
# ! content split


# n syntax error is 句法错误
# n use {python3 basics.py} to excute in terminal (it does not save the lines automatically)

# n {python3} can use terminal as calculator when no file is opened
# n >>> is interactive shell and could not run the code
# n >>> exit() is exits the interactive shell





# basic
day_hours = 24
week_days = 7

week_hours = day_hours * week_days
print(week_hours)




# int str & float
x = 10      #int
y = 10      #str "10"
z = 10.1     #float

sum1 = x + x
sum2 = x + y

print(sum1, sum2)
print(type(x), type(y), type(z))




#! section 3 data types
#* list[]: mutable, means can add more values in
student_grades = [9.1, 8.8, 7.5]
#n student_grades.append(3.5)


#* ranges
list(range(1,10))      #[1-9]
list(range(1,10,2))    #[1,3,5,7,9]


#* attributes
#n "dir" is a function in Python that will give you all the things you can do with a specific type.
#tm dir(list)  #n all are attributes of a list 都是list的属性
#tm dir(float)
#tm dir(str)
#tm help(str.upper) #use help to check the documentation for the upper method, then use "q" to quit.
#tm myword = "hello"
#tm myword.title()




# dir(__builtins__) to find the built in features in Python
student_grades = [9.1, 8.8, 7.5]
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum/length
print(mean)




#$ Learning python is about learning 3 things: syntax, proper data structure for particular scenario, and algorithms.

#n ex
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
num_greater = student_grades.count(10.0)
print(num_greater)

username = "Python3"
lowercase = username.lower()
print(lowercase)




# dictionary{}: identity attached to items
monday_temperature = [9.1, 8.8, 7.5]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.value())     #n dir(dict), dir(dict.values)
length = len(student_grades)            #n use student_grades.keys() to get names
mean = mysum/length
print(mean)




# tuple(): immutable, means cannot add more values in (append or remove does not work for tuple)
monday_temperature = (1, 4, 5)
print(monday_temperature)





# lists
#n use "clear" to empty command line & "ctrl + l" to console. use "exit()" to come back to terminal in console.

monday_temperature = [9.1, 8.8, 7.5]
monday_temperature.append(8.1)        #n add 8.1 to the list
monday_temperature.clear()            #n clear the list 
monday_temperature.index(8.8)         #n check the index of specific num
#$ monday_temperature.__getitem__(1) & monday_temperature[1] will get the same result as index
monday_temperature.index(8.8, 3)      #n check the index of specific num from the third
monday_temperature.remove(8.8)        #n remove 8.8 from the list
monday_temperature.pop()              #n remove the last item
monday_temperature.reverse()
monday_temperature.insert(2,"apple")



#* list slice
monday_temperature = [9.1, 8.8, 7.5, 6.6, 9.9]
len(monday_temperature)
monday_temperature[3]                #n call the 4th item
monday_temperature[1:4]              #n call the index of 1, 2, 3 item (index 4 not included, the upper limit is never included in the slice)
monday_temperature[0:2] = monday_temperature[:2]             #td same results
monday_temperature[3:5] = monday_temperature[3:]


#* list negative slice
monday_temperature[-1] = monday_temperature[4]
monday_temperature[3:] = monday_temperature[-2:]    
monday_temperature[-4:-2]


#* string slice
mystring = 'hello'
mystring[1]
mystring[2:4]
monday_temperature = ['hello', 1, 2, 3]
monday_temperature[0][2]                    #n the index 2 of the index 0 is 'l' 




# dictionary
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
student_grades["Sim"]
eng_port = {"rain":"chuva", "sun":"sol"}
eng_port["sun"]

