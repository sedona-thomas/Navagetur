#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Random password generator and password security checker

    @author: sedonathomas
"""

import random
import string
import math
import time
import os


class Password(object):

    def __init__(self):
        self.letters = string.ascii_letters
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.punctuation = string.punctuation
        self.special_characters = "@#$%^&*_-=+`~\\/"
        self.parentheses = "()[]{}<>|"
        self.punctuation = ".?,!;:'\""
        chars = [string.ascii_letters, string.digits, string.punctuation]
        self.characters = "".join(chars)

    def generate(self, length):
        return "".join([random.choice(self.characters) for i in range(length)])

    def generate_letter_heavy(self, length):
        return "".join([random.choice("".join([self.characters, 4*self.lowercase])) for i in range(length)])

    def print_password(self, length):
        print("\n{}\n".format(self.random_password_generator(length)))

    def brute_force_attack(self, password):
        leak, search = self.check_leaks(password), self.search_time(password)
        time = leak if leak != -1 and leak < search else search
        end = " (leaked password)" if leak != -1 else ""
        if time / (60 * 60 * 24 * 365) > 1:
            return "{:.0f} years{}".format(time / (60 * 60 * 24 * 365), end)
        elif time / (60 * 60 * 24) > 1:
            return "{:.0f} days{}".format(time / (60 * 60 * 24), end)
        elif time / (60 * 60) > 1:
            return "{:.0f} hours{}".format(time / (60 * 60), end)
        elif time / (60) > 1:
            return "{:.0f} minutes{}".format(time / (60), end)
        else:
            s = "{:." + str(3 + abs(int(math.log10(time)))) + "f} seconds{}"
            return s.format(time, end)

    def search_time(self, password):
        possible_passwords = self.search_space(password)
        computation_time = self.runtime_test()
        return possible_passwords * computation_time  # seconds

    def search_space(self, password):
        possibilities, pw_set = 0, set(password)
        for s in [self.lowercase, self.uppercase, self.numbers, self.punctuation]:
            if len(set(s).intersection(pw_set)) > 0:
                possibilities += len(self.lowercase)
        return (possibilities ** len(password))

    def runtime_test(self):
        length = 100
        start = time.time()  # seconds
        li = [0 for i in range(length)]  # runs in C speed
        end = time.time()  # seconds
        return ((end - start) / length)  # seconds

    def check_leaks(self, password):
        start = time.time()
        filepath = '../leaked_passwords/'
        files = os.listdir(filepath)
        files = [file for file in files if self.nonRM_txt(file)]
        for filename in files:
            with open(filepath + filename) as file:
                leaked_passwords = [line.rstrip() for line in file]
                if password in leaked_passwords:
                    return time.time() - start  # seconds
        return -1

    def nonRM_txt(self, s):
        return "readme" not in s.lower() and s.endswith(".txt")


if __name__ == "__main__":
    password_handler = Password()
    password = password_handler.generate(15)
    print(password)
    print(password_handler.brute_force_attack(password))

    print()

    password = password_handler.generate(10)
    print(password)
    print(password_handler.brute_force_attack(password))

    print()

    password = password_handler.generate(5)
    print(password)
    print(password_handler.brute_force_attack(password))

    print()

    print("15 chars, upper, lower, number, special char: ", "dhbaa4786ASD#$%#")
    print(password_handler.brute_force_attack("dhbaa4786ASD#$%#"))

    print()

    print("15 chars, upper, lower, number: ", "fjdknfjfnASEDE123")
    print(password_handler.brute_force_attack("fjdknfjfnASEDE123"))

    print()

    print("15 chars, upper, lower: ", "dhdhjfbhjAWSEDF")
    print(password_handler.brute_force_attack("dhdhjfbhjAWSEDF"))

    print()

    print("15 chars, lower: ", "fjdknfjfnhdnjhd")
    print(password_handler.brute_force_attack("fjdknfjfnhdnjhd"))

    print()

    print("password")
    print(password_handler.brute_force_attack("password"))

    print()

    print("a")
    print(password_handler.brute_force_attack("a"))
