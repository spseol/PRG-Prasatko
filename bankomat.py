#!/usr/bin/env python3
from sys import stdout, stderr


class Bankomat:
    trezor = {}

    def __init__(self, trezorfile):
        self.trezorfile = trezorfile

    def read(self):
        return True or False

    def write(self):
        return True or False

    def make(self, amount):
        return True or False


if __name__ == "__main__":
    bankomat = Bankomat("trezor.txt")

    while True:
        try:
            line = input("bankomat >> ")
            number = int(line)
            bankomat.read()
            bankomat.make(number)
            bankomat.write()
        except EOFError:
            print("\nExit")
            exit(0)
        except KeyboardInterrupt:
            stderr.write("\nProgram byl přerušen z klávecnice.")
            exit(1)
        except ValueError:
            stdout.write("ERROR: Nesprávná hodnota.\n")
