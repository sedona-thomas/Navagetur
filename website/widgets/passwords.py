#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Random password generator and password security checker
"""

__author__ = "Sedona Thomas"
__date__ = "03/04/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

import random
import string
import math
import time
import os


class Password(object):

    """
    Password generates passwords and calculates the time to brute force crack passwords
    """

    def __init__(self):
        """
        Construct a new 'Password' object.

        :return: returns nothing
        """
        self.filepath = '../leaked_passwords/'
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
        """
        Generates a random password of specified length

        :param length: length of the password
        :return: returns a random password
        """
        return "".join([random.choice(self.characters) for i in range(length)])

    def generate_letter_heavy(self, length):
        """
        Generates a random password of specified length with a higher ratio of lowercase letters

        :param length: length of the password
        :return: returns a random password
        """
        return "".join([random.choice("".join([self.characters, 4*self.lowercase])) for i in range(length)])

    def print_password(self, length):
        """
        Prints a random password

        :return: returns nothing
        """
        print("\n{}\n".format(self.random_password_generator(length)))

    def brute_force_attack(self, password):
        """
        Calculates the time to brute force crack a password

        :param :password password to check
        :return: returns a string describing the time to brute force crack the password
        """
        leak, search = self.check_leaks(password), self.search_time(password)
        time = leak if leak != -1 and leak < search else search
        end = " (leaked password)" if leak != -1 else ""
        if time / (60 * 60 * 24 * 365 * 1000) > 1:
            return "{:.0f} millennia{}".format(time / (60 * 60 * 24 * 365 * 1000), end)
        elif time / (60 * 60 * 24 * 365 * 100) > 1:
            return "{:.0f} centuries{}".format(time / (60 * 60 * 24 * 365 * 100), end)
        elif time / (60 * 60 * 24 * 365 * 10) > 1:
            return "{:.0f} decades{}".format(time / (60 * 60 * 24 * 365 * 10), end)
        elif time / (60 * 60 * 24 * 365) > 1:
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
        """
        Calculates the time to brute force check all passwords of the same composition

        :param :password password to check
        :return: returns seconds to generate all passwords with same characteristics
        """
        possible_passwords = self.search_space(password)
        computation_time = self.runtime_test()
        return possible_passwords * computation_time  # seconds

    def search_space(self, password):
        """
        Calculates the search space to brute force crack a password

        :param :password password to check
        :return: returns number of possible combinations of password composition
        """
        possibilities, pw_set = 0, set(password)
        for s in [self.lowercase, self.uppercase, self.numbers, self.punctuation]:
            if len(set(s).intersection(pw_set)) > 0:
                possibilities += len(self.lowercase)
        return (possibilities ** len(password))

    def runtime_test(self):
        """
        Tests the time to execute single iteration of a loop on current device

        :return: returns seconds to execute one loop iteration
        """
        length = 100
        start = time.time()  # seconds
        li = [0 for i in range(length)]  # runs in C speed
        end = time.time()  # seconds
        return ((end - start) / length)  # seconds

    def check_leaks(self, password):
        """
        Calculates the time find a password in leaked password lists

        :param :password password to check
        :return: returns time to find password in files or -1 if not found
        """
        start = time.time()
        files = os.listdir(self.filepath)
        files = [file for file in files if self.nonRM_txt(file)]
        for filename in files:
            with open(self.filepath + filename) as file:
                leaked_passwords = [line.rstrip() for line in file]
                if password in leaked_passwords:
                    return time.time() - start  # seconds
        return -1

    def nonRM_txt(self, filename):
        """
        Calculates the time to brute force crack a password

        :param :filename a file name
        :return: returns if the file is a text file and not a README file
        """
        return "readme" not in filename.lower() and filename.endswith(".txt")


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

    print("15 chars, upper, lower, number: ", "fjdknfjASEDE123")
    print(password_handler.brute_force_attack("fjdknfjASEDE123"))

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
