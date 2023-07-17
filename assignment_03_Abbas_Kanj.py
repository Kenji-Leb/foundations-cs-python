# # FCS CYCLE 46
# # Assignment 3
# # Due Date: July 22nd, 10am
# # Name: Abbas kanj
# # ---------------------------
# import json

# def main():
#     displaymenu()
#     while (True):
#             try: 
#                 choice = int(input("Please select one of the options: "))
#             except:
#                 print("Invalid Choice...")
#                 continue
#             if (choice == 1):
#                 sumTuples()
#                 continue
#             elif (choice == 2):
#                 exportJson()
#             elif (choice == 3):
#                 importJson()
#             elif (choice == 4):
#                 print("Thanks for using my program!, Exiting...")
#                 exit()
#             else:
#                 continue
# #----------------------------------------------------------
# def displaymenu():
#     print("1- Sum Tuples\n" + "2- Export JSON\n" + "3- Import JSON\n" + "4- Exit\n")
#     print("----------------------------")
# #----------------------------------------------------------
# def sumTuples():   
#     while(True):
#         try:
#             input_str = (input("Enter the first tuple(comma-separated, i.e: 1,2,3): "))
#             input_str2 = (input("Enter the second tuple: "))
#             input_list = input_str.split(",")
#             input_list2 = input_str2.split(",")
#             tuple_elements = [int(num) for num in input_list]
#             tuple_elements2 = [int(num2) for num2 in input_list2]
#             tuples1 = tuple(tuple_elements)
#             tuples2 = tuple(tuple_elements2)
#             tup=[]

#             for i in range(0,len(tuples1)):
#                 tup.append(tuples1[i]+tuples2[i])
#             result =tuple(tup)

#             print("Updated tuple: ",result)
#             print("-----------------------")
#             break
        
#         except:
#             print("Invalid input!, please try again")
#             continue
        
#     displaymenu()
# #----------------------------------------------------------
# def exportJson():
#     while (True):
#         try:
#             filname = input("Enter a filename(ends with .json): ")
#             num_inputs = int(input("Enter the number of key(s) and value(s): "))
#             my_dict = {}

#             for i in range(num_inputs):
#                 # .format() allows you to format strings by inserting values into predefined placeholders within the string
#                 key = input("Enter key {}: ".format(i + 1))
#                 value = input("Enter value {}: ".format(i + 1))
#                 my_dict[key] = value

#             print("Filename: ", filname)
#             print("Dictionary:", my_dict)
#             print("----------------------------")

#             with open(filname,'w') as file:
#                 json.dump(my_dict, file)
#             break

#         except:
#             print("Invalid input!, please try again")
#             continue

#     displaymenu()
# #----------------------------------------------------------
# def importJson():
#     while (True):
#         try:
#             filname1 = input("Enter a filename(ends with .json): ")
#             with open(filname1, 'r') as file:
#                 json_data = json.load(file)

#             dictionary_list = []
#             for item in json_data:
#                 dictionary_list.append(dict(item))
                
#             print(dictionary_list)
#             print("----------------------------")
#             break

#         except:
#             print("Invalid input!, please try again")
#             continue

#     displaymenu()
# #----------------------------------------------------------
# main()