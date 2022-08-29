from concurrent.futures import ThreadPoolExecutor


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(10000):
            t.submit(func, f'任务{i}')
