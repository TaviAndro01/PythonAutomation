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
                        if "router" in device['name'].lower():
                            ConfigMenuRouter()
                        elif "switch" in device['name'].lower():
                            ConfigMenuSwitch(device)
                    else:
                        raise Exception("Device not found")
                except TimeoutError or ConnectionError:
                    print("Connection failed, network may be unreachable, or target device might not exist.")
    elif choice == '2':
        print("Thank you for using the Network Automation Tool!")
        exit()


def ConfigMenuRouter() -> None:
    """
    Menu with configuration options in case the device we connected to is a Router.
    :return:
    """
    print("""
    The following configuration options are available for the Router:
    1. Configure a vlan.
    2. Configure a sub-interface.
    3. Configure a DHCP server.
    4. Set up RIPv2.
    5. Exit to Main Menu.
    """)
    config_choice = input("Enter your choice: ")
    if config_choice == '1':
        pass
    elif config_choice == '2':
        pass
    elif config_choice == '3':
        pass
    elif config_choice == '4':
        pass
    elif config_choice == '5':
        main()
    else:
        raise ValueError("Invalid choice")


def ConfigMenuSwitch(device) -> None:
    """
    Menu with configuration options in case the device we connected to is a Switch.
    :return:
    """
    print("""
    The following configuration options are available for the Switch:
    1. Configure a Vlan.
    2. Configure a PortChannel.
    3. Configure Security.
    4. Configure STP.
    5. Configure HSRP (for multilayer switches only).
    6. Exit to Main Menu.
    """)
    config_choice = input("Enter your choice: ")
    if config_choice == '1':
        pass
    elif config_choice == '2':
        pass
    elif config_choice == '3':
        pass
    elif config_choice == '4':
        pass
    elif config_choice == '5':
        if "multilayer" not in device['name'].lower():
            print("This is not a multilayer switch, as such it can not act as a router.")
            ConfigMenuSwitch(device)
    elif config_choice == '6':
        main()
    else:
        raise ValueError("Invalid choice.")
