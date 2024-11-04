import socket
import ipaddress

def get_ip_from_url(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        return f"Error: {e}"

def get_url_from_ip(ip_address):
    try:
        # Check if the IP address is private
        if ipaddress.ip_address(ip_address).is_private:
            return "The provided IP address is a private IP and cannot be resolved to a public URL."
        
        url = socket.gethostbyaddr(ip_address)[0]
        return url
    except (socket.herror, ValueError):
        return "Invalid IP address or unable to resolve URL."

def dns_lookup_menu():
    while True:
        print("\nDNS Lookup Menu")
        print("1. Get IP address from URL")
        print("2. Get URL from IP address")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            url = input("Enter the URL: ")
            ip_address = get_ip_from_url(url)
            print(f"IP Address: {ip_address}")
        elif choice == '2':
            ip_address = input("Enter the IP address: ")
            url = get_url_from_ip(ip_address)
            print(f"URL: {url}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the DNS lookup menu
dns_lookup_menu()
