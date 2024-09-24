"""
Module responsible for router configurations.
"""
from Device import Device


class Router(Device):

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
