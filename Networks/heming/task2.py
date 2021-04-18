from math import comb

###
# Для задания про Космического Котика достаточно кратких теоретических пояснений
# и кода программы либо решения на листочке (но, надеюсь, никто не пошел таким путем O_o)
###

""" INPUT DATA """

_p = 0.315712416801
const_probability = _p
q = 1 - const_probability
_packages = 5
_limit = 18

"""
Изначально мы можем отправить n пакетов и доставлены будут k из n требуемых. 
С помощью формулы Бернулли рассчитаем вероятность каждого из k случаев.
Затем, нам должен прийти "отчёт о доставке" с шансом 1-p. Если он не пришёл, вновь отправляем n пакетов,
иначе n-k. Рекурсивно повторяем, пока не превышен лимит

Реализуем этот алгоритм с помощью рекурсивной функции:
"""


def Probability_of_send(num_of_frames, probability, max_num_of_frames):
    result = float(0)
    for i in range(num_of_frames + 1):
        # Bernoulli formula to get chance of current case (k from n)
        p_i = probability * comb(num_of_frames, i) * const_probability ** (num_of_frames - i) * q ** i
        # messaged received chance
        success = successfully_received_answer = p_i * q
        # message lost chance
        failure = p_i * const_probability
        """
        Recursive part
            Calculate probability of successful sending of frames in node
        """
        if i != num_of_frames:
            if (num_of_frames - i) > (max_num_of_frames - num_of_frames):
                # we don't have enough "credits"
                successfully_received_answer = 0
            else:
                successfully_received_answer = Probability_of_send(num_of_frames - i, success,
                                                                   max_num_of_frames - num_of_frames)
        if num_of_frames > (max_num_of_frames - num_of_frames):
            # we don't have enough "credits"
            answer_was_not_received = 0
        else:
            answer_was_not_received = Probability_of_send(num_of_frames, failure, max_num_of_frames - num_of_frames)
        # result
        result = result + successfully_received_answer + answer_was_not_received
    return result


if __name__ == '__main__':
    p = _p
    packages = _packages
    limit = _limit
    prob = Probability_of_send(packages, 1, limit)
    # Round to 12 after comma?
    print("Chance of successful result is: ", prob)
