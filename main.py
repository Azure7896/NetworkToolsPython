from InternetTools import SpeedTests
from colorama import Fore
from colorama import Style
import os


def do_speedtest():
    test = SpeedTests()
    print("Proszę czekać, trwa wykonywanie testu...")
    print("Lokalizacja serwera", )
    for key, value in test.get_test_info():
        print(key, ' : ', value)

    print()

    print(f"Ping:{Fore.LIGHTGREEN_EX}", round(test.checkPing()), f"ms {Style.RESET_ALL}")
    print(f"Prędkość pobierania:{Fore.LIGHTGREEN_EX}", + round(test.checkDownload(), 2), f"Mbps{Style.RESET_ALL}")
    print(f"Prędkość wysyłania:{Fore.LIGHTGREEN_EX}", round(test.checkUpload(), 2), f"Mbps{Style.RESET_ALL}")


def get_ip_addresses():
    print(os.system("ipconfig"))


print("Network tools")
print()
print("Wybierz odpowiednią opcję:")
print("1. Test internetu (Pobieranie, Wysyłanie, Ping)")
print("2. Wyświetl adresację IP")
print()

while (True):
    option = int(input())
    match option:
        case 1:
            do_speedtest()
        case 2:
            get_ip_addresses()
        case _:
            print("Wybrałeś błędną opcję, spróbuj ponownie.")

    "Wybierz kolejną opcję."
