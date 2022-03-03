#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Random password generator and password security checker

    @author: sedonathomas
"""

import random
import string
import time


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
        return self.search_time(password)

    def search_time(self, password):
        possible_passwords = self.search_space(password)
        computation_time = self.runtime_test()
        return possible_passwords * computation_time

    def search_space(self, password):
        possibilities, pw_set = 0, set(password)
        for s in [self.lowercase, self.uppercase, self.numbers, self.punctuation]:
            if len(set(s).intersection(pw_set)) > 0:
                possibilities += len(self.lowercase)
        return (possibilities ** len(password))

    def runtime_test(self):
        length = 100
        start = time.time()  # seconds
        li = [random.choice(self.characters) for i in range(length)]
        end = time.time()  # seconds
        return ((end - start) / length) / (60 * 60 * 24)  # days


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

    print("password")
    print(password_handler.brute_force_attack("password"))
