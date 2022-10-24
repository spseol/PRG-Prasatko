#!/usr/bin/env python3
from sys import stdout, stderr


class Bankomat:
    TREZORFILE = "trezor.txt"
    trezor = {}

    def read():
        return True or False

    def write():
        return True or False

    def make(amount):
        return True or False


if __name__ == "__main__":
    bankomat = Bankomat

    while True:
        try:
            line = input("bankomat >> ")
            number = int(line)
            bankomat.read()
            bankomat.make(number)
            bankomat.write()
        except EOFError:
            exit(0)
        except KeyboardInterrupt:
            stderr.write("Program byl přerušen z klávecnice.")
            exit(1)
        except ValueError:
            stdout.write("ERROR\n")
