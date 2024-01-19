from ping3 import ping
import ipaddress

import time
import threading


# Determine if you can reach a singlular host
def check_single_host(ip, available_hosts, timeout=1):
    # IP returns IPv4-Address, so I need it to be a string instead.
    ip_str = str(ip)

    # Backup message incase failure. I leave it here for testing...
    message = f"Failed to reach {ip_str}"

    # Obtain the response time in seconds.
    response_time = ping(ip_str, timeout)

    # For some reason (despite documentation), response can be True, False or some value.
    # The value (in seconds) is what I want.
    if response_time is not None and response_time is not False:
        message = f"{ip_str} is reachable @ {response_time} seconds."

        # Obtain the ip-address from the message above
        addr = message.split(" ")

        # If the new address doesn't exist in the list, add it in.
        if addr[0] not in available_hosts:
            available_hosts.append(addr[0])

            # This is just to have a visual representation of what is happening.
            print(f"This is an available host: {addr[0]} - Size: {len(available_hosts)}")
            print(len(available_hosts))


def pingsweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    available_hosts = []
    threads = []

    for ip in network.hosts():
        # Check a single host
        thread = threading.Thread(target=check_single_host, args=(ip, available_hosts))
        # Add it to the thread list
        threads.append(thread)
        # Start threading
        thread.start()

    return available_hosts


# Very basic file output.
def write_ips(fileName, data):
    with open(fileName, 'a') as f:
        for d in data:
            abc = d + "\n"
            f.writelines(abc)


# Very basic file output.
def write_file(fileName, data):
    with open(fileName, 'a') as f:
        abc = data + "\n"
        f.writelines(abc)


# Displays overall stats of what the program found.
def display_summary(num_of_hosts, s, data):
    # Modify the subnet string, so it doesn't contain ../24..
    name = subnet.split("/")
    fileName = f"IP-ADDRESS-{name[0]}.txt"

    difference = 255 - num_of_hosts

    statement_1 = f"The subnet tested: {s}."
    statement_2 = f"The number of valid IPs discovered: {num_of_hosts}."
    statement_3 = f"The number of hosts left: {difference}"

    write_file(fileName, statement_1)
    write_file(fileName, statement_2)
    write_file(fileName, statement_3)

    # Maybe it is just my computer, but without a timer ips don't get written properly.
    time.sleep(1)

    write_ips(fileName, sorted(data))


if __name__ == "__main__":
    subnet = "192.168.1.0/24"
    addr = pingsweep(subnet)
    number_of_available_hosts = len(addr)
    display_summary(number_of_available_hosts, subnet, addr)
