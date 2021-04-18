# Чему равняется FCS кадра "нового" Ethernet, содержащего ARP запрос от хоста c
# IP = 199.36.16.249 и MAC = 4A:BC:11:2A:2E:4B,
# интересующегося MAC-адресом хоста с
# IP = 31.254.120.54 и MAC = 6A:8B:1A:4F:22:84.

from binascii import hexlify

from scapy.all import *
from scapy.layers.l2 import ARP, Ether

# Для бинаризации

dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"

}

""" Дано: """

_psrc = "199.36.16.249"
_hwsrc = "4A:BC:11:2A:2E:4B"
_pdst = "31.254.120.54"
# Мак дист нам не нужен

ether = Ether()
ether.src = _hwsrc
ether.dst = "ff:ff:ff:ff:ff:ff"

# Отправка пакета:

arp = ARP(op="who-has",
          hwlen=6,
          plen=4,
          psrc=_psrc,
          hwsrc=_hwsrc,
          pdst=_pdst,
          )

packet_to_send = ether / arp
pad_len = 60 - len(packet_to_send)
pad = Padding()
pad.load = '\x00' * pad_len
packet_to_send = packet_to_send / pad
res = hexlify(bytes(packet_to_send[0]))
res = str(res)[2:-1]

sendp(packet_to_send, verbose=0)
pkt = sniff(count=1)[0]

res1 = ""
for sym in res:
    res1 += dict[sym]

degree = 32


# Расчёт CRC

def crc(polynom_bin, message_bin, type=1):
    registr = []
    # 1. Создаётся массив (регистр), заполненный нулями, равный по длине разрядности (степени) полинома.
    for _ in range(degree):
        registr.append(0)
    # Исходное сообщение дополняется нулями в младших разрядах, в количестве, равном числу разрядов полинома.
    message_bin += "0" * degree
    # Инверсия первых битов
    message_bin = "0" * 32 + message_bin[32:]
    # message_bin += "00011001000101000100010011110010"
    for bit in message_bin:
        # В млаший разряд регистра заносится один старший бит сообщения,
        # а из старшего разряда регистра выдвигается один бит.
        shifted = registr[degree - 1]
        for i in range(degree - 1, 0, -1):
            registr[i] = registr[i - 1]
        registr[0] = int(bit)
        # Если выдвинутый бит равен "1", то производится инверсия битов
        # (операция XOR, исключающее ИЛИ) в тех разрядах регистра, которые соответствуют единицам в полиноме.
        if shifted == 1:
            for i in range(degree):
                registr[i] = registr[i] ^ int(polynom_bin[i])

    result = ""

    # Конечная инверсия
    registr = registr[::-1]

    if type == 2:
        """ Для поиска магического числа нам не нужна инверсия CRC """
        for r in registr:
            result += (str(r))
        digit = int(result, 2)
        return result, digit

    # Конечная инверсия
    ff = "1" * 32
    for i in range(degree):
        registr[i] = registr[i] ^ int(ff[i])

    for r in registr:
        result += (str(r))
    digit = int(result, 2)
    return result, digit


# Разделить строку на n

def splitStrByN(string, n):
    return [string[i:i + n] for i in range(0, len(string), n)]


def1 = splitStrByN(res1, 8)

p = ""

for d in def1:
    p += d[::-1]

poly = "101110100000110111000110011010111"

result = crc(poly[::-1], p)
print("FCS:", result[1])

# Для поиска Магического числа добавим в конец исходного пакета CRC и выполним те же действия,
# но также необходимо выполнить дополнительную инверсию CRC кода

n_message = p + result[0]
MAGIC = crc(poly[::-1], n_message, 2)
print("Magic number:", MAGIC[1])
