from InternetTools import Speed
from InternetTools import IpChecker
from colorama import Fore
from colorama import Style


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


def show_menu():
    print("Network tools")
    print()
    print("Select an option:")
    print("1. Internet speedtest (Pobieranie, Wysyłanie, Ping)")
    print("2. Show IP addresses")
    print("3. Show public IP address ")
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
            print(f"{Fore.LIGHTGREEN_EX}", IpChecker.get_public_ip_address(), f"{Style.RESET_ALL}")
        case _:
            print("Wrong option, try again.")
