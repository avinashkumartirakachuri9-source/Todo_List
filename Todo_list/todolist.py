def Todo():
    dictionary={
        1:"ADD",
        2:"VIEW",
        3:"REMOVE",
        4:"EXIT"
    }
    ls=[]
    while True:
        print(f'{1}:"ADD TASK"\n{2}:"VIEW TASK"\n{3}:"REMOVE TASK"\n{4}:"EXIT"')
        a=int(input("Enter Which operation have to perform"))
        b=dictionary[a]
        if b == "ADD":
            user_input = input("Enter the task to add: ")
            ls.append(user_input)

        elif b == "VIEW":
            print("Tasks:", ls)

        elif b == "REMOVE":
            user_input = input("Enter the task to remove: ")
            if user_input in ls:
                ls.remove(user_input)
            else:
                print("Task not found")

        elif b == "EXIT":
            print("Closing the Todo...")
            break
Todo()