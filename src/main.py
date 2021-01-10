import requests
import time
timeCount = dict()


def enter():
    urls = dict()
    with open('input.txt', 'r', encoding='utf-8') as info:
        for line in info:
            line = line.rstrip().split(': ')
            urls[line[0]] = line[1]
    return check_start(urls)


def check_start(urls):
    while True:
        online_check(urls)
        time.sleep(60)


def online_check(urls):
    status = dict()
    for url in urls:
        response = requests.get(urls[url])
        if response.status_code == 200:
            response = response.text
            if response.find('Online') == -1:
                status[url] = 'offline'
            else:
                status[url] = 'online'
        else:
            print('Произошла сетевая ошибка, код:', response.status_code)
    return time_counter(status)


def time_counter(status):
    for name in status:
        if status[name] == 'online':
            if name in timeCount:
                timeCount[name] += 1
            else:
                timeCount[name] = 0
    return output(timeCount)


def output(timeCount):
    with open('output.txt', 'a', encoding='utf-8') as outFile:
        print(f'Время вывода: {time.strftime("%d:%m:%y %H:%M", time.gmtime())}', file=outFile)
        for name, count in timeCount.items():
            print(name + ': ', count, 'min', file=outFile)
        print('\n', file=outFile)


enter()

