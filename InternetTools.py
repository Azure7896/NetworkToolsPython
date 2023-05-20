import os
import socket

import requests
import speedtest as st
from ip2geotools.databases.noncommercial import DbIpCity


class Speed:
    server = st.Speedtest()
    jsonTestInfo = server.get_best_server()

    def __init__(self):
        pass

    @classmethod
    def get_test_info(cls):
        return Speed.jsonTestInfo.items()

    @classmethod
    def check_download(cls):
        down = Speed.server.download()
        down = down / 1000000
        return down

    @classmethod
    def check_upload(cls):
        upload = Speed.server.upload()
        upload = upload / 1000000
        return upload

    @classmethod
    def check_ping(cls):
        ping = Speed.server.results.ping
        return ping


class Ip:

    def __init__(self):
        pass

    @classmethod
    def get_ip_addresses(cls):
        return os.system("ipconfig")

    @classmethod
    def get_public_ip_address(cls):
        return str(requests.get('https://checkip.amazonaws.com').text.strip())

    @classmethod
    def get_route(cls):
        return os.system("route PRINT")


class Port:

    def __init__(self):
        pass

    @classmethod
    def port_check(cls, port_number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect(("127.0.0.1", port_number))
            return True
        except:
            return False


class Dns:

    def __init__(self):
        pass

    @classmethod
    def resolve_name_to_ip(cls, name):
        return socket.gethostbyname(name)

    @classmethod
    def resolve_ip_to_name(cls, ip_address):
        return socket.gethostbyaddr(ip_address)


class Tracert:

    def __init__(self):
        pass

    @classmethod
    def trace(cls, destination):
        command = "tracert " + destination
        return os.system(command)


class Location:

    def __init__(self):
        pass

    @classmethod
    def print_details(csl, name):
        ip = DnsResolver.resolve_name_to_ip(name)
        location_info = DbIpCity.get(ip, api_key="free")
        return location_info
