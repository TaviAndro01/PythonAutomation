"""
Module responsible for connectivity.
"""
import paramiko


class DeviceConnection:
    """
    Class meant to handle connection logic.
    3 methods, each tasked with doing 1 specific thing.
    Connect method, sets up the ssh connection.
    Send_command method, sends the command('s) to the device.
    Close method, is tasked with closing the ssh connection.
    The data for the connection will be fetched from a json file.
    """
    def __init__(self, ip, username, password):
        """
        The constructor for DeviceConnection class.
        :param ip: The ip address of the target device.
        :param username: The username of the target device for the SSH connection.
        :param password: The password of the target device for the SSH connection.
        """
        self.ip = ip
        self.username = username
        self.password = password
        self.client = None

    def connect(self, priv_exec_pass) -> None:
        """
        Method that establishes the SSH connection to the device.
        :param priv_exec_pass: The password used to access the privileged exec mode of the target device.
        :return:
        """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username=self.username, password=self.password)
        self.client.exec_command(f'ena\n{priv_exec_pass}\nconf t\n')

    def send_command(self, command):
        """
        Method that sends the command to the device.
        :param command: The command to send to the device.
        :return:
        """
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self) -> None:
        """
        Method that closes the SSH connection.
        :return:
        """
        if self.client:
            self.client.close()
