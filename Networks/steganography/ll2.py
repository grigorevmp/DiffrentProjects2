alph = "abcdefghijklmnopqrstuvw"

text1 = "accdefghijklmnopqrstuvwabceegghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuvwabcdefghhkklmnopqrsttwwabcdefgihjjlmnopqrsttvwabcdefghikklmnopqrstuwwabbdefghijklmnnqqrstuwwabcddfghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnnpqrstuvwaccdefghijklmnopqrruuvwabcdefgihjklmnopqrsutvwabcdefghhjklmnopqrstuvwabcdefghhjklmnopqrsttvwabcdegfhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrstuvwabcdefghijkmmnopqrstuvw`cbdefghikklmonpqrstuwwabcdefghijjlmnopqrstuvvaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnnqprstuvwabbeefghijklmnoqqrsttvwabcdegfiijklmnopqssuuwwabcdeffhhjjlmnopprruuwv`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text2 = "`bbeefghijjlmnopqrstuvvabcdefghijkllnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuwwabceefghhjjlmnoqqrsutvwabcdefgihjjlmnopqrstuvvabcdefghijkmmoopqrstuwvabbeefghijjmmnoqprstuvv`bcdeffhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwaccedffhijklmnopprruuvwabcdegghijklmnopqrstuvwabcdefghhkklmnopqrsttwwabcdefghhjklmnopqsstuvwabcdegghijklmnopqrstuvwabcdefghijklmnopqrstuvvabcdefghikjmlnopqrstuvv`bcdefghijkllnopqrstuvwaccdefghijklmnopqrstuvwabceefghijjlmnopqrstuvvaccdefghijkmmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnoqprsuuvwabbdefghhjklmnoqqrrttvwabcddffhikklmnoppsstuvwabcddgghhjklmnopprsuuvw`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text3 = "acbdefghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjjlmooqqrstuvwabbddfgiijjllnopprstuvwacbdefghijjmmnnpqrstuvv`bceefghijklmnopprstuvv`bcdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwaccddffiijklmnopqrsuuvwabcdegghijklmnopqsstuvwabcdefghijklmnoqqrsutvwabcddfghhkjlmnoppsstuvvabcdeggiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhkjllnopqrsttvvabcdefghijkmmnopqrstuvv`cbdefghikkllonpqrstuwwabceefghijklmnoqqrstuvwaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefgiijklmnoqpssuuvwabbdefghijklmnoqqrrtuvwabcdeffhijklmnopqssuuvwabcddggihjklmnopqsruuvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text4 = "accdefghijjlmnnpqrstuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijkmmnopqrstuww`ccdefgihjkllnopqrstuvw`cbddfgiijjllonpprsuuwwabbdegghijjlmnopqsstuvwabcdefghijjllnopqrstuvv`ccdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwaccddfgiijklmoopqrstuvwabbdefghijklmnnpqsrtuvwabceefgiikklmnoqqrsuuwwabcdefghikjlmnopqsstuvwabcdeggihjklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrsttvwaccdefghhkklmoopqrsttwvabbdefghikjllnopqrstuvwacbdefghijklmonqqrstuvwacbeefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwabbddgfhijklmnoqqrrtuvwabcdeffihjklmnoqqrrutvwabcddfgihkjlmnopqsrttvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text5 = "abbdefghijjlmnopqrrtuvvabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjkmmnopqrstuvw`bcddfghikjlmnnpqrsuuwvabbeefghijkmlnnpqsstuvw`cceeffhijjllooqprrtuww`cbdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabcdegghijklmnnpqssuuvwabceeffhhjklmnoqqsrttvwabcddfgiikklmnopprstuvwabcdefghikklmnopqrstuwwabcdeggihjklmnopqrstuvwabcdefghijkllnopqrstuvw`ccdefghikkllnopqrsuuvwaccdefghhjklmnopqrstuvv`bcdefghijjmlnopqrstuvvaccdefghijkmmnopqrstuvw`ccdefghijklloopqrstuvwabcdefghijklmnopqrstuvwabcdeffhhjklmnopqsrtuvwabbdegfiijklmnoqqsruuvwabcedgfiijjlmnoqpssuuvwabcdegfhijjlmnopqrrtuvw`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text6 = "abcdefghijjlmnnpqrstuvvabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdeffihkjmmnnpqrstuwv`bcedfghikjmmnoqqrsuuvv`bcedfghhjkllnoqprsttwwabcddgfhikklmnoqpsrtuww`bcddffiijjlmnopqrstuvwabcdefghijklmnopqrrtuvwabcddgghijklmnoqprrtuvwabbdefgiijklmnnpqrsuuvwabcdefghijklmnopqssuuvwabcdeffihjklmnopqrsutvwabcdegghhjklmnopqrstuvwabcdefgihjklmnopqrstuvwabcdefghijklmnopqrrtuvwaccdefgiikjlmoopqrsuuvvabcdefghijkmmnopqrstuvw`bcdefghijkmmnopqrstuvv`bcdefghijkmlnnpqrstuvw`cceefghijkllnopqrstuvwabcdefghijklmnopprstuvwabcdegghhjklmnopqsstuvwabbedfghijklmnnqprstuvwabcedgghijjlmnopqrstuvwabcdefghijjlmnopqrstuvv`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text7 = "`ccdefghijklmnopqrrtuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwaccdeffihjjlmnopqrrutvv`bcdefgihjkllnopprsuuvwaccdegghikklmnopqsstuvwabcdefghijklmnopqrstuvwabcdeffhijklmnopqrstuvwabcdefghijklmnopqrrtuvwabcdeggiijklmnoqqsruuvwabbdeffhhjklmnopqrrtuvwabcdefgiijklmnopqrsuuvwabcdeffhijklmnopqrstuvwabcdegghijklmnopqssutvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmnopqrstuwwabbdefghijjlmnnpqrstuvvabcdefghijjmmoopqrstuvvabbeefghijklmnnqqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhjklmnopqrstuvwabbdefghhjklmnnpqrsttvwabcdefghikjlmnopqrstuwwabcdefghijjlmnopqrsttvvabcdefghijkllnopqrstuvwabcdefghijklmnopqr"
text8 = "abbdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwacceefghhjklmnoqqrsttvwabcddfghhjklmnopqrsttvwaccdefghikklmoopqrstuwwabbdefghijjlmnnpqrstuvvabcdeffhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabbeeffhhjklmnoqqrsttvwabcddfghijklmnopprstuvwabcdegghijklmnopqsrtuvwabcdeffiijklmnopqsruuvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmoopqrstuwwabcdefghijklmnnpqrstuvwacceefghijjlmonpqrstuvwabceefghijklmnopqrstuvwabbdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwabcdeffihjklmnoqprsuuvwabcdegghhjklmnopqsstuwwabcdeffhijjlmnopqrstuvwabcdefghijklmnopqrsttvvaccdefghijkllnopqrstuvwabcdefghijklmnopqr"

ideal_text = ('abcdefghijklmnopqrstuvw' * 28 + 'abcdefghijklmnopqr') * 8
id = []
for ch in ideal_text:
    id.append(int(bin(ord(ch))[-1]))

arrs = [text1, text2, text3, text4, text5, text6, text7, text8]

arrs2 = []
i = 0
for ar in arrs:
    arrs2.append([])
    for ch in ar:
        arrs2[i].append(int(bin(ord(ch))[-1]))
    i += 1

for ar in arrs2:
    for i in range(len(ar)):
        ar[i] = ar[i] ^ id[i]

for ar in arrs2:
    for i in ar:
        if i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

sh = 0

print()
f_tr = ""
endM = [[], [], [], [], [], [], [], []]

for y in range(len(arrs2[0])):
    _str = ""
    j = 0
    for i in range(sh, 8):
        _str += str(arrs2[i][y])
        endM[j].append(arrs2[i][y] * '*')
        j += 1
    for i in range(0, sh):
        _str += str(arrs2[i][y])
        endM[j].append(arrs2[i][y] * '*')
        j += 1
    sh -= 1
    sh = sh % 8
    f_tr += chr(int(_str, 2))
    print(chr(int(_str, 2)))

import re

res = re.sub(r'[^A-Za-z]', '', f_tr)
print(res)

for e in endM:
    for _e in e:
        if str(_e) == '*':
            print(str(_e), end="")
        else:
            print(str(' '), end="")
    print()
