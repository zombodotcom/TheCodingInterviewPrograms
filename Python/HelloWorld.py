#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function


def main():
    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for something")
        print("Choose 2 for something")
        print("Choose 3 for something")
        print("Choose 4 for something")
        print("Choose 5 to go to another menu")

        choice = input ("Please make a choice: ")

        if choice == "5":
            print("Go to another menu")
            # second_menu()
        if choice == "4":
            print("Do Something 4")
        if choice == "3":
            print("Do Something 3")
        if choice == "2":
            print("Do Something 2")
        if choice == "1":
            print("Do Something 1")
        else:
            print("I don't understand your choice.")


def second_menu():
    print("This is the second menu")


if __name__ == '__main__':
  main()