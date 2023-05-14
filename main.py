from InternetTools import Speed
from InternetTools import IpChecker
from colorama import Fore
from colorama import Style
from InternetTools import PortChecker
from InternetTools import DnsChecker


def do_speedtest():
    test = Speed()
    print("Please wait...")
    print("Server location:", )
    for key, value in test.get_test_info():
        print(key, ' : ', value)

    print()

    print(f"Ping:{Fore.LIGHTGREEN_EX}", round(test.check_ping()), f"ms {Style.RESET_ALL}")
    print(f"Download speed:{Fore.LIGHTGREEN_EX}", + round(test.check_download(), 2), f"Mbps{Style.RESET_ALL}")
    print(f"Upload speed: {Fore.LIGHTGREEN_EX}", round(test.check_upload(), 2), f"Mbps{Style.RESET_ALL}")


def check_port():
    port_checker = PortChecker()
    print("Write the port number:")
    port = int(input())
    if port_checker.port_check(port):
        print(f"{Fore.LIGHTGREEN_EX}", port, f"is open.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}", port, f"is closed.{Style.RESET_ALL}")


def resolve_dns_name():
    name = input()
    dns_checker = DnsChecker()
    print(f"{Fore.LIGHTGREEN_EX}Name", name, "is resolved to an IP", dns_checker.resolve_name_to_ip(name),
          f"{Style.RESET_ALL}")


def resolve_ip():
    ip_address = input()
    dns_checker = DnsChecker
    print(f"{Fore.LIGHTGREEN_EX}Ip address", ip_address, "is resolved to a name",
          dns_checker.resolve_ip_to_name(ip_address), f"{Style.RESET_ALL}")

def get_public_ip_address():
    print(f"{Fore.LIGHTGREEN_EX}", IpChecker.get_public_ip_address(), f"{Style.RESET_ALL}")


def show_menu():
    print("Network tools")
    print()
    print("Select an option:")
    print("1. Network speedtest (Download, Upload, Ping)")
    print("2. Show IP addresses")
    print("3. Show public IP address ")
    print("4. Check is the port open")
    print("5. Resolve DNS name to an IP address")
    print("6. Resolve IP address to a name")
    print()


while True:
    show_menu()
    option = int(input())
    match option:
        case 1:
            do_speedtest()
        case 2:
            IpChecker.get_ip_addresses()
        case 3:
            get_public_ip_address()
        case 4:
            check_port()
        case 5:
            resolve_dns_name()
        case 6:
            resolve_ip()
        case _:
            print("Wrong option, try again.")
