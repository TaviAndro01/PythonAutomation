"""
Module responsible for switch configurations.
"""
from Device import Device


class Switch(Device):
    """
    Class tasked with encasing methods related to switch configuration.
    """

    def config_Security(self):
        """
        Method for configuring the security on a switch.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        interface = input("Please enter the name of the interface you want to apply security to: ")
        vlan = input("Please enter the name of the VLAN you want to be allowed to pass: ")
        stdout, stderr = self.connection.send_command(f'int {interface}\nswitchport port-security\nswitchport mode access\nswitchport access vlan {vlan}\nspanning-tree bpdu guard enable\n')
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
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {primary_vlan} root primary\nspanning-tree vlan {seccondary_vlan} root secondary\n')
        elif primary_vlan != 'q' and seccondary_vlan == 'q':
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {primary_vlan} root primary\n')
        elif primary_vlan == 'q' and seccondary_vlan != 'q':
            stdout, stderr = self.connection.send_command(f'spanning-tree mode rapid-pvst\nspanning-tree vlan {seccondary_vlan} root secondary\n')
        else:
            return ValueError("The Vlan names should be numbers.")
        self.connection.close()

    def config_Vlan(self):
        self.connection.connect(self.priv_exec_pass)
        vlan_id = input("Please enter the ID of the VLAN you want to be created: ")
        vlan_name = input("Please enter the name of the VLAN you want to create: ")
        stdout, stderr = self.connection.send_command(f'vlan {vlan_id}\nname {vlan_name}\n')
        self.connection.close()
