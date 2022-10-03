def bytes_to_int(bytes_var: bytearray, signed: bool, byteorder: str) -> (int):

    """
    This script first converts a bytearray,
    to its corresponding signed/unsigned binary number,
    and then converts the binary number to an integer.

    >>> bytes_to_int(b'\\x00\\x10',False,'big')
    16
    >>> bytes_to_int(b'\\xfc\\x00',True,'big')
    -1024
    >>> bytes_to_int(b'\\x00\\x01',False,'big')
    1
    >>> bytes_to_int('abc',False,'big')
    ERROR - 'str' object cannot be interpreted as an integer
    0
    >>> bytes_to_int(b'\\x00\\x10',False,'little')
    4096
    """

    try:
        byteorder = byteorder.lower()
        if byteorder == "little":
            bytes_var = bytes_var[::-1]
        binval = ""
        for i in bytes_var:
            binnum = str(bin(i))[2:]
            if len(binnum) < 8:
                for i in range(0, 8 - len(binnum)):
                    binnum = "0" + binnum
            binval = binval + binnum

        rslt = 0

        if signed is True:
            temp = ""
            for j in binval:
                flag = j == "0"
                temp += str(int(flag))
            binval = temp
            binval = str(bin(int(binval, 2) + int("1", 2)))[2:]

        for k in binval:
            rslt = 2 * rslt + int(k)

        if signed is True:
            rslt *= -1

        return rslt

    except Exception as e:
        print(f"ERROR - {e}")
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
