from colorama import Fore
from colorama import Style

from NetworkTools import Dns
from NetworkTools import Ip
from NetworkTools import Port
from NetworkTools import Speed
from NetworkTools import Tracert
from NetworkTools import Location


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
    port_checker = Port()
    print("Write the port number:")
    port = int(input())
    if port_checker.port_check(port):
        print(f"{Fore.LIGHTGREEN_EX}", port, f"is open.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}", port, f"is closed.{Style.RESET_ALL}")


def resolve_dns_name():
    name = input()
    dns_checker = Dns
    print(f"{Fore.LIGHTGREEN_EX}Name", name, "is resolved to an IP", dns_checker.resolve_name_to_ip(name),
          f"{Style.RESET_ALL}")


def resolve_ip():
    ip_address = input()
    dns_checker = Dns
    print(f"{Fore.LIGHTGREEN_EX}Ip address", ip_address, "is resolved to a name",
          dns_checker.resolve_ip_to_name(ip_address), f"{Style.RESET_ALL}")


def get_public_ip_address():
    print(f"{Fore.LIGHTGREEN_EX}", Ip.get_public_ip_address(), f"{Style.RESET_ALL}")


def get_destination_trace_route():
    print("Traceroute. Write domain name or IP address:")
    destination = input()
    tracert = Tracert()
    tracert.trace(destination)


def get_location():
    name = input()
    location_info = Location().print_details(name)
    print(f"{Fore.LIGHTGREEN_EX}IP Address: {location_info.ip_address}")
    print(f"Location: {location_info.city}, {location_info.region}, {location_info.country}")
    print(f"Coordinates: (Lat: {location_info.latitude}, Lng: {location_info.longitude}){Style.RESET_ALL}")

def do_ip_renew():
    Ip.ip_renew()


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
    print("7. Tracert")
    print("8. Check server location")
    print("9. Show route print")
    print("10. Netstat")
    print ("11. Renew IP address")
    print()


while True:
    show_menu()
    option = int(input())
    match option:
        case 1:
            do_speedtest()
        case 2:
            Ip.get_ip_addresses()
        case 3:
            get_public_ip_address()
        case 4:
            check_port()
        case 5:
            resolve_dns_name()
        case 6:
            resolve_ip()
        case 7:
            get_destination_trace_route()
        case 8:
            get_location()
        case 9:
            Ip.get_route()
        case 10:
            Ip.netstat()
        case 11:
            do_ip_renew()
        case _:
            print("Wrong option, try again.")
