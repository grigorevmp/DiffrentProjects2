import numpy
import matplotlib.pyplot as plt

# Шаг 1) Данные
""" После того, как я открыл дамп с условием, первым делом начал листать до конца дампа, пытаясь найти странности.
Т.к. это плодов не принесло, я посмотрел название темы и поставил дисплейный фильтр по ICMP. Сразу же бросились в глаза
ICMP-пакеты с размером 704 и id=1984 =)
В пакетах содержалось повторение алфавита 28.8 раза с искажениями"""

# Шаг 2) Как это анализировать
""" Были скопированы все тексты и начался бурный брейншторм"""

text1 = "accdefghijklmnopqrstuvwabceegghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuvwabcdefghhkklmnopqrsttwwabcdefgihjjlmnopqrsttvwabcdefghikklmnopqrstuwwabbdefghijklmnnqqrstuwwabcddfghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnnpqrstuvwaccdefghijklmnopqrruuvwabcdefgihjklmnopqrsutvwabcdefghhjklmnopqrstuvwabcdefghhjklmnopqrsttvwabcdegfhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrstuvwabcdefghijkmmnopqrstuvw`cbdefghikklmonpqrstuwwabcdefghijjlmnopqrstuvvaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnnqprstuvwabbeefghijklmnoqqrsttvwabcdegfiijklmnopqssuuwwabcdeffhhjjlmnopprruuwv`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text2 = "`bbeefghijjlmnopqrstuvvabcdefghijkllnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnnpqrstuwwabceefghhjjlmnoqqrsutvwabcdefgihjjlmnopqrstuvvabcdefghijkmmoopqrstuwvabbeefghijjmmnoqprstuvv`bcdeffhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwaccedffhijklmnopprruuvwabcdegghijklmnopqrstuvwabcdefghhkklmnopqrsttwwabcdefghhjklmnopqsstuvwabcdegghijklmnopqrstuvwabcdefghijklmnopqrstuvvabcdefghikjmlnopqrstuvv`bcdefghijkllnopqrstuvwaccdefghijklmnopqrstuvwabceefghijjlmnopqrstuvvaccdefghijkmmnopqrstuvwabcdefghijklmnopqrstuvwabcdeggiijklmnoqprsuuvwabbdefghhjklmnoqqrrttvwabcddffhikklmnoppsstuvwabcddgghhjklmnopprsuuvw`bcdeggiijklmnopqrstuvwabcdefghijklmnopqr"
text3 = "acbdefghijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjjlmooqqrstuvwabbddfgiijjllnopprstuvwacbdefghijjmmnnpqrstuvv`bceefghijklmnopprstuvv`bcdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwaccddffiijklmnopqrsuuvwabcdegghijklmnopqsstuvwabcdefghijklmnoqqrsutvwabcddfghhkjlmnoppsstuvvabcdeggiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhkjllnopqrsttvvabcdefghijkmmnopqrstuvv`cbdefghikkllonpqrstuwwabceefghijklmnoqqrstuvwaccdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefgiijklmnoqpssuuvwabbdefghijklmnoqqrrtuvwabcdeffhijklmnopqssuuvwabcddggihjklmnopqsruuvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text4 = "accdefghijjlmnnpqrstuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijkmmnopqrstuww`ccdefgihjkllnopqrstuvw`cbddfgiijjllonpprsuuwwabbdegghijjlmnopqsstuvwabcdefghijjllnopqrstuvv`ccdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwaccddfgiijklmoopqrstuvwabbdefghijklmnnpqsrtuvwabceefgiikklmnoqqrsuuwwabcdefghikjlmnopqsstuvwabcdeggihjklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikkllnopqrsttvwaccdefghhkklmoopqrsttwvabbdefghikjllnopqrstuvwacbdefghijklmonqqrstuvwacbeefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnoqqsstuvwabbddgfhijklmnoqqrrtuvwabcdeffihjklmnoqqrrutvwabcddfgihkjlmnopqsrttvw`bcdegfiijklmnopqrstuvwabcdefghijklmnopqr"
text5 = "abbdefghijjlmnopqrrtuvvabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdefgihjkmmnopqrstuvw`bcddfghikjlmnnpqrsuuwvabbeefghijkmlnnpqsstuvw`cceeffhijjllooqprrtuww`cbdegfhijjlmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabcdegghijklmnnpqssuuvwabceeffhhjklmnoqqsrttvwabcddfgiikklmnopprstuvwabcdefghikklmnopqrstuwwabcdeggihjklmnopqrstuvwabcdefghijkllnopqrstuvw`ccdefghikkllnopqrsuuvwaccdefghhjklmnopqrstuvv`bcdefghijjmlnopqrstuvvaccdefghijkmmnopqrstuvw`ccdefghijklloopqrstuvwabcdefghijklmnopqrstuvwabcdeffhhjklmnopqsrtuvwabbdegfiijklmnoqqsruuvwabcedgfiijjlmnoqpssuuvwabcdegfhijjlmnopqrrtuvw`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text6 = "abcdefghijjlmnnpqrstuvvabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuwwaccdeffihkjmmnnpqrstuwv`bcedfghikjmmnoqqrsuuvv`bcedfghhjkllnoqprsttwwabcddgfhikklmnoqpsrtuww`bcddffiijjlmnopqrstuvwabcdefghijklmnopqrrtuvwabcddgghijklmnoqprrtuvwabbdefgiijklmnnpqrsuuvwabcdefghijklmnopqssuuvwabcdeffihjklmnopqrsutvwabcdegghhjklmnopqrstuvwabcdefgihjklmnopqrstuvwabcdefghijklmnopqrrtuvwaccdefgiikjlmoopqrsuuvvabcdefghijkmmnopqrstuvw`bcdefghijkmmnopqrstuvv`bcdefghijkmlnnpqrstuvw`cceefghijkllnopqrstuvwabcdefghijklmnopprstuvwabcdegghhjklmnopqsstuvwabbedfghijklmnnqprstuvwabcedgghijjlmnopqrstuvwabcdefghijjlmnopqrstuvv`bcdegghijklmnopqrstuvwabcdefghijklmnopqr"
text7 = "`ccdefghijklmnopqrrtuvwabcdefghijkmmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwaccdeffihjjlmnopqrrutvv`bcdefgihjkllnopprsuuvwaccdegghikklmnopqsstuvwabcdefghijklmnopqrstuvwabcdeffhijklmnopqrstuvwabcdefghijklmnopqrrtuvwabcdeggiijklmnoqqsruuvwabbdeffhhjklmnopqrrtuvwabcdefgiijklmnopqrsuuvwabcdeffhijklmnopqrstuvwabcdegghijklmnopqssutvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmnopqrstuwwabbdefghijjlmnnpqrstuvvabcdefghijjmmoopqrstuvvabbeefghijklmnnqqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghhjklmnopqrstuvwabbdefghhjklmnnpqrsttvwabcdefghikjlmnopqrstuwwabcdefghijjlmnopqrsttvvabcdefghijkllnopqrstuvwabcdefghijklmnopqr"
text8 = "abbdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijkllonpqrstuvwabcdefghijklmnopqrstuvwacceefghhjklmnoqqrsttvwabcddfghhjklmnopqrsttvwaccdefghikklmoopqrstuwwabbdefghijjlmnnpqrstuvvabcdeffhijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdegghijklmnoqqsstuvwabbeeffhhjklmnoqqrsttvwabcddfghijklmnopprstuvwabcdegghijklmnopqsrtuvwabcdeffiijklmnopqsruuvwabcdefgiijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghikklmoopqrstuwwabcdefghijklmnnpqrstuvwacceefghijjlmonpqrstuvwabceefghijklmnopqrstuvwabbdefghijklmnopqrstuvwabcdefghijklmnopqsstuvwabcdeffihjklmnoqprsuuvwabcdegghhjklmnopqsstuwwabcdeffhijjlmnopqrstuvwabcdefghijklmnopqrsttvvaccdefghijkllnopqrstuvwabcdefghijklmnopqr"

""" Возникло 2 идеи - тексты дают спрятанное сообщение по-отдельности, тексты дают сообщение только вместе """

# Шаг 3) Что дают тексты в отдельности

""" Логичным показалось все несовпадения выделить в 1, а совпадения в 0.
В дальнейшим, я обосновал это как нахождение последнего значащего бита lsb и xor-функции и идеальными значениями"""

""" Была идея, что высокие буквы - 1, низкие - 0"""

f = text1[0]
res1 = ""
res11 = ""
res111 = ""

sym1 = " "
sym = "*"
sym0 = " "

resX1 = " "
cpounter = 0
curr = 1
rep = False
for c in text1[1:]:
    if f == '`':
        curr = ord(c) - ord("a")
    if c == f:
        res1 += c

    if c == '`':
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif c == f and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX1 += sym
        cpounter += 1
        rep = True
    else:
        resX1 += sym1
        rep = False

    if c != chr(ord("a") + curr):
        res11 += chr(ord("a") + curr)
        if ord(c) - (ord("a") + curr) > 0:
            res111 += "1"
        else:
            res111 += "0"
    f = c
    curr += 1
    if curr == 23:
        curr = 0

print(resX1)
print(res1)
print(res11)
print(res111)

""" Были веведены разные варианты обнаружения чего-то в 1ом тексте: мб буквы что-то образуют, мб 1 и 0, мб там азбука 
Морзе, но беглый перевод в ascii и морзянку ничего не дал. Был предпринята отчаяная идея совместить тексты."""

# Шаг 4) Всё вместе и полный перебор (Переходите к строке 450, если не хотите видеть плохой код!)

alph = "qwertyuiopasdfghjklzxcvbnm"

f = text1[0]
res1 = ""
res11 = ""
res111 = ""

sym1 = " "
sym = "*"
sym0 = " "

resX1 = " "
resX2 = "*"
resX3 = " "
resX4 = " "
resX5 = " "
resX6 = " "
resX7 = "*"
resX8 = " "
cpounter = 0
curr = 1
rep = False
for c in text1[1:]:
    if f == '`':
        curr = ord(c) - ord("a")
    if c == f:
        res1 += c

    if c == '`':
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif c == f and rep is False:
        resX1 += sym
        cpounter += 1
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX1 += sym
        cpounter += 1
        rep = True
    else:
        resX1 += sym1
        rep = False

    if c != chr(ord("a") + curr):
        res11 += chr(ord("a") + curr)
        if ord(c) - (ord("a") + curr) > 0:
            res111 += "1"
        else:
            res111 += "0"

    f = c
    curr += 1
    if curr == 23:
        curr = 0

f = text2[0]
res2 = ""
res22 = ""
rep = True
for c in text2[1:]:
    if c == f:
        res22 += chr(ord(c) + 1)
        res2 += c

    if c == '`':
        resX2 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX2 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX2 += sym
        rep = True
    elif c == f and rep is False:
        resX2 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX2 += sym
        rep = True
    else:
        resX2 += sym1
        rep = False

    f = c

f = text3[0]
res33 = ""
res3 = ""
rep = False
for c in text3[1:]:
    if c == f:
        res33 += chr(ord(c) + 1)
        res3 += c

    if c == '`':
        resX3 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX3 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX3 += sym
        rep = True
    elif c == f and rep is False:
        resX3 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX3 += sym
        rep = True
    else:
        resX3 += sym1
        rep = False

    f = c

f = text4[0]
res4 = ""
res44 = ""
rep = False
for c in text4[1:]:
    if c == f:
        res44 += chr(ord(c) + 1)
        res4 += c

    if c == '`':
        resX4 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX4 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX4 += sym
        rep = True
    elif c == f and rep is False:
        resX4 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX4 += sym
        rep = True
    else:
        resX4 += sym1
        rep = False

    f = c

f = text5[0]
res5 = ""
res55 = ""
rep = False
for c in text5[1:]:
    if c == f:
        res55 += chr(ord(c) + 1)
        res5 += c

    if c == '`':
        resX5 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX5 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX5 += sym
        rep = True
    elif c == f and rep is False:
        resX5 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX5 += sym
        rep = True
    else:
        resX5 += sym1
        rep = False

    f = c

tf = text6[0]
res6 = ""
res66 = ""
rep = False
for c in text6[1:]:
    if c == f:
        res66 += chr(ord(c) + 1)
        res6 += c

    if c == '`':
        resX6 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX6 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX6 += sym
        rep = True
    elif c == f and rep is False:
        resX6 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX6 += sym
        rep = True
    else:
        resX6 += sym1
        rep = False

    f = c

f = text7[0]
res7 = ""
res77 = ""
rep = False
for c in text7[1:]:
    if c == f:
        res77 += chr(ord(c) + 1)
        res7 += c

    if c == '`':
        resX7 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX7 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX7 += sym
        rep = True
    elif c == f and rep is False:
        resX7 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX7 += sym
        rep = True
    else:
        resX7 += sym1
        rep = False

    f = c

f = text8[0]
res8 = ""
res88 = ""
rep = False
for c in text8[1:]:
    if c == f:
        res88 += chr(ord(c) + 1)
        res8 += c

    if c == '`':
        resX8 += sym
        rep = True
    elif ord(c) == ord(f) + 2 and rep is False:
        resX8 += sym
        rep = True
    elif ord(c) == ord(f) + 3 and rep is False:
        resX8 += sym
        rep = True
    elif c == f and rep is False:
        resX8 += sym
        rep = True
    elif ord(c) == (ord(f) - 1):
        resX8 += sym
        rep = True
    else:
        resX8 += sym1
        rep = False

    f = c

"""print("-----------------------")"""

high = "bdfghjklpqty"


def printHL(val):
    for _i in val:
        if _i in high:
            print(1, end="")
        else:
            print(0, end="")
    print()


"""printHL(res1)
printHL(res2)
printHL(res3)
printHL(res4)
printHL(res5)
printHL(res6)
printHL(res7)
printHL(res8)"""

"""
print("-----------------------")

print(res11)
print(res22)
print(res33)
print(res44)
print(res55)
print(res66)
print(res77)
print(res88)

print("-----------------------")

printHL(res11)
printHL(res22)
printHL(res33)
printHL(res44)
printHL(res55)
printHL(res66)
printHL(res77)
printHL(res88)

print("-----------------------")

printHL(res111)

"""

arr = [resX1, resX2, resX3, resX4, resX5, resX6, resX7, resX8]
defa = [0, 1, 2, 3, 4, 5, 6, 7]
"""
for i in arr:
    for j in arr:"""

print(resX1)
print(resX2)
print(resX3)
print(resX4)
print(resX5)
print(resX6)
print(resX7)
print(resX8)
print()
print()

print(resX8)
print(resX7)
print(resX6)
print(resX5)
print(resX4)
print(resX3)
print(resX2)
print(resX1)

import itertools

# БУДЬТЕ АККУРАТНЫ: данный строчки генерируют ПОЛНЫЙ перебор перестановок текстов, размер файла вышел немаленький

with open("newfile.txt", 'w') as outfile:
    for list in itertools.permutations(defa):
        for i in list:
            outfile.write(arr[i])
            outfile.write("\n")
        outfile.write("\n\n")
        outfile.write("\n\n")

""" Что нам дало данное творение - Я всё равно не смог проанализировать все перестановки, но видно, что несмотря на то,
что что-то в сочетание текстов разглядеть можно, но смысла это не несёт
В итоге - перестановка строк бессмысленна
Изменение размерности - бессмысленно
Перестановка столбцов - безумие """

print("//////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////")
print("///////////                  NEW PART                     ////////////")
print("//////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////")

# Шаг 5) Рефакторинг и ключ

""" Следующим шагом стала перепись кода в человеческий вид и визуализация с помощью plt
Для тестирования - выведем ещё и транспонированный вариант - мало ли...?"""

correct_alphabet = ('abcdefghijklmnopqrstuvw' * 28 + 'abcdefghijklmnopqr') * 8


def lbs_fication(text):
    result = []
    for i in text:
        result.append(int(bin(ord(i))[-1]))
    return numpy.array(result)


arr2 = [text1, text2, text3, text4, text5, text6, text7, text8]
all_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8

arr = lbs_fication(all_text)
# Будто бы текст под текстом
arr_n = arr.reshape((8, 662))
ideal_text = lbs_fication(correct_alphabet)
xorred_text = numpy.bitwise_xor(arr, ideal_text)
f = 8
add = 0
xor = numpy.append(xorred_text, [0] * ((f - (5296 % f)) % f))
xor = xor.reshape((f, len(xor) // f))
plt.imshow(xor, cmap='gray', interpolation='nearest')
plt.show()
plt.imshow(xor.T, cmap='gray', interpolation='nearest')
plt.show()

""" Опять ничего особо не прояснилось, но отчётливо видно, что вначале текст отделён полосой, вопрос только - что
это значит. Заметил, что если транспонированный текст читать как ASCII код, то в обеих вариантах получается первый символ B.
Появилось 2 идеи - 
Спрятаны буквы, чтобы получилось слово 
Буквы и цифры образуют какую-то последовательность
Поэтому опять прибегнул к перестановком, но пытаясь не портить буквы B, т.к. в Ascii первый символ точно 0..."
"""

defa = [0, 2, 3, 4, 5, 7]

import re


def read_by_columns(xor):
    result = ""
    for _i in range(xor.shape[1]):
        number = 0
        j = 0
        for num in xor[:, _i]:
            number += 2 ** (j) * int(num)
            j += 1
        # if number != 0:
        result += chr(number)
        # print(chr(number), end='')
    result_alpha = re.sub(r'[^A-Za-z]', '', result)  #
    print(result)
    print(result_alpha)

    print()


# Долго выполняется

# for list in itertools.permutations(defa):
#     all_text = arr2[0]
#     all_text += text2
#     for i in list[1:-1]:
#         all_text += arr2[i]
#     all_text += text7
#     all_text += arr2[list[-1]]
#
#     arr = lbs_fication(all_text)
#     xor = numpy.bitwise_xor(arr, ideal_text)
#     xor = xor.reshape((8, 662))
#     read_by_columns(xor)

# Долго выполняется

# for list in itertools.permutations(defa):
#     all_text = arr2[0]
#     all_text += text7
#     for i in list[1:-1]:
#         all_text += arr2[i]
#     all_text += text2
#     all_text += arr2[list[-1]]
#
#     arr = lbs_fication(all_text)
#     xor = numpy.bitwise_xor(arr, ideal_text)
#     xor = xor.reshape((8, 662))
#     read_by_columns(xor)

defa_2 = [0, 1, 2, 3, 4, 5, 6, 7]

# Долго выполняется

# for list in itertools.permutations(defa_2):
#    all_text = ""
#    for i in list:
#        all_text += arr2[i]
#    arr = lbs_fication(all_text)
#    xor = numpy.bitwise_xor(arr, ideal_text)
#    xor = xor.reshape((8, 662))
#    read_by_columns(xor)

"""Получилось огромное количество разных комбинаций, я пытался пройтись поиском по интересным комбинациям.
Там были
BELKA
USSR 
И главное! - BMP
В голову сразу пришло, что, если читать столбцы наоборот получается BP первых символах.
Я проверил, и действительно, BMP картинки сохраняются как BM? набор символов, аналог полосы и набор битов.
Кажется - это наш вариант!"""

""" Код не работает, потому что символы выходят за 128. Удалим их."""

"""def read_by_columns_ver2(xor):
    result = ""
    for _i in range(xor.shape[1]):
        number = 0
        j = 0
        for num in xor[:, _i]:
            number += 2 ** j * int(num)
            j += 1
        print(chr(number), end='')
        result += chr(number)
    return result"""


def read_by_columns_ver3(xor):
    result = ""
    size = xor.shape[1]
    for _i in range(size):
        number = 0
        j = 0
        for num in xor[:, _i]:
            if j != 7:
                number += 2 ** j * int(num)
                j += 1
        print(chr(number), end='')
        result += chr(number)
    return result


all_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8
arr = lbs_fication(all_text)
ideal = lbs_fication(correct_alphabet)
xor = numpy.bitwise_xor(arr, ideal)
xor = xor.reshape(8, 662)

res = read_by_columns_ver3(xor)

print(res.encode('ascii', 'replace'))
with open('message.bmp', 'w+b') as f:
    f.write(res.encode('ascii'))

# ZABERITE MENYA OTSYDA POZALUYSTA
# С учётом северокорейских сайтов в дампе всё встаёт на свои места
