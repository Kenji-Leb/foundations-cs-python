# FCS CYCLE 46
# Assignment 3
# Due Date: July 22nd, 10am
# Name: Abbas kanj
# ---------------------------
def main():
    displaymenu()
    while (True):
            try: 
                choice = int(input("Please select one of the options: "))
            except:
                print("Invalid Choice...")
                continue
            if (choice == 1):
                sumTuples()
                continue
            elif (choice == 2):
                exportJson
            elif (choice == 3):
                importJson
            elif (choice == 4):
                print("Thanks for using my program!, Exiting...")
                exit()
            else:
                continue
#----------------------------------------------------------
def displaymenu():
    print("1- Sum Tuples\n" + "2- Export JSON\n" + "3- Import JSON\n" + "4- Exit\n")
#----------------------------------------------------------
def sumTuples():   
    while(True):
        try:
            input_str = (input("Enter a tuple of numbers (comma-separated): "))
            input_str2 = (input("Enter a tuple of numbers (comma-separated): "))
            input_list = input_str.split(",")
            input_list2 = input_str2.split(",")
            tuple_elements = [int(num) for num in input_list]
            tuple_elements2 = [int(num2) for num2 in input_list2]
            tuples1 = tuple(tuple_elements)
            tuples2 = tuple(tuple_elements2)
            def sumTupless(tuples1,tuples2):
                tup=[]
                for i in range(0,len(tuples1)):
                    tup.append(tuples1[i]+tuples2[i])
                result =tuple(tup)
                print("Updated tuple: ",result)
                print("-----------------------")
            sumTupless(tuples1,tuples2)
            break
        except:
            print("Invalid input!, please try again")
            continue
    displaymenu()
#----------------------------------------------------------
def exportJson():
    print
#----------------------------------------------------------
def importJson():
    print
#----------------------------------------------------------
main()