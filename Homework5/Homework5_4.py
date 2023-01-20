from datetime import datetime


def decor(time):
    print(datetime.now())
    return time


@decor
def example1(i):
    if i != 1:
        return i * (i - 1)
    else:
        return i


@decor
def example2(x):
    x = x.replace(' ', '')
    if len(x) > 20:
        print('Слово содержит больше 20 букв')
        return x
    else:
        print('Слово содержит больше 20 букв')
        return x


print(example1(3))
print(example2('I am a student at TeachMeSkills'))
