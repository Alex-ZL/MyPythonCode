# coding: utf-8
def intToStr(i):
    digits = "0123456789"
    if i == 0:
        return '0'
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i/10
    return result