"""
Module responsible for router configurations.
"""
from Connection import DeviceConnection


class Router:
    def __init__(self, name, ip, username, password, priv_exec_pass):
        """
        The constructor for the Router class.
        :param name: The name of the router.
        :param ip: The IP address of the router.
        :param username: The username of the router.
        :param password: The password of the router.
        :param priv_exec_pass: The password for the privileged exec mode of the router.
        """
        self.name = name
        self.connection = DeviceConnection(ip, username, password)
        self.priv_exec_pass = priv_exec_pass

    def config_RipV2(self):
        """
        Method for configuring RipV2 on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        network_1 = input("Enter the ip address of the first network: ")
        network_2 = input("Enter the ip address of the second network: ")
        stdout, stderr = self.connection.send_command(f'router rip\nversion 2\nno auto-summary\nnetwork {network_1}\nnetwork {network_2}')
        self.connection.close()

    def config_Subinterface(self):
        """
        Method for configuring a Sub-interface for a vlan on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)

        stdout, stderr = self.connection.send_command('config subinterface command')
        self.connection.close()

    def setup_DHCP(self):
        """
        Method for configuring DHCP services on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('dhcp command')
        self.connection.close()

    def config_HSRP(self):
        """
        Method for configuring HSRP on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('stp command')
        self.connection.close()
