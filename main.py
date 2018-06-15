#!/usr/bin/python3

import pickle
import os


def dec_to_bi_int(dec_num):
    bi_num = ""
    dec_num = int(dec_num)
    if dec_num <= 1:
        result = dec_num
    else:
        while dec_num > 1:
            quotient = dec_num // 2
            remainder = dec_num % 2
            dec_num = quotient
            bi_num += str(remainder)

        bi_num = str(quotient) + bi_num
        result = int(bi_num)
    return result

def dec_to_bi_float(dec_num):
    bi_num = ""
    dec_num = float(dec_num)
    # if dec_num <= 1:
    #     result = dec_num
    # else:
    while dec_num != 0:
        quotient = dec_num // 0.5
        remainder = dec_num % 0.5
        dec_num = remainder
        bi_num += str(quotient)
        print(bi_num)

    bi_num = str(quotient) + bi_num
    result = int(bi_num)
    return result



def main():
    while True:
        print("=============================================")
        print("              Decimal to Binary             ")
        print("=============================================")
        input_num = input("Fill in a number(Decimal)? :")
        output_num = dec_to_bi_float(input_num)
        print("{} is converted to {}\n".format(input_num, output_num))

main()
