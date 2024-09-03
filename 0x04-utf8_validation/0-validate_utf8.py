#!/usr/bin/python3
"""validating utf-8"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """a utf-8 data validator"""
    # check the cont'd bytes
    n_bytes = 0
    byte_1_check = 0b10000000
    bytes_2_check = 0b11100000
    bytes_3_check = 0b11110000
    bytes_4_check = 0b11111000

    # check the validity of the rem bytes
    byte_contd_check = 0b11000000

    for num in data:
        if n_bytes == 0:
            if num & byte_1_check == 0:
                continue
            elif num & bytes_4_check == 0b11110000:
                n_bytes = 3
            elif num & bytes_3_check == 0b11100000:
                n_bytes = 2
            elif num & bytes_2_check == 0b11000000:
                n_bytes = 1
            else:
                return False
        else:
            if num & byte_contd_check != 0b10000000:
                return False
            n_bytes -= 1
    return n_bytes == 0
