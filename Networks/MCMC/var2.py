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

text1 = text1
text2 = text2
text3 = text3
text4 = text4
text5 = text5
text6 = text6
text7 = text7
text8 = text8

ideal_text = ('abcdefghijklmnopqrstuvw' * 28 + 'abcdefghijklmnopqr') * 8


def return_lsb(text):
    arr = []
    for i in text:
        arr.append(int(bin(ord(i))[-1]))
    return numpy.array(arr)


all_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8

# arr2 = [text1, text2, text3, text4, text5, text6, text7, text8]
# arr2 = [text1, text2, text3, text4, text6, text5, text7, text8]

defa = [0, 1, 2, 3, 4, 5, 6, 7]


arr = return_lsb(all_text)
arr_n = arr.reshape((8, 662))
"""plt.imshow(arr_n, cmap='gray', interpolation='nearest')
plt.show()"""
ideal = return_lsb(ideal_text)
xor = numpy.bitwise_xor(arr, ideal)
# xor = xor.reshape((8, 662))
f = 8
add = 0
xor = numpy.append(xor, [0] * ((f - (5296 % f)) % f))
xor = xor.reshape((f, len(xor) // f))
plt.imshow(xor, cmap='gray', interpolation='nearest')
"""plt.show()
plt.imshow(xor.T, cmap='gray', interpolation='nearest')"""

##plt.show()
plt.show()

"""import itertools
j = 0
for list in itertools.permutations(defa):
    all_text = ""
    for i in list:
        all_text += arr2[i]
    arr = return_lsb(all_text)
    xor = numpy.bitwise_xor(arr, ideal)
    xor = xor.reshape((8, 662))
    plt.imshow(xor, cmap='gray', interpolation='nearest')
    plt.savefig(f'res/{j}.png')
    j += 1
"""

