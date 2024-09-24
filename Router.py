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
        redistrib = input("Do you want to redistribute the static routes from this device? (y/n): ")

        if redistrib.lower() == "y":
            redistributed = True
        elif redistrib.lower() == "n":
            redistributed = False
        else:
            print("You entered an invalid option. The router will not redistribute it's static routes.")
            redstributed = False

        if redistributed is False:
            stdout, stderr = self.connection.send_command(f'router rip\nversion 2\nno auto-summary\nnetwork {network_1}\nnetwork {network_2}\n')
        elif redistributed is True:
            stdout, stderr = self.connection.send_command(f'router rip\nversion 2\nno auto-summary\nnetwork {network_1}\nnetwork {network_2}\nredistribute static\n')
        self.connection.close()

    def config_HSRP(self):
        """
        Method for configuring a Sub-interface for a vlan on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        interface = input("Enter the ID of the interface: ")
        standby_id = input("Enter the ID of the standby interface: ")
        vrouter_ip = input("Enter the IP address of the Virtual Router: ")
        priority = input("Enter the priority of the physical interface (no if you would like to keep default priority - 100): ")
        if priority == "no":
            priority = "100"
        stdout, stderr = self.connection.send_command(f'int {interface}\nstandby {standby_id} ip {vrouter_ip}\nstandby {standby_id} priority {priority}\nstandby {standby_id} preempt\n')
        self.connection.close()

    def setup_DHCP(self, ip):
        """
        Method for configuring DHCP services on a Router.
        :return:
        """
        self.connection.connect(self.priv_exec_pass)
        ip_base = '.'.join(ip.split('.')[:3])
        lan_id = input("Enter the ID of the LAN: ")
        ip_pool = input("Enter the IP address of the DHCP pool: ")
        subnet_mask = input("Enter the subnet mask: ")
        switch_nr = int(input("Enter the number of switches in the lan: "))
        router_nr = int(input("Enter the number of routers in the lan: "))
        last_addr_b = router_nr + 1
        first_addr_e = 255 - switch_nr
        stdout, stderr = self.connection.send_command(
            f'ip dhcp pool LAN{lan_id}\nnetwork {ip_pool} {subnet_mask}\ndefault router {ip}\ndns-server 8.8.8.8\nexit\nip dhcp excluded-address {ip_base}.1 {ip_base}.{last_addr_b}\nip dhcp excluded-address {ip_base}.{first_addr_e} {ip_base}.254\n'
        )
        self.connection.close()
