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


def main(target_device: str) -> None:
    """
    Main function responsible for running the main routine.
    :param target_device: Checks if the device we want to configure exists in our device list.
    :return:
    """
    devices = load_device_data('deviceDetails.json')

    for device in devices:
        try:
            if device['ip'] == target_device:
                if device['type'] == "normal_sw" or device['type'] == "multilayer_sw":
                    switch = Switch(device['name'], device['ip'], device['username'], device['password'],
                                    device['privileged_password'])
                    switch.configure_port_channel()
                    switch.apply_security()
                elif device['type'] == "router":
                    router = Router(device['name'], device['ip'], device['username'], device['password'],
                                    device['privileged_password'])
                    router.config_rip2()
                    router.setup_routes()
                return
            else:
                raise Exception("Device not found")
        except TimeoutError or ConnectionError:
            print("Connection failed, network may be unreachable, or target device might not exist.")


if __name__ == "__main__":
    given_ip = input("Enter IP Address for the device you want to configure: ")
    main(given_ip)
