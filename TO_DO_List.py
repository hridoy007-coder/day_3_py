def task():
    tasks = []
    print("Welcome to the To-Do List App!")

    total_task = int(input("Enter how many task you want to add ="))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} =")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-ADD\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation ==1:
            add = input("Enter task to want to add =")
            tasks.append(add)
            print(f"Task{add} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter task to want to update =")
            if update_val in tasks:
                up =  input("Enter new task =")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"update task{up}")

        elif operation == 3:
            delete_val = input("Enter task to want to delete =")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task {delete_val} has been successfully deleted...")

        elif operation == 4: 
            print(f"Today's tasks = {tasks}")

        elif operation == 5:
            print("closing the program...")
            break

        else:
            print("Invalid input")


task()