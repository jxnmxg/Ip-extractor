import re

file_path = input("Please enter the path to the file you'd like to filter for IP addresses: ")
document = input("Would you like a .txt of the ips? (y/n):")
with open(file_path, "r") as file:
    data = file.read()

def valid_ip(ip):
    parts = ip.split('.')
    return all(0 <= int(part) <=255 for part in parts)

ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
potential_ips = re.findall(ip_pattern, data)
valid_ips = [ip for ip in potential_ips if valid_ip(ip)]

print("Filtered IP addresses:")
for ip in valid_ips:
    print(ip)

if document == "y" or  document == "Y":
    with open("filtered_ips.txt", "w") as output_file:
        for ip in valid_ips:
            output_file.write(ip + "\n")
    
else:
    print("No file created.")
