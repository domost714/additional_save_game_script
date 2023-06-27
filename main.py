import os
import shutil

destination = os.getcwd() + "/Copy"


def read_path():
    path = open("path.txt", "r")
    path = path.readline()
    return path


def save():
    shutil.copytree(read_path(), destination, dirs_exist_ok=True)


def delete():
    try:
        shutil.rmtree(destination)
    except FileNotFoundError:
        print("There is nothing to delete")


def print_menu():
    print("""
    1. Save
    2. Delete
    0. Exit
    """)


def menu():
    option = ""
    while option != "0":
        print_menu()
        option = input("What do you want to do? ")
        if option == "1":
            save()
        elif option == "2":
            delete()
        elif option == "0":
            print()
        else:
            print("Wrong option. Choose the right one")


if __name__ == '__main__':
    menu()
