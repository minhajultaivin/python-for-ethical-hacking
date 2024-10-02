import pyfiglet
import socket
from termcolor import colored

print(colored("<===========***Domain To IP Converter***=============>", 'red'))
print(colored("<===========***Created by TAIVIN***=============>", 'blue'))

banner=colored(pyfiglet.figlet_format("IP Converter"), 'blue')

print(banner)

Domain_name = input("Enter The Domain :")

ip= socket.gethostbyname(Domain_name)

print("IP for {} : {}".format(Domain_name,ip) )