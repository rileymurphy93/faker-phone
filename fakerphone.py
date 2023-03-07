#!/usr/bin/env python3

from faker import Faker

f = Faker(["en_US"])

for i in range(5):
    print(f.phone_number())