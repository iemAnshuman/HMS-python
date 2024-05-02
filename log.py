import water as wt
import calories as cal
import exercise as ex

def log():
    while(True):
        print("Menu: ")
        print("0. Exit")
        print("00. Go back")
        print("1. Water tracker")
        print("2. Calories tracker")
        print("3. Exercise tracker")
    
        choice = (input("Enter choice: "))
        if(choice == '0'):
            print("Exiting...")
            exit(0)
        elif choice == '00':
            break
        elif(choice == '1'):
            wt.main()
        elif(choice == '2'):
            cal.calorie()
        elif(choice == '3'):
            ex.main()
        else:
            print("Invalid Input")


    