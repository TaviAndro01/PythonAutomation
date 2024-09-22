"""
Module responsible for switch configurations.
"""
from Connection import DeviceConnection


class Switch:
    """
    Class tasked with encasing methods related to switch configuration.
    """
    def __init__(self, name, ip, username, password, priv_exec_pass):
        self.name = name
        self.connection = DeviceConnection(ip, username, password)
        self.priv_exec_pass = priv_exec_pass

    def configure_port_channel(self):
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config port-channel command')
        self.connection.close()

    def apply_security(self):
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config security command')
        self.connection.close()
