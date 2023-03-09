import time

def hhh(func):
    def sss():
        with open('./eee.txt', 'w', encoding='utf-8') as f:
            f.write(str(func()))

    return sss


@hhh
def ddd():
    return 'qwert'

def get_now():
    return time.time()

def test():
    dd = get_now()
    print(dd)
    if dd:
        test()

if __name__ == '__main__':
    test()
