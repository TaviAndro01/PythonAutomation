"""
Module responsible for switch configurations.
"""
from Connection import DeviceConnection


class Switch:
    """
    Class tasked with encasing methods related to switch configuration.
    """
    def __init__(self, name, ip, username, password, priv_exec_pass):
        """
        The constructor for the Switch class.
        :param name: The name of the switch.
        :param ip: The IP address of the switch.
        :param username: The username of the switch.
        :param password: The password of the switch.
        :param priv_exec_pass: The password for the priviledged exec mode of the switch.
        """
        self.name = name
        self.connection = DeviceConnection(ip, username, password)
        self.priv_exec_pass = priv_exec_pass

    def config_PortChannel(self):
        """
        Method for configuring a port channel switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config port-channel command')
        self.connection.close()

    def config_Security(self):
        """
        Method for configuring the security on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config security command')
        self.connection.close()

    def config_STP(self):
        """
        Method for configuring the STP on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config stp command')
        self.connection.close()

    def config_HSRP(self):
        """
        Method for configuring HSRP on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config hsrp command')
        self.connection.close()

    def config_Vlan(self):
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config vlan command')
        self.connection.close()
