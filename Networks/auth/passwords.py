# MD5 от конкатенации кода сообщения, идентификатора, длины сообщения, случайной последовательности,
# полученной сервером в пункте 1 (Request Athenticator), атрибутов передаваемых в данном пакете и разделяемого секрета.

# MD5(CODE, ID, LENGTH, RA, Attr, SECRET)

import hashlib
import binascii
import itertools

# given
hex_digits = ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46']  # 0-F
maxLen = 6

# from WS

CODE = "02"  # AA CODE 02
ID = "59"  # AA ID
LENGTH = "0052"  # AA LENGTH
RA = "3a9e97f30209f0965a9208e5298620d7"  # AR 2 Auth <CAN BE BRUTEFORCED (for task3)>
# AA : attribute Value pairs
Attr = "0606000000024f060302000419203f0305080000013700017f00000101c1923e5a3cf3fa00000000000000395012d" \
       "4474c006865ad0911f6f1b3b7407b96 "
# AA
ACCEPT = "ee19ca53f926c718b4a08b3922e85bfd"

stringToHash = CODE + ID + LENGTH + RA + Attr

for secret in itertools.chain.from_iterable((''.join(line)
                                             for line in itertools.product(hex_digits, repeat=i))
                                            # составляет комбинации
                                            # всех hex_digits длинной i с повторами
                                            for i in range(1, maxLen + 1)):  # Password length up to 6
    check = stringToHash + secret
    if hashlib.md5(binascii.unhexlify(check)).hexdigest() == ACCEPT:
        print("Shared secret was", binascii.unhexlify(secret))
        break

ID = "02"
eap_md5_value = "e014c19009c6c4f5283d251f5192c101"  # REQUEST - SUCCESS
eap_md5_value_response = "995ac55ec9b14e9bbfab2f78b4dd5888"  # RESPONSE - SUCCESS

for password in itertools.chain.from_iterable((''.join(line)
                                               for line in itertools.product(hex_digits, repeat=i))  # составляет
                                              # комбинации всех hex_digits длинной i с повторами
                                              for i in range(1, maxLen + 1)):  # Password length up to 6
    check = ID + password + eap_md5_value
    if hashlib.md5(binascii.unhexlify(check)).hexdigest() == eap_md5_value_response:
        print("Password was", binascii.unhexlify(password))
        break
