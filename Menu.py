"""
Module for displaying menu items, and executing the functions according to the user input.
"""
from Switch import Switch
from Router import Router
import json


def load_device_data(filename):
    """
    Loads data from JSON file.
    :param filename: Represents the name of the target file.
    :return: Dictionary containing the data for the devices.
    """
    with open(filename, 'r') as file:
        return json.load(file)


def main() -> None:
    """
    Main function responsible for running the main routine.
    Checks if the device we want to configure exists in our device list.
    :return:
    """

    devices = load_device_data('deviceDetails.json')

    print("""
    Welcome to Main Menu of the Network Automation Tool!
    
    The following options are available:
    1. Configure a device.
    2. Exit the application.
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        target_device = input("Enter the ip of the device you want to configure: ")
        device_not_found = True
        for device in devices:
            if device_not_found:
                try:
                    if device['ip'] == target_device:
                        device_not_found = False
                        if "router" in device['type'].lower():
                            ConfigMenuRouter(device)
                        elif "sw" in device['type'].lower():
                            ConfigMenuSwitch(device)

                except TimeoutError or ConnectionError:
                    print("Connection failed, network may be unreachable, or target device might not exist.")
        if device_not_found:
            raise ValueError(f"Device with ip {target_device} not found. Please add it to the file or make sure the ip is correct.")
    elif choice == '2':
        print("Thank you for using the Network Automation Tool!")
        exit()
    else:
        raise ValueError("Invalid choice. Please restart the script to try again.")


def ConfigMenuRouter(device) -> None:
    """
    Menu with configuration options in case the device we connected to is a Router.
    :return:
    """

    router_instance = Router(device['name'], device['ip'], device['username'], device['password'], device['privileged_password'])

    print("""
    The following configuration options are available for the Router:
    1. Configure HSRP for a Vlan.
    2. Configure a DHCP server.
    3. Set up RIPv2.
    4. Exit to Main Menu.
    """)
    config_choice = input("Enter your choice: ")
    if config_choice == '1':
        router_instance.config_HSRP(device['ip'])
    elif config_choice == '2':
        router_instance.setup_DHCP()
    elif config_choice == '3':
        router_instance.config_RipV2()
    elif config_choice == '4':
        main()
    else:
        print("Please enter a valid option.")
        ConfigMenuRouter(device)


def ConfigMenuSwitch(device) -> None:
    """
    Menu with configuration options in case the device we connected to is a Switch.
    :return:
    """

    switch_instance = Switch(device['name'], device['ip'], device['username'], device['password'], device['privileged_password'])
    print("""
    The following configuration options are available for the Switch:
    1. Configure a Vlan.
    2. Configure Security.
    3. Configure STP.
    4. Configure HSRP (for multilayer switches only).
    5. Exit to Main Menu.
    """)
    config_choice = input("Enter your choice: ")
    if config_choice == '1':
        switch_instance.config_Vlan()
    elif config_choice == '2':
        switch_instance.config_Security()
    elif config_choice == '3':
        switch_instance.config_STP()
    elif config_choice == '4':
        if "multilayer" not in device['name'].lower():
            print("This is not a multilayer switch, as such it can not act as a router.")
            ConfigMenuSwitch(device)
        else:
            switch_instance.config_HSRP()

    elif config_choice == '5':
        main()
    else:
        print("Please enter a valid choice.")
        ConfigMenuSwitch(device)
