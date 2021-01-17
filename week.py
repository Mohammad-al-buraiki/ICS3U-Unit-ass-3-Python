# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is the number of weekday


def main():
    # this function is to find the weekday number
        user_number = int(input("Enter the number: "))
        if user_number == 1:
            print("Sunday")
        elif user_number == 2:
            print("Monday")
        elif user_number == 3:
            print("Tuesday")
        elif user_number == 4:
            print("Wednesday")
        elif user_number == 5:
            print("Thursday")
        elif user_number == 6:
            print("Friday")
        elif user_number == 7:
            print("Saturday")
        else:
            print("There is no weekday with the number {0}."
                  .format(user_number))

            
if __name__ == "__main__":
    main()
