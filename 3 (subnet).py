def convert_to_binary(num):
    return f"{num:08b}"

print("This assignment decodes a class C IP address")

# Input and split IP address
ip_address = input("Enter the initial IP (192.B.C.D format): ")
sections = list(map(int, ip_address.split('.')))

# Display IP address in binary format
print("The IP address in bits format is:", ".".join(convert_to_binary(s) for s in sections))

# Subnet mask calculation
cidr = int(input("Enter the CIDR bits (a number between 24 to 31): "))
subnet_mask = [255, 255, 255, (2 ** (cidr - 24) - 1) << (8 - (cidr - 24))]
print("\nSubnet mask in numeric format:", ".".join(map(str, subnet_mask)))
print("Subnet mask in bitwise format:", ",".join(convert_to_binary(s) for s in subnet_mask), "\n")

# Calculate network, broadcast, first, and last IPs
network_ip = sections[:3] + [sections[3] & subnet_mask[3]]
broadcast_ip = sections[:3] + [sections[3] | (255 - subnet_mask[3])]

print("Network address in numeric format:", ".".join(map(str, network_ip)))
print("\nBroadcast address in numeric format:", ".".join(map(str, broadcast_ip)))

if broadcast_ip[3] - network_ip[3] > 1:
    print("First address:", ".".join(map(str, network_ip[:3] + [network_ip[3] + 1])))
    print("Last address:", ".".join(map(str, broadcast_ip[:3] + [broadcast_ip[3] - 1])))
else:
    print("No usable address in this subnet")

# Check connectivity with another client IP
while True:
    other_ip = input("\nEnter another IP (192.B.C.D format) or '1' to exit: ")
    if other_ip == '1':
        break

    other_sections = list(map(int, other_ip.split('.')))
    if sections[:3] != other_sections[:3]:
        print("Clients not in the same network")
    elif network_ip[3] <= other_sections[3] <= broadcast_ip[3]:
        print("Clients are in the same subnet! Connectivity can be established!")
    else:
        print("Clients are in the same network but different subnets, connectivity cannot be established.")