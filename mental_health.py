import depression as dp

def quiz():
    print("Menu: ")
    print("0. Exit")
    print("1. for depression")

    choice = input("Enter input")

    if choice == '0':
        print("Exiting...")
        return
    elif choice == '1':
        dp.main()
    else:
        print("Invalid choice")
        return 

def main():
    while(1):
        print("Menu: ")
        print("0. Exit")
        print("1. Quiz for testing")

        choice = input("Enter the choice: ")

        if choice == '0':
            print("Exiting...")
            return
        elif choice == '1':
            quiz()
        else:
            print("Invalid choice")
            return 