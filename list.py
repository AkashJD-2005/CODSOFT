tasks = []

def addtask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"task'{task}'added to the list.")

def deletetask():
    listtasks()
    try :
        TaskToDelete = int(input("enter number of the task do you want to delete:"))
        if TaskToDelete  >=0 and TaskToDelete < len(tasks):
            tasks.pop(TaskToDelete)
            print(f"task{TaskToDelete} has removed")
        else :
            print(f"task{TaskToDelete} is not found")
    except :
        print("Invalid data")
def listtasks():
    if not tasks: 
        print("there is no tasks")
    else :
        print("The tasks are:")
        for index,task in enumerate(tasks):
            print(f"task  {index}. {task}")


if __name__=="__main__":
    print("welcome to do list functions:)")
    while True:
        print("\n")
        print("select the one of the following option")
        print(".......................................")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.list the tasks")
        print("4.Quit")

        choice=input("Enter your choise:")
        if(choice=="1"):
            addtask()

        elif(choice=="2"):
            deletetask()

        elif(choice=="3"):
            listtasks()

        elif(choice=="4"):
            break
        else:
            print("invalid data . so please enter a valid data")   




                          