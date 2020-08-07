#!/usr/bin/python
# -*- coding: utf-8 -*-
import random as r
import string


def letter():
    return r.choice(string.ascii_letters)


def loCase():
    return r.choice(string.ascii_lowercase)


def upCase():
    return r.choice(string.ascii_uppercase)


def digit():
    return r.choice(string.digits)


def symbol():
    return r.choice(string.punctuation)


def all():
    randomCharList = [letter(), digit(), symbol()]
    return r.choice(randomCharList)


if __name__ == "__main__":
    print("\nThis module was created by fr4nkl1n-1k3h\n")
