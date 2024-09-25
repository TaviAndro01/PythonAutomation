"""
Module responsible for handling function common between the different device types, as well as the constructor.
e.g: HSRP,
"""
from Connection import DeviceConnection
import subprocess


class Device:
    def __init__(self, name, ip, username, password, priv_exec_pass):
        """
        Constructor for Device.
        :param name: The name of the device (Router/Switch).
        :param ip: The IP address of the device.
        :param username: The username for the device.
        :param password: The password for the device.
        :param priv_exec_pass: The privileged exec mode password.
        """
        self.name = name
        self.ip = ip
        self.username = username
        self.password = password
        self.priv_exec_pass = priv_exec_pass
        self.connection = DeviceConnection(ip, username, password)

    def config_HSRP(self) -> None:
        """
        Method for configuring HSRP (shared for both routers and switches).
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        interface = input("Enter the ID of the interface: ")
        standby_id = input("Enter the ID of the standby interface: ")
        vrouter_ip = input("Enter the IP address of the Virtual Router: ")
        priority = input("Enter the priority of the physical interface (default 100 if not set): ")
        if priority.lower() == "no":
            priority = "100"
        stdout, stderr = self.connection.send_command(
            f'int {interface}\nstandby version 2\nstandby {standby_id} ip {vrouter_ip}\n'
            f'standby {standby_id} priority {priority}\nstandby {standby_id} preempt\n'
        )
        self.connection.close()

    def ping_Device(self) -> None:
        """
        Method for pinging another device with the purpose of testing connectivity.
        :return:
        """
        try:
            self.connection.connect(self.priv_exec_pass)

            ping_target = input("Enter the IP address of the target device: ")

            response = subprocess.run(["ping", "-c", "4", ping_target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if response.returncode == 0:
                print(f"There is connectivity with the device with the IP {ping_target}.")
            else:
                print(f"There is no connectivity with the device with the IP {ping_target}.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.connection.close()
