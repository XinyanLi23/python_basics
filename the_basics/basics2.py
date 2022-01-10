
# $ content split
# * title
# tm terminal
# td treads
# n note
# ! important
# alternative


#$ section 5 create functions

#* return
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean                          #n return "None" if no return
                                             #td it runs halfway with "print(the_mean)". Since after printing the results, it still looks for the return, and shows "None" if there no return afterwards.
print(mean([1, 4, 6]))
#print(type(mean),type(sum))



#* print
def mean(mylist):
    print("Function started!")              #n we can still use print for information
    the_mean = sum(mylist) / len(mylist)
    return the_mean                         #$ ALWAYS use RETURN in functions

mymean = mean([0, 3, 4])
print(mymean + 10)



#* conditional
def mean(mylist):                            #n only used for list, not for dictionary
    the_mean = sum(mylist) / len(mylist)
    return the_mean 

#student_grade = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}     #n does not work
#print(mean(student_grade))



#* set for conditional
def mean(value):
    #if type(value) == dict:                              #* if true = isinstance
    if isinstance(value, dict):                           #td ex."type(3) == int" = "isinstance(3, int)"
        the_mean = sum(value.values()) / len(value)
    else:                            
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
print(mean(monday_temperatures))

student_grade = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}   
print(mean(student_grade))


# ex.
def foo(string):
    if len(string) < 8:
        return False
    else:
        return True

print(foo("mypass"))



#* elif
x = 3
y = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal than y")
else:
    print("x is less than y")



#* white space (one or more)
if 3 > 1:          #n always one white space between operators
    print('b')     #n indentation (4 white spaces)


# ex.
def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature > 15 & temperature < 25:
        return "Warm"
    else:
        return "Cold"





#$ section 6 create functions

#* user input
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

#print(weather_condition(7))
user_input = float(input("Enter temperature:"))      #n prompting the user to enter a value
print(weather_condition(user_input))                 #td "input" function freezes the execution of a program and waits for the user input one the command line
#user_input = input("Enter some input:")             #n use "input" only will get a string, so need to add "float" or "int" before
#print(type(user_input), user_input)                 #n help to check the type



#* string formatting
user_input = input("Enter your name: ")
message = "Hello %s!" % user_input                   #td "%s" is a special string, use "%" instead of "," and then the value of variable will replace the %s
#message = f"Hello {user_input}"                     #n only used after python3.6



#* with multiple variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s %s" % (name, surname)                     #td need more "%s" for more strings to input
message = f"Hello {name} {surname}, what's up {when}"         #n as same as line above
print(message)

#def A():                                    #n use for only run the block A
#if __name__ == '__main__':
    #A()

#ex.
def foo(name):
    message = "Hi %s" % (name.capitalize())      #n uppercase
    return message