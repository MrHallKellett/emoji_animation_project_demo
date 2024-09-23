from time import sleep
from os import system
from sys import stdout
from random import randrange, choice
from unicodedata import east_asian_width

clear = lambda : system("clear")

DELAY = 0.0001

def dprint(*strings, end="\n"):
    for string in strings:
        for char in str(string):
            stdout.write(char);
            stdout.flush()
            sleep(DELAY)
    stdout.write(end)

HALF2FULL = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
HALF2FULL[0x20] = 0x3000
    
def fullen(s):
    '''
    Convert all ASCII characters to the full-width counterpart.
    '''
    return str(s).translate(HALF2FULL)

SPACE = fullen(" ")


MSG = fullen("Y8 CODING EMOJI ANIMATION PROJECT")
WIDTH = len(MSG) + 6
HEIGHT = 20


ANIMALS = """🐵
🐒
🦍
🦧
🐶
🦮
🐩
🐺
🦊
🦝
🦄
Unicorn
🦓
Zebra
🦌
Deer
🦬
Bison
🐮
Cow Face
🐂
Ox
🐃
Water Buffalo
🐄
Cow
🐷
Pig Face
🐖
Pig
🐗
Boar
🐽
Pig Nose
🐏
Ram
🐑
Ewe
🐐
Goat
🐪
Camel
🐫
Two-Hump Camel
🦙
Llama
🦒
Giraffe
🐘
Elephant
🦣
Mammoth
🦏
Rhinoceros
🦛
Hippopotamus
🐭
Mouse Face
🐁
Mouse
🐀
Rat
🐹
Hamster
🐰
Rabbit Face
🐇
Rabbit
🐿️
Chipmunk
🦫
Beaver
🦔
Hedgehog
🦇
Bat
🐻
Bear
🐻‍❄️
Polar Bear
🐨
Koala
🐼
Panda
🦥
Sloth
🦦
Otter
🦨
Skunk
🦘
Kangaroo
🦡
Badger
🐾
Paw dprints""".splitlines()

ANIMALS = [a for a in ANIMALS if len(a) == 1]

clear()

def act1():
    for anim in ANIMALS[:HEIGHT // 2]:
        dprint(anim * WIDTH)
        sleep(0.1)

    for a in fullen("🦓🦓 " + MSG + " 🦓🦓"):
        dprint(a, end="")
        sleep(0.1)
    dprint()

    for anim in reversed(ANIMALS[:HEIGHT // 2]):
        dprint(anim * WIDTH)
        sleep(0.1)

    sleep(1)
    clear()

def act2():

    t = 0.5
    spacer = 1
    up = True
    words = "your task is to create THE best emoji animation possible ... your deadline is Wednesday 9th October!!!".split()
    for i, (anim, word) in enumerate(zip(ANIMALS, words)):
        dprint(spacer * fullen(" "), anim, "    ", word)
        sleep(t)
        if spacer > len(words) // 2:
            up = False
        if up:
            spacer += 1
        else:
            spacer -= 1
        t *= 0.9

    sleep(3)

    clear()

def act3():
    width = 50
    height = HEIGHT
    for word in "BUT THAT'S NOT ALL !!!".split():
        x = randrange(0, len(ANIMALS) - 5)
        animals = ANIMALS[x:x+(width//10)] * (width//5)
        word = SPACE + word + SPACE
        for i in range(height):
            a = list(animals)
            for j, w in zip((-1, 0, 1), (SPACE * len(word), word, SPACE * len(word))):
                if i == (height // 2) + j:
                    for x, char in enumerate(fullen(w)):
                        a[width//2 - (len(w) // 2) + x] = char
            print("".join(a))
            animals.append(animals.pop(0))
        sleep(1)
        clear()



def act4():
    w = 40
    txt = [fullen("""YOUR PROJECT MUST:"""), ""] + ["✅" + item for item in ("""Follow the theme you have been given........
Have a funny/unique/interesting storyline...
Make use of Python techniques e.g. FOR LOOPS""").splitlines()]

    for i in range(HEIGHT // 2):
        txt = [""] + txt
        txt = txt + [""]

    for i, line in enumerate(txt):

        

        a = "a"
        while east_asian_width(a) != "W":
            a = choice(ANIMALS)
        line_length = len(line)
        if i > 2:
            line_length //= 2

        length = w - line_length
        

        line = a*(length //2) + line + a * (length // 2)

        print(line)
        sleep(0.1)
    sleep(5)
    clear()

       

act1()
act2()
act3()
act4()
