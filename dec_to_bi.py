#!/usr/bin/python3
import math


def dec_to_bi_int(dec_num):
    bi_num = ""
    if dec_num <= 1:
        result = dec_num
    else:
        while dec_num != 0:
            quotient, remainder = divmod(dec_num, 2)
            bi_num = str(remainder) + bi_num
            dec_num = quotient
        result = bi_num
    return result


def dec_to_bi_float(dec_num):
    bi_num = ""
    while dec_num != 0:
        quotient, remainder = math.modf(dec_num * 2)
        dec_num = quotient
        bi_num = bi_num + str(int(remainder))
    if bi_num is "":
        result = 0
    else:
        result = bi_num
    return result


def split_int_float(dec_num):
    dec_num = float(dec_num)
    float_num, int_num = math.modf(dec_num)
    result = (float(float_num), int(int_num))
    return result


def check_input_num(dec_str):
    result = dec_str.lstrip('-').replace('.', '', 1).isdigit()
    return result


def main():
    while True:
        print("=============================================")
        print("              Decimal to Binary             ")
        print("=============================================")
        input_num = input("Fill in a number(Decimal)? : ")
        if check_input_num(input_num) is True:
            float_num, int_num = split_int_float(input_num)
            output_int = dec_to_bi_int(int_num)
            output_float = dec_to_bi_float(float_num)
            print("{} is converted to \x1b[1;32m{}.{}\x1b[1;m\n".format(input_num, output_int, output_float))
        else:
            print("\x1b[1;31m{} isn't a number.\x1b[1;m\n".format(input_num))


main()
