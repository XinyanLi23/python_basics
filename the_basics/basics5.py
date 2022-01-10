
# $ content split
# * title
# tm terminal
# td treads
# n note
# ! important
# alternative



#$ Modules
#* builtin module
dir(str)              #n methods
dir(__builtins__)     #n builtin func

#while True:
    #with open("the_basics/files/vegetables.txt") as file:
        #print(file.read())                                     #td its a loop which run forever and the content printed out every split of a second 

#td use ctrl+c to interupt, so there is no built in func can do that. check built in modules
#td step 1 - import sys 
#td step 2 - sys.builtin_module_names
#td step 3 - dir(time)
#td step 4 - help(sleep)
#td step 5 - time.sleep(3)

#so let's try run the content every 10 seconds

def built_in_module():
    import time                                                    #! this is how to use module!
    while True:
        with open("the_basics/files/vegetables.txt") as file:
            print(file.read())
            time.sleep(10)
        break

# built_in_module()




#* standard modules
# keep executing the script even the file is not in the directory
import os
# sys.prefix                                     # td os is not a built in and we need to get a directory path. So this commande will show the directory
# open + copy the directory in terminal           #td shows the folder

dir(os)                                                 #n to see what available for the module
os.path.exists("the_basics/files/vegetables.txt")       #n to check if a file exists

def standard_module():
    import time            #n built in
    import os             #n not built in
    while True:
        if os.path.exists("the_basics/files/vegetables.txt"):
            with open("the_basics/files/vegetables.txt") as file:
                print(file.read())
        else:
            print("File does not exist.")
        time.sleep(10)
        break

# standard_module()


#* third-party modules - pandas
import time             #n built in
import os               #n standard lib 
import pandas           #n third-party lib 

#ex.
while True:
    if os.path.exists("./files/temps_today.csv"):
        data = pandas.read_csv("./files/temps_today.csv")     #n the data frame is being created
        print(data.mean()["st1"])                   #n the st1 column mean
    else:
        print("File does not exist.")
    time.sleep(10)
    break

