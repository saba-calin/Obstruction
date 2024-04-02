from Obstruction.user_interface.user_interface import UserInterface
from Obstruction.user_interface.user_interface_pygame import UserInterfacePygame


if __name__ == "__main__":
    print("Would you like to use the GUI? (y/n)")
    option = input(">")

    if option == "y":
        ui = UserInterfacePygame()
    elif option == "n":
        ui = UserInterface()
    else:
        print("Error: Invalid input! ... Exiting the application")
        exit()

    ui.start()
