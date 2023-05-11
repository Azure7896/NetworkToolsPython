import speedtest as st
import os
import requests


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


class IpChecker:

    def __init__(self):
        pass

    @classmethod
    def get_ip_addresses(cls):
        return os.system("ipconfig")

    @classmethod
    def get_public_ip_address(cls):
        return str(requests.get('https://checkip.amazonaws.com').text.strip())
