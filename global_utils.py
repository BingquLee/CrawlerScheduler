# -*- coding: utf-8 -*-
import time
import os


def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


def ts2date_min(ts):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(ts))


def today():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def read_files(direction='.'):
    file_list = []
    for file_path, dirs, fs in os.walk(direction):
        # print(file_path, dirs, fs)
        for f in fs:
            if file_path == '.' or file_path == '.\\.idea' or file_path == '.\\.ipynb_checkpoints':
                continue
            file_list.append(os.path.join(file_path, f))
            pass
    return file_list