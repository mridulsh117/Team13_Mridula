import os 
import netifaces #Module to list network interfaces on local machine

class SystemOperations:
    @staticmethod
    def display_ipconfig():
        #Function to display the system IP address
        try:
            interfaces = netifaces.interfaces()
            for interface in interfaces: #loop to iterate through each network interface available on system
                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses: #Condition to check if current interface has IPv4 address
                    for addr in addresses[netifaces.AF_INET]: 
                        print(f"Interface: {interface}, IP Address: {addr['addr']}")
        except Exception as e:
            print(f"An error occurred while retrieving network information: {e}")

    @staticmethod
    def display_pwd():
        # Function to display the present working directory
        try:
            print(os.getcwd())
        except Exception as e:
            print(f"An error occurred while retrieving the current directory: {e}")

    @staticmethod
    def clear_screen():
        # Function to clear the terminal screen
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"An error occurred while trying to clear the screen: {e}")
