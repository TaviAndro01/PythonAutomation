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
        self.ip = ip
        self.username = username
        self.password = password
        self.client = None

    def connect(self, priv_exec_pass):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username=self.username, password=self.password)
        self.client.exec_command(f'ena\n{priv_exec_pass}\nconf t')

    def send_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        if self.client:
            self.client.close()
