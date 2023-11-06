from mytodoapp.todo import add_task, display_task, delete_task

def main():
    while True:
        print("*** To-Do List Menu ***")
        print("1) Add task")
        print("2) Display Tasks")
        print("3) Delete Task")
        print("4) Quit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            display_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Quitting Program")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
