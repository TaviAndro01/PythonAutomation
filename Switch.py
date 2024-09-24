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
        :param priv_exec_pass: The password for the privileged exec mode of the switch.
        """
        self.name = name
        self.connection = DeviceConnection(ip, username, password)
        self.priv_exec_pass = priv_exec_pass

    def config_Security(self):
        """
        Method for configuring the security on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        interface = input("Please enter the name of the interface you want to apply security to: ")
        vlan = input("Please enter the name of the VLAN you want to be allowed to pass: ")
        stdout, stderr = self.connection.send_command(f'int {interface}\nswitchport mode access\nswitchport access vlan {vlan}\nswitchport port security')
        self.connection.close()

    def config_STP(self):
        """
        Method for configuring the STP on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        primary_vlan = input("Please enter the ID of the VLAN you want to be set as primary on this switch (enter q if you do not want to set a primary vlan): ")
        seccondary_vlan = input("Please enter the ID of the VLAN you want to set as secondary on this switch (enter q if you do not want to set a secondary vlan): ")

        if primary_vlan != 'q' and seccondary_vlan != 'q':
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {primary_vlan} root primary\nspanning-tree vlan {seccondary_vlan} root secondary')
        elif primary_vlan != 'q' and seccondary_vlan == 'q':
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {primary_vlan} root primary')
        elif primary_vlan == 'q' and seccondary_vlan != 'q':
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {seccondary_vlan} root secondary')
        else:
            return ValueError("The Vlan names should be numbers.")
        self.connection.close()

    def config_HSRP(self):
        """
        Method for configuring HSRP on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('')
        self.connection.close()

    def config_Vlan(self):
        self.connection.connect(self.priv_exec_pass)
        vlan_ID = input("Please enter the ID of the VLAN you want to be created: ")
        vlan_NAME = input("Please enter the name of the VLAN you want to create: ")
        stdout, stderr = self.connection.send_command(f'vlan {vlan_ID}\n{vlan_NAME}')
        self.connection.close()
