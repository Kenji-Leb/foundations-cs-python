# FCS CYCLE 46
# Assignment 2
# Due Date: July 15, 10am
# Name: Abbas kanj
# ---------------------------
def main():
    displaymenu()
    choice = int(input("Please select one of the options: "))
    while (choice != 4):
        try:
            if (choice == 1):
                num = int(input("Enter a number: "))
                print(countDigits(num))
            elif (choice == 2):
                numbers = findMax()
                if numbers:
                    max_num = numbers[0]
                    for num in numbers[1:]:
                        if num > max_num:
                            max_num = num
                    print("Maximum number is: ", max_num)
                else:
                    print("No numbers entered.")
            elif (choice == 3):
                countTags()
        except:
            print("This is an invalid option")
#----------------------------------------------------------
def displaymenu():
    print("1- Count Digits\n" + "2- Find Max\n" + "3- Count Tags\n" + "4- Exit\n")
#----------------------------------------------------------
def countDigits(num):
    
    if num == 0:
      return 0
    else:
      return 1 + countDigits(num // 10)
#----------------------------------------------------------
def findMax():
    num1 = input("Enter your number(s) here (press enter to exit): ")
    if num1 == "":
        return []
    return [int(num1)] + findMax()
#----------------------------------------------------------
def countTags(html, tag):
    start_tag = "<" + tag
    end_tag = "</" + tag + ">"
    count = 0

    start_index = html.find(start_tag)

    while start_index != -1:
        end_index = html.find(end_tag, start_index)
        if end_index == -1:
            break

        count += 1
        start_index = html.find(start_tag, end_index + len(end_tag))

    return count
#----------------------------------------------------------
main()