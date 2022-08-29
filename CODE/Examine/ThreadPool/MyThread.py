from threading import Thread

def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=('线程1',))
    t1.start()
    t2 = Thread(target=func('线程2'))
    t2.start()
