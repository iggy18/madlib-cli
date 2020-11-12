import re
seeker = re.compile(r'{.*?}')

def greet ():
    print("welcome to this madlib. you know what to do...")


def read_template():
    with open('assets/text.txt', 'r') as file:
        open_file = file.read()

def parse(file):
    return re.findWords(seeker, file)


def merge():
    print("three")

greet()
read_template()
parse()
