#!/usr/bin/env python3

import os
import signal

string="Мой кот пришел kill в сад, сад был очень красив, мой кот очень любил этот сад."

list1=string.split(' ')

for word in list1:
    if word=='kill':
        print('Демонстрация killll', word)
        pid = os.fork()
        if pid:
            os.kill(pid, signal.SIGKILL)
            print('Дочерний вывел? Если нет, то он умер\n')
        else:
            print('Меня убили')
        continue
    pid=os.fork()
    if pid:
        wait_signal=os.waitpid(pid, 0)
        print('Ответ процесса', wait_signal[1], 'Пид процесса', pid)
        print()
    else:
        os.execlp('./slave.py', './slave.py', word)
