import numpy
import matplotlib.pyplot as plt

text1 = "accdefghijklmnopqrstuvwabceegghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuvwabcdefghhkklmnopqrsttwwabcdefgihjjlmnopqrsttvwabcdefghikklmnopqrstuwwabbdefghijklmnnqqrstuwwabcddfghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnnpqrstuvwaccdefghijklmnopqrruuvwabcdefgihjklmnopqrsutvwabcdefghhjklmnopqrstuvwabcdefghhjklmnopqrsttvwabcdegfhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrstuvwabcdefghijkmmnopqrstuvw`cbdefghikklmonpqrstuwwabcdefghijjlmnopqrstuvvaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnnqprstuvwabbeefghijklmnoqqrsttvwabcdegfiijklmnopqssuuwwabcdeffhhjjlmnopprruuwv`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text2 = "`bbeefghijjlmnopqrstuvvabcdefghijkllnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuwwabceefghhjjlmnoqqrsutvwabcdefgihjjlmnopqrstuvvabcdefghijkmmoopqrstuwvabbeefghijjmmnoqprstuvv`bcdeffhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwaccedffhijklmnopprruuvwabcdegghijklmnopqrstuvwabcdefghhkklmnopqrsttwwabcdefghhjklmnopqsstuvwabcdegghijklmnopqrstuvwabcdefghijklmnopqrstuvvabcdefghikjmlnopqrstuvv`bcdefghijkllnopqrstuvwaccdefghijklmnopqrstuvwabceefghijjlmnopqrstuvvaccdefghijkmmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnoqprsuuvwabbdefghhjklmnoqqrrttvwabcddffhikklmnoppsstuvwabcddgghhjklmnopprsuuvw`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text3 = "acbdefghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjjlmooqqrstuvwabbddfgiijjllnopprstuvwacbdefghijjmmnnpqrstuvv`bceefghijklmnopprstuvv`bcdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwaccddffiijklmnopqrsuuvwabcdegghijklmnopqsstuvwabcdefghijklmnoqqrsutvwabcddfghhkjlmnoppsstuvvabcdeggiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhkjllnopqrsttvvabcdefghijkmmnopqrstuvv`cbdefghikkllonpqrstuwwabceefghijklmnoqqrstuvwaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefgiijklmnoqpssuuvwabbdefghijklmnoqqrrtuvwabcdeffhijklmnopqssuuvwabcddggihjklmnopqsruuvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text4 = "accdefghijjlmnnpqrstuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijkmmnopqrstuww`ccdefgihjkllnopqrstuvw`cbddfgiijjllonpprsuuwwabbdegghijjlmnopqsstuvwabcdefghijjllnopqrstuvv`ccdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwaccddfgiijklmoopqrstuvwabbdefghijklmnnpqsrtuvwabceefgiikklmnoqqrsuuwwabcdefghikjlmnopqsstuvwabcdeggihjklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrsttvwaccdefghhkklmoopqrsttwvabbdefghikjllnopqrstuvwacbdefghijklmonqqrstuvwacbeefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwabbddgfhijklmnoqqrrtuvwabcdeffihjklmnoqqrrutvwabcddfgihkjlmnopqsrttvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text5 = "abbdefghijjlmnopqrrtuvvabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjkmmnopqrstuvw`bcddfghikjlmnnpqrsuuwvabbeefghijkmlnnpqsstuvw`cceeffhijjllooqprrtuww`cbdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabcdegghijklmnnpqssuuvwabceeffhhjklmnoqqsrttvwabcddfgiikklmnopprstuvwabcdefghikklmnopqrstuwwabcdeggihjklmnopqrstuvwabcdefghijkllnopqrstuvw`ccdefghikkllnopqrsuuvwaccdefghhjklmnopqrstuvv`bcdefghijjmlnopqrstuvvaccdefghijkmmnopqrstuvw`ccdefghijklloopqrstuvwabcdefghijklmnopqrstuvwabcdeffhhjklmnopqsrtuvwabbdegfiijklmnoqqsruuvwabcedgfiijjlmnoqpssuuvwabcdegfhijjlmnopqrrtuvw`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text6 = "abcdefghijjlmnnpqrstuvvabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdeffihkjmmnnpqrstuwv`bcedfghikjmmnoqqrsuuvv`bcedfghhjkllnoqprsttwwabcddgfhikklmnoqpsrtuww`bcddffiijjlmnopqrstuvwabcdefghijklmnopqrrtuvwabcddgghijklmnoqprrtuvwabbdefgiijklmnnpqrsuuvwabcdefghijklmnopqssuuvwabcdeffihjklmnopqrsutvwabcdegghhjklmnopqrstuvwabcdefgihjklmnopqrstuvwabcdefghijklmnopqrrtuvwaccdefgiikjlmoopqrsuuvvabcdefghijkmmnopqrstuvw`bcdefghijkmmnopqrstuvv`bcdefghijkmlnnpqrstuvw`cceefghijkllnopqrstuvwabcdefghijklmnopprstuvwabcdegghhjklmnopqsstuvwabbedfghijklmnnqprstuvwabcedgghijjlmnopqrstuvwabcdefghijjlmnopqrstuvv`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text7 = "`ccdefghijklmnopqrrtuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwaccdeffihjjlmnopqrrutvv`bcdefgihjkllnopprsuuvwaccdegghikklmnopqsstuvwabcdefghijklmnopqrstuvwabcdeffhijklmnopqrstuvwabcdefghijklmnopqrrtuvwabcdeggiijklmnoqqsruuvwabbdeffhhjklmnopqrrtuvwabcdefgiijklmnopqrsuuvwabcdeffhijklmnopqrstuvwabcdegghijklmnopqssutvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmnopqrstuwwabbdefghijjlmnnpqrstuvvabcdefghijjmmoopqrstuvvabbeefghijklmnnqqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhjklmnopqrstuvwabbdefghhjklmnnpqrsttvwabcdefghikjlmnopqrstuwwabcdefghijjlmnopqrsttvvabcdefghijkllnopqrstuvwabcdefghijklmnopqr"
text8 = "abbdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwacceefghhjklmnoqqrsttvwabcddfghhjklmnopqrsttvwaccdefghikklmoopqrstuwwabbdefghijjlmnnpqrstuvvabcdeffhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabbeeffhhjklmnoqqrsttvwabcddfghijklmnopprstuvwabcdegghijklmnopqsrtuvwabcdeffiijklmnopqsruuvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmoopqrstuwwabcdefghijklmnnpqrstuvwacceefghijjlmonpqrstuvwabceefghijklmnopqrstuvwabbdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwabcdeffihjklmnoqprsuuvwabcdegghhjklmnopqsstuwwabcdeffhijjlmnopqrstuvwabcdefghijklmnopqrsttvvaccdefghijkllnopqrstuvwabcdefghijklmnopqr"

ideal_text = ('abcdefghijklmnopqrstuvw' * 28 + 'abcdefghijklmnopqr') * 8
import re


def transform_column(xor):
    str = ""
    for i in range(xor.shape[1]):
        number = 0
        j = 0
        for num in xor[:, i]:
            number += 2 ** (j) * int(num)
            j += 1
        # if number != 0:
        str += chr(number)
        # print(chr(number), end='')
    #res = re.sub(r'[^A-Za-z]', '', str)
    print(str)
    print()


def return_lsb(text):
    arr = []
    for i in text:
        arr.append(int(bin(ord(i))[-1]))
    return numpy.array(arr)


# all_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8


defa = [0, 2, 3, 4, 5, 7]
arr2 = [text1, text2, text3, text4, text5, text6, text7, text8]
all_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8

arr = return_lsb(all_text)
arr_n = arr.reshape((8, 662))
# """plt.imshow(arr_n, cmap='gray', interpolation='nearest')
# plt.show()"""
ideal = return_lsb(ideal_text)
xor = numpy.bitwise_xor(arr, ideal)
## xor = xor.reshape((8, 662))
f = 8
add = 0
xor = numpy.append(xor, [0] * ((f - (5296 % f)) % f))
xor = xor.reshape((f, len(xor) // f))
plt.imshow(xor, cmap='gray', interpolation='nearest')
plt.show()
plt.imshow(xor.T, cmap='gray', interpolation='nearest')
plt.show()
print("COLUMNS")
transform_column(xor)
print()

##plt.show()
# plt.show()

import itertools

j = 0

"""for list in itertools.permutations(defa):
    all_text = arr2[0]
    all_text += text2
    for i in list[1:-1]:
        all_text += arr2[i]
    all_text += text7
    all_text += arr2[list[-1]]

    arr = return_lsb(all_text)
    xor = numpy.bitwise_xor(arr, ideal)
    xor = xor.reshape((8, 662))
    transform_column(xor)

for list in itertools.permutations(defa):
    all_text = arr2[0]
    all_text += text7
    for i in list[1:-1]:
        all_text += arr2[i]
    all_text += text2
    all_text += arr2[list[-1]]

    arr = return_lsb(all_text)
    xor = numpy.bitwise_xor(arr, ideal)
    xor = xor.reshape((8, 662))
    transform_column(xor)"""

"""def transform_row(xor):
    arr = xor.reshape((xor.shape[0]*xor.shape[1],))
    start = 0
    end = start + 8
    while start < len(arr):
        number = 0
        j = 0
        arr_ = arr[start:end]
        for num in arr_:
            number += 2**(7-j)*int(num)
            j += 1
        if number != 0:
            print(chr(number), end='')
        start += 8
        end = start + 8
"""

"""
print('ROWS')
transform_row(xor)
print()"""
