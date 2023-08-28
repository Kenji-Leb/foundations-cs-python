# FCS CYCLE 46
# Midterm Solution
# Due Date: August 1st, 11:59 PM
# Name: Abbas kanj
# ---------------------------
# Used links:
# https://www.w3schools.com/python/default.asp
# https://docs.python.org/3/library/re.html
# https://www.programiz.com/python-programming/datetime
#-----------------------------------------------------------
import re
import sys
from datetime import datetime

def check_line(line):
    try:
        ticket_id, event_id, username, date, prio = line.strip().split(", ")
        if re.match(r'^tick\d{3}$', ticket_id) and \
           re.match(r'^ev\d{3}$', event_id) and \
           re.match(r'[a-zA-Z]', username) and \
           re.match(r'^\d{8}$', date) and \
           re.match(r'^\d{1,4}$', prio) and \
           len(prio) <= 3:
            return True
        else:
            return False
    except ValueError:
        #ValueError is raised when a function receives an argument of the correct type but an inappropriate value.
        return False

updated_text_file = []
checking_lines = set() 

with open(r"tickets.txt") as file:
    for line in file:
        if line not in checking_lines:  
            if check_line(line):
                updated_text_file.append(line.strip())
            checking_lines.add(line)  
#---------------------------------------------------------------------------
def main():
    print("Welcome to my program :)")
    while (True):
            try: 
                displaymenu()
                choice = int(input())
            except:
                print("Invalid Input....")
                continue
            if (choice == 1):
                tries = 0
                max_tries = 5
                while tries != 5:
                    for tries in range(max_tries):
                        password = input("Enter your password: ")
                        if password == 'admin123123':
                            while (True):
                                print("---------------------------")
                                print("Tickets:\n" +"----------")
                                for line in updated_text_file:
                                    print(line)
                                print("---------------------------")
                                try:
                                    display_admin_menu()
                                    choice_admin = int(input())
                                except:
                                    print("Invalid Input...")
                                    continue
                                if (choice_admin == 1):
                                    display_statistics(updated_text_file)
                                    event_id, ticket_count = display_statistics(updated_text_file)
                                    print(f"Event ID with the highest number of tickets: {event_id} (Ticket Count: {ticket_count})")
                                    continue
                                elif (choice_admin == 2):
                                    book_ticket()
                                elif (choice_admin == 3):
                                    display_all_tickets(updated_text_file)
                                elif (choice_admin == 4):
                                    change_tickets_prio()
                                elif (choice_admin == 5):
                                    disable_ticket(updated_text_file)
                                elif (choice_admin == 6):
                                    run_events()
                                elif (choice_admin == 7):
                                    print("Thanks for using my program.\n" + "Exiting...")
                                    sys.exit()
                        else:
                            tries += 1
                            print("Incorrect passowrd. Please try again:")
                            continue
                else:
                    print("Account locked, max tries exceeded.\n Exiting...")
                    sys.exit()
            elif (choice == 2):
                while True:
                    try:
                        display_guest_menu()
                        choice_guest = int(input())
                        if (choice_guest == 1):
                            book_ticket()
                        elif (choice_guest == 2):
                            print("Thanks for using my program.\n" + "Exiting...")
                            sys.exit()
                    except ValueError:
                        print("Invalid input.")
                        continue
            elif (choice == 3):
                print("Thanks for using my program!, Exiting...")
                sys.exit()
#----------------------------------------------------------
def displaymenu():
    print("\nPlease choose one of the following options: ")
    print("\n1- Admin\n" + "2- Guest\n" + "3- Exit")
    print("----------------------------")

def display_guest_menu():
    print("\nPlease choose one of the following options: ")
    print("\n1- Book a Ticket\n" + "2- Exit")
    print("----------------------------")

def display_admin_menu():
    print("\nPlease choose one of the following options: ")
    print("\n1- Display Statistics\n" + "2- Book a Ticket\n" + "3- Display all tickets\n" + "4- Change ticket's priority\n" + "5- Disable ticket\n" + "6- Run Events\n" + "7- Exit")
    print("----------------------------")
#----------------------------------------------------------
def display_statistics(ticket_list):
    event_tickets_count = {}

    for ticket_info in ticket_list:
        event_id = ticket_info.split(", ")[1]
        if event_id in event_tickets_count:
            event_tickets_count[event_id] += 1
        else:
            event_tickets_count[event_id] = 1

    max_tickets_event_id = None
    max_tickets_count = 0
    # .items is used to return the list with all dictionary keys with values.
    for event_id, ticket_count in event_tickets_count.items():
        if ticket_count > max_tickets_count:
            max_tickets_event_id = event_id
            max_tickets_count = ticket_count

    return max_tickets_event_id, max_tickets_count

def book_ticket():

    def get_first_index(line):
        return int(line.strip().split(",")[0][4:])

    def valid_date(date_str):
        try:
            year = int(date_str[:4])
            month = int(date_str[4:6])
            day = int(date_str[6:8])
            current_year = datetime.today().year
            return (
                current_year <= year <= current_year + 1 and 
                1 <= month <= 12 and
                1 <= day <= 31
            )
        except ValueError:
            return False

    def create_new_line(last_line):
        last_index = get_first_index(last_line)
        new_index = last_index + 1

        while True:
            try:
                # the .format method formats the specified value(s) and insert them inside the string's placeholder.
                new_ticket_id = "tick{:03d}".format(new_index)
                new_username = input("Enter a username: ")
                new_event_id = input("Enter the event ID(i.e: ev022): ")
                new_date = input("Enter the date of the event (YYYYMMDD): ")
                if not re.match(r'^\d{8}$', new_date) or not valid_date(new_date):
                    print("Invalid date. Please use valid YYYYMMDD format.")
                    continue
                elif not re.match(r'^ev\d{3}$', new_event_id):
                    print("Invalid event ID. Please use valid ID (i.e: ev002)")
                    continue
                new_prio = int(input("Enter priority: "))
                if  re.match(r'^tick\d{3}$', new_ticket_id) and \
                    re.match(r'^ev\d{3}$', new_event_id) and \
                    re.match(r'[a-zA-Z]', new_username) and \
                    len(new_prio) <= 3:
                    return new_ticket_id, new_event_id, new_username, new_date, new_prio
                else:
                    print("Invalid input. Please try again.")
                
            except ValueError: 
                print("Invalid input. Please try again.")
                continue    

    last_line = updated_text_file[-1]
    new_line = create_new_line(last_line)
    updated_text_file.append(",".join(new_line))

    print("Updated Ticket's list:")
    for line in updated_text_file:
        print(line)

    file_path = r"tickets.txt"
    with open(file_path, "w") as file:
        for line in updated_text_file:
            file.write(line + "\n")

def display_all_tickets(updated_text_file):
    
    def valid_date(date_str):
        try:
            date = datetime.strptime(date_str, "%Y%m%d")
            return date >= datetime.today()
        except ValueError:
            return False

    def get_valid_tickets(updated_text_file):
        valid_tickets = []
        for line in updated_text_file:
            ticket_info = line.strip().split(", ")
            if len(ticket_info) == 5 and check_line(line) and valid_date(ticket_info[3]):
                valid_tickets.append(ticket_info)

        def sort_key(ticket):
            # .strptime is used to parse a string representing a date and time according to %Y%m%d format.
            event_date = datetime.strptime(ticket[3], "%Y%m%d")
            return event_date, ticket[1]

        valid_tickets.sort(key=sort_key)
        return valid_tickets

    valid_tickets = get_valid_tickets(updated_text_file)

    print("Valid Tickets:")
    for ticket in valid_tickets:
        # .join takes all the elements of an iterable and joins them into a single string.
        print(",".join(ticket))

def change_tickets_prio():
    while True:
        try:
            old_ticket_id = input("Enter the ticket id you want to change: ")
            old_priority = input("Enter its priority: ")

            if re.match(r'^tick\d{3}$', old_ticket_id) and old_priority.isdigit() and len(old_priority) <= 3:
                old_priority = int(old_priority)
                found_ticket = None

                for line in updated_text_file:
                    ticket_info = line.strip().split(", ")

                    if len(ticket_info) == 5 and ticket_info[0] == old_ticket_id and int(ticket_info[4]) == old_priority:
                        found_ticket = ticket_info
                        break

                if found_ticket:
                    new_priority = input("Enter the new priority for the ticket: ")

                    if new_priority.isdigit() and len(new_priority) <= 3:
                        new_priority = int(new_priority)
                        found_ticket[4] = str(new_priority)

                        print(f"Priority of ticket {old_ticket_id} updated to {new_priority}.")
                        break
                    else:
                        print("Invalid input for the new priority. Please enter a valid integer with a maximum of 3 digits.")
                else:
                    print(f"Ticket with ID {old_ticket_id} and priority {old_priority} not found in the list.")
            else:
                print("Invalid input for ticket ID or priority. Please enter valid values.")
        except:
            print("Invalid input")
            continue

def disable_ticket():
    ticket_id = input("Enter the ticket ID you wish to remove: ")
    if re.match(r'^tick\d{3}$', ticket_id):
        found = False
        for line in updated_text_file:
            tickets = line.strip().split(", ")
            if len(tickets) == 5 and tickets[0] == ticket_id:
                updated_text_file.remove(line)
                found = True
                break
        if found:
            print(f"Ticket {ticket_id} removed from the system.")
        else:
            print(f"Ticket {ticket_id} not found in the system.")

def run_events():
    today = datetime.today().strftime("%Y%m%d")
    todays_events = []
    
    for line in updated_text_file[:]:
        tickets = line.strip().split(", ")
        if len(tickets) == 5 and tickets[3] == today:
            todays_events.append(tickets)
            updated_text_file.remove(line)

    if not todays_events:
        print("No events have been found today!")
    else:
        print("Today's Events:\n")
        for lines in todays_events:
            print(lines)
#----------------------------------------------------------
main()