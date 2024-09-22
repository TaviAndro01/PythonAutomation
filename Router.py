"""
Module responsible for router configurations.
"""
from Connection import DeviceConnection


class Router:
    def __init__(self, name, ip, username, password, priv_exec_pass):
        self.name = name
        self.connection = DeviceConnection(ip, username, password)
        self.priv_exec_pass = priv_exec_pass

    def config_rip2(self):
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config rip2 command')
        self.connection.close()

    def setup_routes(self):
        self.connection.connect(self.priv_exec_pass)
        stdout, stderr = self.connection.send_command('config static route command')
        self.connection.close()
