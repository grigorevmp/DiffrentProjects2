from scapy.all import *
from scapy.layers.l2 import ARP, Ether
import random
import socket
import struct
import optparse
import psutil
import re


def check_ip(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def check_mac(mac):
    result = re.match(r"([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}$", mac)
    return result


def generate_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc


def send_ARP(_source, _destination, _count, _response, _gratuitous,
             _target_ip, _tell_ip, _target_ip_custom, _tell_ip_custom, interfaces):
    print()
    if interfaces == "all":
        interfaces = psutil.net_if_addrs()
        elem = []

        for k, v, in interfaces.items():
            # if v[0].address.find('-') == -1:
            if not check_mac(v[0].address):
                elem.append(k)
        for i in elem:
            print(i, " is not interface with correct address")
            del interfaces[i]

    if _target_ip_custom or _tell_ip_custom:
        for _ in range(_count):
            ether = Ether()
            ether.src = _source
            ether.dst = _destination
            op = "who-has"
            if _response:
                op = "is-at"
            if target_ip_custom:
                _target_ip = generate_random_ip()

            if _tell_ip_custom:
                _tell_ip = generate_random_ip()

            if _gratuitous:
                _target_ip = _tell_ip

            print(f"Source: {_tell_ip}, destination: {_target_ip}")
            arp = ARP(op=op,
                      psrc=_tell_ip,
                      pdst=_target_ip)

            packet_to_send = ether / arp
            try:
                if isinstance(interfaces, dict):
                    for interface in interfaces:
                        sendp(packet_to_send, iface=interface, count=1, verbose=0)
                else:
                    sendp(packet_to_send, iface=interfaces, count=1, verbose=0)
            except ValueError as e:
                print(e)
        print(f"{_count} packets has been sent")
    else:
        ether = Ether()
        ether.src = _source
        ether.dst = _destination
        op = "who-has"
        if _response:
            op = "is-at"

        if _gratuitous:
            _target_ip = _tell_ip

        print(f"Source: {_tell_ip}, destination: {_target_ip}")
        arp = ARP(op=op,
                  psrc=_tell_ip,
                  hwsrc=get_mac(_tell_ip),
                  pdst=_target_ip,
                  hwdst=get_mac(_target_ip))
        packet_to_send = ether / arp
        try:
            if isinstance(interfaces, dict):
                for interface in interfaces:
                    sendp(packet_to_send, iface=interface, count=_count, verbose=0)
                print(f"{_count} packets has been sent")
            else:
                sendp(packet_to_send, iface=interfaces, count=_count, verbose=0)
                print(f"{_count} packets has been sent")
        except ValueError as e:
            print(e)


if __name__ == "__main__":

    parser = optparse.OptionParser()
    # parser.add_option('--res', '--response', action='store_true', dest='response',
    #                   help='flood response')

    parser.add_option('--t', '--type', action='store', dest='type',
                      help='[response (default), request] - type of sending packet', default='request')
    parser.add_option('--n', '--num', action='store', dest='number',
                      help='number of sending packets', default='1')
    parser.add_option('--gr', '--gratuitous', action='store_true', dest='gratuitous',
                      help='gratuitous arp sending')
    parser.add_option('--tara', '--target_arp', action='store', dest='target_arp',
                      help='target arp packet ip or [random (default)]', default='random')
    parser.add_option('--srca', '--source_arp', action='store', dest='source_arp',
                      help='source arp packet ip or [random (default)]', default='random')
    parser.add_option('--dst', '--destination', action='store', dest='destination',
                      help='target mac or broadcast (default)', default='ff:ff:ff:ff:ff:ff')
    parser.add_option('--src', '--source', action='store', dest='source',
                      help='source mac, your mac by default', default=Ether().src)
    parser.add_option('--i', '--interface', action='store', dest='interface',
                      help='interface to send packets', default="all")
    options, args = parser.parse_args()

    Problem = False

    print(f"// Packets type: {options.type}")
    print(f"// Packets number: {options.number}")
    print(f"// Gratuitous mode: {options.gratuitous}")
    print(f"// Source mac: {options.source}")
    print(f"// Target mac: {options.destination}")
    print(f"// Source arp packet ip: {options.source_arp}")
    print(f"// Target arp packet ip: {options.target_arp}")
    print(f"// Interface: {options.interface}")

    # Input info

    tell_ip = "10.52.4.14"
    tell_ip_custom = False
    if check_ip(options.source_arp) or options.source_arp == "random":
        if options.source_arp == "random":
            tell_ip_custom = True
        tell_ip = options.source_arp

    target_ip = "10.52.4.1"
    target_ip_custom = False
    if check_ip(options.target_arp) or options.target_arp == "random":
        if options.target_arp == "random":
            target_ip_custom = True
        target_ip = options.target_arp

    source = Ether().src
    if check_mac(options.source):
        source = options.source
    else:
        Problem = True

    destination = "ff:ff:ff:ff:ff:ff"
    if check_mac(options.destination):
        destination = options.destination
    else:
        Problem = True

    gratuitous = options.gratuitous

    count = 1
    if int(options.number) > 0:
        count = int(options.number)
    else:
        Problem = True

    response = False
    if options.type == "request":
        response = False
    elif options.type == "response":
        response = True
    else:
        Problem = True

    if not Problem:
        send_ARP(source, destination, count, response, gratuitous,
                 target_ip, tell_ip, target_ip_custom, tell_ip_custom, options.interface)
    else:
        print("--- Wrong arguments ---")
