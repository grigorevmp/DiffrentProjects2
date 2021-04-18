import math


class HemmingCode:
    def __init__(self, data):
        self.data = data
        self.code = ""

    def encode(self, input_num, code_word_len, control_bits_num):
        binary_input_data = ""
        for symbol in str(input_num):
            bin_symbol = str(bin(ord(symbol))[2:])
            # add zeroes if need
            if len(bin_symbol) < 8:
                bin_symbol = (8 - len(bin_symbol)) * "0" + bin_symbol
            binary_input_data += bin_symbol

        # split string by code_word_len - control_bits_num
        binary_input_data_split = self.splitStrByN(binary_input_data, code_word_len - control_bits_num)

        result = ""
        # with every group
        for part in binary_input_data_split:
            # add zeroes if need
            if len(part) < code_word_len:
                part = part + (code_word_len - len(part)) * "0"
            part_of_encrypted_word = [0 for _ in range(code_word_len)]
            current_power = 0
            k = 0
            # expand array to size of code word
            for i in range(len(part)):
                if i + 1 == 2 ** current_power:
                    current_power += 1
                else:
                    part_of_encrypted_word[i] = part[k]
                    k += 1

            array_of_cw = self.returnControlBits(part_of_encrypted_word, control_bits_num)

            for i in range(control_bits_num):
                part_of_encrypted_word[2 ** i - 1] = sum(array_of_cw[i][1:]) % 2

            # reverse word due to trap in previous part ^_~
            part_of_encrypted_word = part_of_encrypted_word[::-1]

            for ch in part_of_encrypted_word:
                result += str(ch)

        left_symbols = math.ceil(float(len(result)) / float(8)) * 8 - len(result)
        result = result + "0" * left_symbols

        encrypted_word = self.splitStrByN(result, 8)

        final_encrypted_word = ""
        final_encrypted_word_in_list = []
        for _res in encrypted_word:
            final_encrypted_word += str(int(_res, 2)) + ", "
            final_encrypted_word_in_list.append(int(_res, 2))

        return final_encrypted_word, final_encrypted_word_in_list

    @staticmethod
    def returnControlBits(code_word, control_bits_num):
        """
        Control bit is XOR of N bit through N starting with N bit
        :param code_word:
        :param control_bits_num:
        :return:
        """
        code_word_array = []
        for a in code_word:
            code_word_array.append(int(a))
        sub_code_word_array = []
        for i in range(control_bits_num):
            sub_code_word_array.append([])
            k = 0
            copy_this_element = True
            # from N bit to the end
            for j in range(2 ** i - 1, len(code_word_array)):
                if copy_this_element:
                    sub_code_word_array[i].append(code_word_array[j])
                k += 1
                k = k % (2 ** (i + 1))
                if k == (2 ** i) or k == 0:
                    copy_this_element = not copy_this_element
        return sub_code_word_array

    def decoding(self, code_word, number):
        code_word_array = []
        for a in code_word:
            code_word_array.append(int(a))
        check_bits = [0 for _ in range(number)]
        mini_array = []
        error_bit = 0
        for i in range(number):
            mini_array.append([])
            k = 0
            copy_this_element = 1
            for j in range(2 ** i - 1, len(code_word_array)):
                if copy_this_element:
                    mini_array[i].append(code_word_array[j])
                k += 1
                k = k % (2 ** (i + 1))
                if k == (2 ** i) or k == 0:
                    copy_this_element = not copy_this_element
            # Sum all elements in wrong control bits
            check_bits[i] = sum(mini_array[i][1:]) % 2
            if check_bits[i] != mini_array[i][0]:
                error_bit += 2 ** i
        if error_bit != 0:
            # invert wrong bit
            code_word_array[error_bit - 1] = int(not (code_word_array[error_bit - 1]))
        code_word_array = [str(i) for i in code_word_array]
        code_word = ""
        for a in code_word_array:
            code_word += a
        # delete control bits
        code_word = self.deleteControlBits(code_word)
        return code_word

    @staticmethod
    def splitStrByN(string, n):
        return [string[i:i + n] for i in range(0, len(string), n)]

    @staticmethod
    def bin_to_char(p):
        return chr(int(p, 2))

    @staticmethod
    def num_to_binary(var):
        return str(bin(var)[2:])

    @staticmethod
    def deleteControlBits(code_word):
        """
        :param code_word: current string
        :return: string with deleted control bits
        """
        degree = 0
        informational_word = ""
        code_word_len = len(code_word)
        for i in range(code_word_len):
            if i + 1 == 2 ** degree:
                degree += 1
            else:
                informational_word += code_word[i]
        return informational_word

    def decode(self, code_word_len, control_bits_num):
        """
        :param code_word_len:
        :param control_bits_num:
        :return:
        """

        # create a binary string
        for number in self.data:
            binary = str(self.num_to_binary(number))
            if len(binary) < 8:
                binary = (8 - len(binary)) * "0" + binary
            self.code += binary

        # n groups by code_word_len bits
        divided_string = self.splitStrByN(self.code, code_word_len)

        # calculate control bits, fix wrong and delete others
        # REVERSE EVERY WORD for this special code
        filtered_divided_string = []
        for group in divided_string:
            if len(group) < code_word_len:
                break
            filtered_divided_string.append(self.decoding(group[::-1], control_bits_num))

        unit_string = ""

        # Connect all groups to one string
        for group in filtered_divided_string:
            unit_string += group

        # split it by 8 bits
        final_string = self.splitStrByN(unit_string, 8)

        # and get ascii
        result = ""
        for group in final_string:
            result += self.bin_to_char(group)

        return result


if __name__ == "__main__":
    input_data = [74, 177, 157, 65, 37, 234, 4, 188, 10, 151, 136, 67, 0, 41, 70, 123, 5, 32, 100, 113, 20, 90, 55, 137, 66, 65, 57, 44, 86, 150, 136, 74, 192, 13, 61, 2, 55, 196]
    word = 20
    controlBits = math.floor(math.log(word, 2)) + 1
    print("// Code word: ", word)
    print("// Control bits num: ", controlBits)
    print()

    code = HemmingCode(input_data)
    result1 = code.decode(word, controlBits)
    print("Decrypted phrase: ", result1)
    answer = int(result1.split(" ")[1]) * int(result1.split(" ")[3])
    print("Answer to phrase: ", answer)

    result2, resultList = code.encode(answer, word, controlBits)
    # print("Encrypted answer [str]", result2)
    print("Encrypted answer [list]: ", resultList)

    code = HemmingCode(resultList)
    answer2 = str(code.decode(word, controlBits))
    print("Decrypt the result to compare ", answer2)
