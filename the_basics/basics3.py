
# $ content split
# * title
# tm terminal
# td treads
# n note
# ! important
# alternative




#$ section 7 Loops

#* for loops
monday_temperatures = [9.1, 8.8, 7.6]

#print(round(monday_temperatures[0]))
#print(round(monday_temperatures[1]))
#print(round(monday_temperatures[2]))

for temperature in monday_temperatures:     #n for loop creates a variable(temperature) and it goes all items one by one
    print(round(temperature))
    print("Done")

for letter in 'hello':
    print(letter.title())          #n title() makes a string with each word is titlecased


#ex.
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for item in colors:
    if isinstance(item, int):
        print(item)



#* loop through a dictionary
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)


#ex1.
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))


#ex2.
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for numbers in phone_numbers.values():
    print(numbers.replace("+", "00"))




#* while loops
a = 3

#while a > 0:      #n as long as the line is true, print 1 
#    print(1)      #n ctrl c to exit the execute 

#while True:
#    print(1)

#ex.
username = ''

while username != "pypy":
    username = input("Enter username: ")      #n the input continues to ask until inputs the true username



#* while loops with break and continue
while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue




#$ Application
#try by myself
conclusion = ""
while True:
    say_something = input("Say something: ")
    if say_something == '\end':
        break 
    else:
        conclusion = conclusion + say_something
        continue

print(conclusion)




#$ build the maker func
#def sentence_maker(phrase):
    #capitalized = phrase.capitalize()
    #if phrase.startswith(("how","what","why")) 

# better 
def sentence_maker(phrase):
    interrogatives = ("how","what","why")     #n 疑问词
    capitalized = phrase.capitalize()
    if phrase.startswith((interrogatives)):
        return "{}?".format(capitalized)         #n return the string "{}" 
    else:
        return "{}.".format(capitalized)

print(sentence_maker("how are you"))




#$ constructing the loop 
#! ex 
def sentence_maker(phrase):
    interrogatives = ("how","what","why")     
    capitalized = phrase.capitalize()
    if phrase.startswith((interrogatives)):
        return "{}?".format(capitalized)         
    else:
        return "{}.".format(capitalized)


results = []                                # td3 store phrases that the user enters in a list, so we start with an empty list outside the loop and the python will execute the func definition
while True:                                 # td1 conditional loop - while
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:                                            # td2 sentences look like many items - lists
        #results.append(user_input)                  # td4 need to convert the string to the func, so add the def in
        results.append(sentence_maker(user_input))

print(" ".join(results))             # td5 use ".join" to join the sentences togethere 

# steps:
# 1. def a function
# 2. then iterate, make a loop, ask user for input in each iteration, immediately check each input first!
# 3. store the output of the census maker in to the results list
# 4. concatenate the items of the list and print!