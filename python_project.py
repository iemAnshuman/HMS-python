import log 
import mental_health as mh

# idea behind this: to make sure healthcare expert and user access it differently
def verify():
    user_credentials = {
        "user": "0000",
        "health_expert": "1234"
    }
    
    for i in range(3):
        user_id = input("Enter your ID: ")
        user_password = input("Enter your password: ")
        if user_id in user_credentials and user_credentials[user_id] == user_password:
            print("Access granted.")
            return 1
        else:
            print("Access denied. Incorrect ID or password.")
            

def main():
    while(1):
        print("Menu: ")
        print("0. Exit")
        print("1. Tracker")
        print("2. Mental Health")
        print("...")

        choice = (input("Enter choice: "))
        if(choice == '0'):
            return
        elif(choice == '1'):
            log.log()
        elif(choice == '2'):
            mh.main()
        else:
            print("Invalid choice")

if __name__ == '__main__':
    if(verify()):
        main()
