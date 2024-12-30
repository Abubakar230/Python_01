from intro import bakar

bakar("Abubakar")


#               Strings

# strip == used to remove space
# split(", ") == used to remove ,===>convert string into list
# (", ".join(my_list)) ===>convert list into string
# replace(1,2)
# find()
# count
# order.format(1,1) ===> this is used to enter value in {}
# len() used to find length
# for letter in variable_string:
# ... space print(letter) ===> then show all charcters one by one in each line 
# variable = "he said, \"good\" " ===> used for nested quotation
# r"c:/lenovo/D"

#               List(array)

# Append ===> Add value in last of the list
# Insert(1,"Value_add_in_list") ===> Add value in the list in any index as you want
# Pop ===> Remove value in last of the list
# Remove ===> Remove value in the list in any index as you want
# for Variable_Declaration_name in Variable_already_declared_List: ===>for loop
# if element_of_list in Variable_already_declared_List:
#               print("Ok success")
# .copy() ===> is used to add new reference in memory
# [x**2 for x in range(10)]===> print===> [0,1,4,9,16,25,36,49,64,81]

#               Dictionary

# In this we will also define manually key/index name
# .get() ===> used to access the dictionary
# dictionary_variable_name = { "key1" : "abc", "key2" : "def", "key3" : "hij" }
# dictionary_variable_name["key3"] = "xyz" ===> Used to push
# for variable_declaration_name in dictionary_variable_name 
#                  ===> print(variable_declaration_name)===> then show only keys
# for variable_declaration_name in dictionary_variable_name 
#                  ===> print(variable_declaration_name, dictionary_variable_name[variable_declaration_name])===> also show keys and values
# for key,value in dictionary_variable_name.items():
#                  ===> print(key,value)        ===>aslo same result as previous
# if "key_name" in dictionary_variable_name:
#                  ===> print("We found this key")
# print(len(dictionary_variable_name)) ===> 3
# dictionary_variable_name["key4"] : "hjk"     ===> add new value/key in dictionary
# del("key3") ===> remove specific key
# pop("key3") ===> Also remove specific key
# popitem() ===> remove last element in dictionary
# .copy()  ===> used to copy address in memory
# .clear()  ===> {}
# keys = ["1", "2", "3"]
# value = "Accurate"
# dict_var = dict.fromkeys(keys, value)  ===> show the result like {"1":"Accurate","2":"Accurate","3":"Accurate"}

#                Tuple
# ("a","b","c") ===> like the list but use small braces
#               ===> Unlike list it is Muteable
#               ===> Can't overload because the result is permanent store in memory