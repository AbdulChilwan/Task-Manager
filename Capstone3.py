# Importing the modules needed, date, to get the current date and re, for multiple splitting.
import datetime
from datetime import date
import re

# Making a function to retrieve all usernames.
def retrieving_username():
    user_data = ""
    file_lines = 0
    usernames = []
    # Opening 'user.txt' and spliting each first word on each line, which is the username.
    f = open ('user.txt', 'r')
    for line in f:
        user_data += line
        file_lines += 1
    user_data = str(user_data)
    user_data = re.split(", |\n", user_data)
    # Adding each username to a list.
    count = 0
    for i in range (0,file_lines):
        usernames.append(user_data[count])
        count += 2
    f.close()
    return usernames

# Making a function to retrieve all passwords.
def retrieving_password ():
    user_data = ""
    file_lines = 0
    passwords = []
    # Opening 'user.txt' and spliting each second word on each line, which is the password.
    f = open ('user.txt', 'r')
    for line in f:
        user_data += line
        file_lines += 1
    user_data = str(user_data)
    user_data = re.split(", |\n", user_data)
    # Adding each password to a list.
    count = 0
    for i in range (0,file_lines):
        count += 1
        passwords.append(user_data[count])
        count += 1
    f.close()
    return passwords

# Function created for verifying if the username matches the password.
# Allows the user to enter the correct details until it logs them in.
# And returns the current user logged in.
def verify(username,password):
    checking = True
    while checking:
        input_user = input("Please enter your username: ")
        input_password = input("Please enter your password: ")
        for i in range (0,len(username)):
            if input_user == username[i]:
                if input_password == password[i]:
                    print("\n###################")
                    print("Login Success!")
                    print("###################\n")
                    checking = False
                elif input_password != password[i]:
                    print("\n--------------------------------")
                    print("Password does not match username.")
                    print("--------------------------------")
        if checking:
            print("|==================|")
            print("| Please try again |")
            print("|==================|")
    return input_user

# Creating a function which allows registering of users.
# Asks user to input the new details and if password matches confirm password, the details are saved in 'user.txt'
def register(usernames):
    with open('user.txt','a')as f:
        user_password = ""
        con_password = ""
        while True:
            new_user = input("\nEnter the new user name: ")
            user_password = input("Enter the password : ")
            con_password = input("Confirm the password: ")
            if(new_user in username):
                print("This user already exists, try another username.")
            elif(user_password != con_password):
                print("\n===================================")
                print("Passwords does not match, try again.")
                print("===================================\n")
            else:
                print("\n********************************")
                print("|| Your entry has been saved. ||")
                print("********************************\n")
                f.write("\n" +new_user +", " +user_password)    
                f.close()
                break

# Displays the text in the files 'task_overview.txt' and 'user_overview.txt' which are the statistics.
# These files are created from calling another function. 
def display_statistics ():
    print("===============================================")
    f = open('task_overview.txt', 'r')
    for line in f:
        print(line)
    f.close()
    print("===============================================")
    f = open('user_overview.txt', 'r')
    for line in f:
        print(line)
    f.close()
    print("===============================================")
    
# Allows the user to add a task, asking them to input the details and then saving it to "task.txt"
def add_task():
    with open('tasks.txt','a')as f:
        assigned = input("Please enter the username of who the task will be assigned to: ")
        title = input("Please enter the title of the task: ")
        description = input("Enter a description of the task: ")
        due = input("Enter the date the task is due: ")
        current_time = datetime.datetime.now()
        date = str(current_time.day)
        month = current_time.month
        # Changes the format, converting the number of the month to its name.
        if (month == 1):
            current_month = "Jan"
        elif (month == 2):
            current_month = "Feb"
        elif (month == 3):
            current_month = "Mar"
        elif (month == 4):
            current_month = "Apr"
        elif (month == 5):
            current_month = "May"
        elif (month == 6):
            current_month = "Jun"
        elif (month == 7):
            current_month = "Jul"
        elif (month == 8):
            current_month = "Aug"
        elif (month == 9):
            current_month = "Sep"
        elif (month == 10):
            current_month = "Oct"
        elif (month == 11):
            current_month = "Nov"
        elif (month == 12):
            current_month = "Dec"
        else:
            current_month = "ERROR"

        # Saves the details, and sets the task start date to todays date, and task completed set to "No" automatically.         
        year = str(current_time.year)
        complete = "No"
        print("\n********************************")
        print("|| Your entry has been saved. ||")
        print("********************************\n")
        f.write("\n" + assigned +", " + title+", " + description+", " + date +" "+ current_month +" "+year +", " + due+", " + complete)
        f.close()

# Allows the user to view all tasks, from 'task.txt', and displays it all on screen, in a specific format.
def view_all_tasks():
    content = ""
    lines = 0
    f = open('tasks.txt', 'r')
    for line in f:
        content += line
        lines += 1
    content = str(content)
    content = content.split(", ")   
    va_task = []
    va_new_task = []
    va_title = []
    va_description = []
    va_start = []
    va_due = []
    va_comp = []
    number = 0
    # Saves each data into an appropiate list. Combines each set of data.
    for i in range (0,lines):
        va_task.append(content[number])
        number += 1
        va_title.append(content[number])
        number += 1
        va_description.append(content[number])
        number += 1
        va_start.append(content[number])
        number += 1
        va_due.append(content[number])
        number += 1
        va_comp.append(content[number].split("\n",1)[0])

    for i in range (0,len(va_task)):
        if (va_task[i][0:2] == "Ye"):
            lona = str(va_task[i].replace("Yes\n",""))
            va_new_task.append(lona)
        else:
            lona = str(va_task[i].replace("No\n",""))
            va_new_task.append(lona)
        
    for i in range (0,lines):
        print("=============================================================")
        print("Task:                   {}".format(va_title[i]))
        print("Assigned to:            {}".format(va_new_task[i]))
        print("Date assigned:          {}".format(va_start[i]))
        print("Due date:               {}".format(va_due[i]))
        print("Task complete?          {}".format(va_comp[i]))
        print("Task description:            \n {}".format(va_description[i]))
        if (i == lines-1):
            print("=============================================================")
            f.close()

# Allows the user to see the tasks, specifically to them.
# And allows them to edit it, the task they chosen.
def view_my_task(input_user):
    has_task = True
    content = ""
    lines = 0
    f = open('tasks.txt', 'r')
    for line in f:
        content += line
        lines += 1
    content = str(content)
    content = content.split(", ")   
    va_task = []
    va_new_task = []
    va_title = []
    va_description = []
    va_start = []
    va_due = []
    va_comp = []
    number = 0
    chosen_task = []
    # Adding each group of data into its specific list.
    for i in range (0,lines):
        va_task.append(content[number])
        number += 1
        va_title.append(content[number])
        number += 1
        va_description.append(content[number])
        number += 1
        va_start.append(content[number])
        number += 1
        va_due.append(content[number])
        number += 1
        va_comp.append(content[number].split("\n",1)[0])
    # Replacing the '\n' so just No or Yes is displayed.
    for i in range (0,len(va_task)):
        if (va_task[i][0:2] == "Ye"):
            lona = str(va_task[i].replace("Yes\n",""))
            va_new_task.append(lona)
        else:
            lona = str(va_task[i].replace("No\n",""))
            va_new_task.append(lona)

    # Checks if the the user logged in links with the task and displays their tasks if the username matches.
    current_task = 0
    for i in range (0,lines):
        if(input_user == va_new_task[i]):
            current_task += 1
            chosen_task.append(va_title[i]+"!"+va_new_task[i]+"!"+va_start[i]+"!"+va_due[i]+"!"+va_comp[i]+"!"+va_description[i])
            print("=================================================================")
            print("------------------------- Task No: {} ---------------------------".format(current_task))
            print("Task:                   {}".format(va_title[i]))
            print("Assigned to:            {}".format(va_new_task[i]))
            print("Date assigned:          {}".format(va_start[i]))
            print("Due date:               {}".format(va_due[i]))
            print("Task complete?          {}".format(va_comp[i]))
            print("Task description:            \n {}".format(va_description[i]))
            print("=================================================================")

        if (i == lines-1):      
            if input_user not in va_new_task:
                print("\n##########################")
                print("You have no current tasks.")
                print("##########################\n")
                has_task = False
                
    f.close()
    while (has_task):
        # Allows the user to edit the task, by selecting it's task no.
        edit_task = int(input("Select a Task No to edit, or enter -1 to return to the main menu: "))
        if (edit_task < len(chosen_task)+1 and edit_task > 0):
            task_selected = chosen_task[edit_task-1].split("!")
            print("=================================================================")
            print("Selected Task:")
            print("=================================================================")
            print("------------------------- Task No: {} ---------------------------".format(edit_task))
            print("Task:                   {}".format(task_selected[0]))
            print("Assigned to:            {}".format(task_selected[1]))
            print("Date assigned:          {}".format(task_selected[2]))
            print("Due date:               {}".format(task_selected[3]))
            print("Task complete?          {}".format(task_selected[4]))
            print("Task description:            \n {}".format(task_selected[5]))
            print("=================================================================")
            # Asking the user to enter the task no. to edit.
            print("1: Mark as complete \n 2: Edit task")
            select_option = int(input("Select an option: "))
            
            # Changes the complete status of the task to yes.
            if (select_option == 1):
                task_selected[4] = "Yes"
                if task_selected[0] in va_title:
                    counter = va_title.index(task_selected[0])
                    new_data = task_selected[1] +", " + task_selected[0]+", " + task_selected[5]+", " + task_selected[2] +", " + task_selected[3]+", " + task_selected[4] + "\n"
                    with open('tasks.txt','r') as file:
                        data = file.readlines()
                        data[counter] = new_data
                    file.close()
                    with open('tasks.txt','w') as file:
                        file.writelines(data)
                        print("############################# The task has been marked as complete #############################")
                        has_task = False
                    file.close()
            # Checks if the task is completed, if it is, it can not be edited.
            elif (select_option == 2):
                if (task_selected[4] == "Yes"):
                    print("This task is marked as completed, and therefore can not be edited.")
                # Asks the user if they would like the changed the task assigned person, or the due date.
                else:
                    print("1: Edit task assigned to. \n2: Edit due date.")
                    edit_option = int(input("Select an option: "))
                    if (edit_option == 1):
                        print("Edit user")
                        user_assigned = input("Enter the user to be assgined to this task: ")
                        task_selected[1] = user_assigned
                        if task_selected[0] in va_title:
                            counter = va_title.index(task_selected[0])
                            # Saves all the new data and stores it into the task file.
                            new_data = task_selected[1] +", " + task_selected[0]+", " + task_selected[5]+", " + task_selected[2] +", " + task_selected[3]+", " + task_selected[4] + "\n"
                            with open('tasks.txt','r') as file:
                                data = file.readlines()
                                data[counter] = new_data
                            file.close()
                            with open('tasks.txt','w') as file:
                                file.writelines(data)
                                print("############################# The task has been updated #############################")
                                has_task = False
                            file.close()

                    # If the user wants the change the due date. It saves the new date and saves it into the task file.
                    elif (edit_option == 2):
                        print("Edit user")
                        new_date = input("Enter the new due date (in whole): ")
                        task_selected[3] = new_date
                        if task_selected[0] in va_title:
                            counter = va_title.index(task_selected[0])
                            new_data = task_selected[1] +", " + task_selected[0]+", " + task_selected[5]+", " + task_selected[2] +", " + task_selected[3]+", " + task_selected[4] + "\n"
                            with open('tasks.txt','r') as file:
                                data = file.readlines()
                                data[counter] = new_data
                            file.close()
                            with open('tasks.txt','w') as file:
                                file.writelines(data)
                                print("############################# The task has been updated #############################")
                                has_task = False
                            file.close()
                    else:
                        print("This is not an option.")
            # Ends the while loop.
            has_task = False
                
        elif (edit_task == -1):
            has_task = False
        else:
            print("This task number does not exist, please try again.")

# Collects data about the tasks, from task.txt and displayed data statistics about them in a file called task_overview.txt.
def task_overciew ():
    lines = 0
    number = 0
    content = ""
    yes_count = 0
    no_count = 0
    # Readinf each line and counting amount of lines ... each line = 1 task
    with open('tasks.txt','r') as file:
        for i in file:
            content += i
            lines += 1
    file.close()

    content = str(content)
    content = content.split(", ")

    va_comp = []
    va_due = []
    # Saving due_dates and complete_status into each set of its data into a list.
    for i in range (0,lines):
        number += 1
        number += 1
        number += 1
        number += 1
        va_due.append(content[number])
        number += 1
        va_comp.append(content[number].split("\n",1)[0])
    
    new_date_format = []
    for i in range (lines):
        now = va_due[i].split(" ")
        # Converting the month to the month number.
        if "Jan" == now[1] or "January" == now[1]:
            now[1] = 1
        elif "Feb" == now[1] or "February" == now[1]:
            now[1] = 2
        elif "Mar" == now[1] or "March" == now[1]:
            now[1] = 3
        elif "Apr" == now[1] or "April" == now[1]:
            now[1] = 4
        elif "May" == now[1] or "May" == now[1]:
            now[1] = 5
        elif "Jun" == now[1] or "June" == now[1]:
            now[1] = 6
        elif "Jul" == now[1] or "July" == now[1]:
            now[1] = 7
        elif "Aug" == now[1] or "August" == now[1]:
            now[1] = 8
        elif "Sep" == now[1] or "September" == now[1]:
            now[1] = 9
        elif "Oct" == now[1] or "October" == now[1]:
            now[1] = 10
        elif "Nov" == now[1] or "November" == now[1]:
            now[1] = 11
        elif "Dec" == now[1] or "December" == now[1]:
            now[1] = 12
        # Saving all the dates into a list.
        for i in range (len(now)):
            now[i] = int(now[i])
        now = datetime.date(now[2],now[1],now[0])
        new_date_format.append(now)

    # Comparing the due dates to the current dates, and keeping count of each task overdue.
    today = date.today()
    overdue = 0
    for i in range (len(va_comp)):
        if va_comp[i] == "No":
            no_count += 1
            if today > new_date_format[i]:
                overdue += 1
        else:
            yes_count += 1
    # Calculating the percentage of the task details, percentage incomplete and percentage overdue.
    percentage_incomplete = (no_count/len(va_comp)) * 100
    percentage_overdue = (overdue/len(va_comp)) * 100
    # Writing the specified data to the task_overview file.
    with open ('task_overview.txt','w') as file:
        file.write(f"There are a total of {len(va_comp)} tasks.\n")
        file.write(f"Number of completed tasks : {yes_count}\n")
        file.write(f"Number of tasks not completed : {no_count}\n")
        file.write(f"Number of tasks overdue : {overdue}\n")
        file.write(f"The percentage of incomplete tasks : {percentage_incomplete}%\n")
        file.write(f"The percentage of overdue tasks : {percentage_overdue}%\n")
    # Returns all the data in the task file. (not sorted)
    return content

# Creating a function to write to the file user_overview, writing the statistics wanted.
def user_overview ():
    # Calling the retrieving_username() to save all the usernames.
    # Calling the task_overciew() to save all the content.
    users = retrieving_username()
    content = task_overciew()

    lines = 0
    f = open('tasks.txt', 'r')
    for line in f:
        content += line
        lines += 1
    f.close()

    va_task = []
    va_new_task = []
    va_title = []
    va_description = []
    va_start = []
    va_due = []
    va_comp = []
    number = 0

    for i in range (0,lines):
        va_task.append(content[number])
        number += 1
        va_title.append(content[number])
        number += 1
        va_description.append(content[number])
        number += 1
        va_start.append(content[number])
        number += 1
        va_due.append(content[number])
        number += 1
        va_comp.append(content[number].split("\n",1)[0])

    for i in range (0,len(va_task)):
        if (va_task[i][0:2] == "Ye"):
            lona = str(va_task[i].replace("Yes\n",""))
            va_new_task.append(lona)
        else:
            lona = str(va_task[i].replace("No\n",""))
            va_new_task.append(lona)

    for i in range (len(va_new_task)):
        va_new_task[i] =  va_new_task[i].lower()
    
    new_list = []
    # Using a dictionary, using the users and keys and the value as the amount of tasks they have.
    user_task_count = {}
    for i in range (len(users)):
        if users[i].casefold() in va_new_task:
            new_list.append(users[i])
            counter = va_new_task.count(users[i])
            user_task_count[users[i]] = counter

    for i in range (len(new_list)):
        new_list[i] =  new_list[i].lower()

    # Writing the amount of users, each line = 1 user in file 'user.txt'
    # Writing the amount of tasks, each line = 1 task in file 'task.txt'
    # Writing the dictionary of users and the amount of tasks each has.
    with open ('user_overview.txt','w') as overview:
        overview.write(f"There are {len(users)} users.\n")
        overview.write(f"There are {len(va_new_task)} tasks.\n")
        overview.write(f"Each user's break down of tasks: {user_task_count}\n")
        overview.write("==================================================\n")
        # Working out the percentage each tasks each user has, out of the total amount of tasks.
        count = 0
        for line in user_task_count:
            user_percentage = user_task_count[line]/len(va_new_task) * 100
            overview.write(f"{new_list[count]} has {user_percentage} percentage of tasks\n")  
            count += 1

        users_completed_task = []
        with open('tasks.txt','r') as file:
            for i in file:
                line = i
                line = line.split(", ")
                for i in range (len(line)):
                    line[i] = line[i].lower()
                for j in range (len(new_list)):
                    counter = 0
                    if (new_list[j] in line) and (("yes" in line) or ("yes\n" in line)):
                        users_completed_task.append(new_list[j])
        file.close()

        dico = {}
        for i in range (len(users_completed_task)):
            dico[users_completed_task[i]] = users_completed_task.count(users_completed_task[i])
            dico[users_completed_task[i]]
            
        overview.write("==================================================\n")

        
        for i in dico:
            overview.write(f"{i} has {dico[i] / user_task_count[i] *100}% tasks completed\n")

        users_not_completed_task = []
        
        with open('tasks.txt','r') as file:
            for i in file:
                line = i
                line = line.split(", ")
                for i in range (len(line)):
                    line[i] = line[i].lower()
                for j in range (len(new_list)):
                    counter = 0
                    if (new_list[j] in line) and (("no" in line) or ("no\n" in line)):
                        users_not_completed_task.append(new_list[j])
        
        file.close()


        dico = {}
        for i in range (len(users_not_completed_task)):
            dico[users_not_completed_task[i]] = users_not_completed_task.count(users_not_completed_task[i])
            dico[users_not_completed_task[i]]
            
        overview.write("==================================================\n")

        
        for i in dico:
            overview.write(f"{i} has {dico[i] / user_task_count[i] *100}% tasks NOT completed\n")

        overdue_user_task = []
        new_date_format = []
        for i in range (len(va_due)):
            now = va_due[i].split(" ")
            if "Jan" == now[1] or "January" == now[1]:
                now[1] = 1
            elif "Feb" == now[1] or "February" == now[1]:
                now[1] = 2
            elif "Mar" == now[1] or "March" == now[1]:
                now[1] = 3
            elif "Apr" == now[1] or "April" == now[1]:
                now[1] = 4
            elif "May" == now[1] or "May" == now[1]:
                now[1] = 5
            elif "Jun" == now[1] or "June" == now[1]:
                now[1] = 6
            elif "Jul" == now[1] or "July" == now[1]:
                now[1] = 7
            elif "Aug" == now[1] or "August" == now[1]:
                now[1] = 8
            elif "Sep" == now[1] or "September" == now[1]:
                now[1] = 9
            elif "Oct" == now[1] or "October" == now[1]:
                now[1] = 10
            elif "Nov" == now[1] or "November" == now[1]:
                now[1] = 11
            elif "Dec" == now[1] or "December" == now[1]:
                now[1] = 12
            
            for i in range (len(now)):
                now[i] = int(now[i])
            now = datetime.date(now[2],now[1],now[0])
            new_date_format.append(now)
            
        today = date.today()
        overdue = 0
        for i in range (len(va_comp)):
            if va_comp[i] == "No" and today > new_date_format[i]:
                overdue_user_task.append(va_new_task[i])

        overview.write("==================================================\n")
       
        another_list = list(dict.fromkeys(overdue_user_task))
        
        for i in range (len(another_list)):
            if another_list[i] in overdue_user_task:

                strep = overdue_user_task.count(overdue_user_task[i])
                overview.write(f"{overdue_user_task[i]} has {strep / user_task_count[overdue_user_task[i]] * 100}% tasks NOT completed AND overdue\n")

                
# Calling the functions, allowing the user to log in.
users = retrieving_username()
passwords = retrieving_password()
login_user = verify(users,passwords)

################################ This is LOGIN #################################
# Asking the user to select from the list of options, some specific to the admin user.
# Calls the function based on their input.
print("Please select an option: ")
while True:
    print("**************************************************")
    if (login_user == "admin"):
        print("r - Registering a user \nd - Display statistics \ngr - generate reports")
    print("a - Adding a task \nva - View all tasks \nvm - view my task \ne - Exit")
    print("**************************************************")
    menu = input("Enter your option: ")
    menu = menu.lower()
    
    if ((menu == "r") and (login_user == "admin")):
        register(users)
        
        
    elif((menu == "d") and (login_user == "admin")):
        display_statistics()

    elif((menu == "gr") and (login_user == "admin")):
        user_overview()
        print("\n###################")
        print('# Reports Generated #')
        print("#####################\n")
    
        
    elif menu == "a":
        add_task()
        
    elif menu == 'va':
        view_all_tasks()
        
    elif menu == 'vm':
        view_my_task(login_user)
        
    elif menu == "e":
        print("\n###########")
        print('# Goodbye #')
        print("###########\n")
        exit()
            

    else:
        print("You have made a wrong choice, Please Try again")            


