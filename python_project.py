#!/usr/bin/env python3

import csv
import time
import math
import log
import mental_health as mh
import report as rp

def verify():
    MAX_ATTEMPTS = 3
    LOCKOUT_TIME = 5  # seconds

    attempt_count = 0
    
    while attempt_count < MAX_ATTEMPTS:
        user_id = input("Enter your ID: ")
        user_password = input("Enter your password: ")

        with open('users.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user_id'].strip() == user_id.strip() and row['password'].strip() == user_password.strip():
                    print("Access granted.")
                    return user_id
            print("Access denied. Incorrect ID or password.")
            attempt_count += 1
            
            if attempt_count == MAX_ATTEMPTS:
                print(f"Maximum attempt limit reached. Please try again in {LOCKOUT_TIME} seconds.")
                time.sleep(LOCKOUT_TIME)
                attempt_count = 0
                LOCKOUT_TIME = 20 * math.log(LOCKOUT_TIME)

    return None

def add_user():
    new_id = input("Enter new user ID: ")
    new_password = input("Enter new user password: ")

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['user_id', 'password'])
        writer.writerow({'user_id': new_id, 'password': new_password})
    
    print("New user added successfully.")



def main(user_type):
    while True:
        print("\nMenu: ")
        print("0. Exit")
        print("00. Sign out")
        if user_type == "admin":
            print("1. Tracker")
            print("2. Mental Health")
            print("3. Full Report")
            print("4. System Settings")
            print("5. Add User")  # Admin-only feature

        elif user_type != "admin":  # Regular user menu
            print("1. Tracker")
            print("2. Mental Health")

        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting program...")
            exit(0)
        elif choice == '00':
            print("Signing Out...")
            break

        elif choice == '1':
            log.log()
        elif choice == '2':
            mh.main()
        elif user_type == "admin" and choice == '3':
            while True:
                print("Menu: ")
                print("0. Exit")
                print("1. Load weekly data")
                print("2. Load daily data")
                print("3. generate report")
                
                choice = input("Enter your choice: ")
                

        elif user_type == "admin" and choice == '4':
            print("Accessing System Settings...")
        elif user_type == "admin" and choice == '5':
            add_user()
        else:
            print("Invalid choice")



if __name__ == '__main__':
    while True:
        print("Already a user?")
        choice = input("y/n: ")

        if(choice == "y"):
            user_type = verify()
            if(user_type):
                main(user_type)
            else:
                exit(0)
        else:
            print("Request Admin to be a user...")
            exit(0)
        
