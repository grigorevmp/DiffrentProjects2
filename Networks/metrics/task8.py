""" Суперкомпьютер МИФИ-2018 """

""" Input data """

max_delay = 2.4789053356e-05   # sec
frame_size = 12439 * 8   # bit
address_size = 8 * 8   # bit
total_size = frame_size + address_size   # bit

bandwidth = 20 * (2 ** 30)  # bit per sec
# bandwidth_m = 4 * (10 ** 9)

store_and_forward_ports = 680
cut_through_ports = 40

time_for_message_sf = total_size / bandwidth    # sec
time_for_message_ct = address_size / bandwidth    # sec

print("Calculated ata")
print(f"--- frame_size: {frame_size}")
print(f"--- address_size: {address_size}")
print(f"--- total_size: {total_size}")
print(f"--- bandwidth: {bandwidth}")
print(f"--- time_for_message_sf: {time_for_message_sf}")
print(f"--- time_for_message_ct: {time_for_message_ct}")
print("")

""" Find number of nodes
    In common case num of nodes = 2 * (ports/2) ^ level of tree,
    but there is maximum value (defined by address size): """

max_nodes = 2 ** address_size

""" Find level of the Fat tree
    level of tree = max_delay divided by 2 (up and down) * message sending time"""

""" Bisco """

Bisco_level_f = max_delay / (2 * time_for_message_sf)
print(f"Bisco level (o(1): {Bisco_level_f}")

Bisco_level = 0
left_delay = max_delay
while left_delay > 0:
    Bisco_level += 1
    left_delay = max_delay - 2 * Bisco_level * time_for_message_sf    # sec
    # print(f"{Bisco_level} - {left_delay}")

print(f"Bisco level: {Bisco_level - 1}")

try:
    max_Bisco_nodes = 2*((store_and_forward_ports / 2)**(Bisco_level - 1))
    if max_Bisco_nodes > max_nodes:
        print(f"Bisco nodes: {max_nodes}")
    else:
        print(f"Bisco nodes: {max_Bisco_nodes}")
except OverflowError:
    print(f"Bisco nodes: {max_nodes}")

""" Crocade """

Crocade_level_f = (max_delay - frame_size/bandwidth )/ (2 * time_for_message_ct)
print(f"Crocade level (o(1): {Crocade_level_f}")

""" #FIXME 
For cut-through we just use address fow any node and time for sending message for 1 node"""

Crocade_level = 0
left_delay = max_delay
while left_delay > 0:
    Crocade_level += 1
    left_delay = max_delay - 2 * Crocade_level * time_for_message_ct - frame_size/bandwidth   # sec
    # print(f"{Crocade_level} - {left_delay}")

print(f"Crocade level: {Crocade_level - 1}")
try:
    max_Crocade_level = 2*((cut_through_ports / 2)**(Crocade_level - 1))
    if Crocade_level > max_nodes:
        print(f"Bisco nodes: {max_nodes} - overflow detected")
    else:
        print(f"Crocade nodes: {max_Crocade_level}")
except OverflowError:
    print(f"Crocade nodes: {max_nodes} - overflow detected")

