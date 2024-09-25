"""
Module responsible for connectivity.
"""
import paramiko
from time import sleep


class DeviceConnection:
    """
    Class meant to handle connection logic.
    Connect method, sets up the SSH connection.
    Send_command method, sends the command(s) to the device.
    Close method, is tasked with closing the SSH connection.
    The data for the connection will be fetched from a JSON file.
    """
    def __init__(self, ip, username, password):
        """
        The constructor for DeviceConnection class.
        :param ip: The IP address of the target device.
        :param username: The username for the SSH connection.
        :param password: The password for the SSH connection.
        """
        self.ip = ip
        self.username = username
        self.password = password
        self.client = None
        self.shell = None

    def connect(self, priv_exec_pass) -> None:
        """
        Method that establishes the SSH connection to the device.
        :param priv_exec_pass: The password used to access the privileged exec mode of the target device.
        """
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.ip, username=self.username, password=self.password)
            self.shell = self.client.invoke_shell()
            self.shell.send(f'ena\n{priv_exec_pass}\nconf t\n')
            sleep(3)
        except paramiko.SSHException as e:
            print(f"Failed to connect to {self.ip}: {e}")
            self.close()

    def send_command(self, command):
        """
        Method that sends the command to the device.
        :param command: The command to send to the device.
        :return: The output and error (if any) from the command.
        """
        if not self.shell:
            print("Connection not established. Please connect first.")
            return None, "Connection not established."

        self.shell.send(command + '\n')
        sleep(3)

        output = ""
        while self.shell.recv_ready():
            output += self.shell.recv(65535).decode('utf-8')

        return output, ""

    def close(self) -> None:
        """
        Method that closes the SSH connection.
        """
        if self.client:
            self.shell.send('\ndo wr\n')
            self.client.close()
            self.client = None
            self.shell = None