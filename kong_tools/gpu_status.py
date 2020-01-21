#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
import time
import shutil


def subjob(script_name):
    datasci_node = [412, 413, 414, 415, 416, 429, 430, 437, 438, 439]
    for node_index in datasci_node:
        os.system('qsub -l hostname=node%d %s' % (node_index, script_name))

    return len(datasci_node)


def check_files(prefix, num_files):
    time.sleep(30)
    try:
        files = [i for i in os.listdir(os.curdir) if prefix in i]
    except:
        print('The first time try...')
    count = 1
    while len(files) < num_files - 1:
        count += 1
        print('The %d times try...' % count)
        time.sleep(5)
        files = [i for i in os.listdir(os.curdir) if prefix in i]

    return files


def read_contents(filename):
    nodeNameIndex = 6
    contents_index = 25
    with open(filename, 'r') as f:
        data = f.readlines()

        if len(data) < 2:
            os.system('qdel %s' % filename[-7:])
            return ['This node is busy\n']
        else:
            return data[nodeNameIndex:nodeNameIndex + 1] + \
                   data[contents_index:-1] + ['\n']


def write_outputs(data):
    new_data = ['Below is datasci nodes\'s GPU status:\n',
                '=================================\n'] + data
    with open('NodeGpuStatus.out', 'w') as f:
        f.writelines(new_data)


if __name__ == '__main__':

    script_name = 'ViewGpuStatus.sh'
    num_files = subjob(script_name)
    print(num_files)
    prefix = 'DatasciNodeGpuStatus.o'
    file_list = check_files(prefix, 7)
    data = []
    file_list.sort()
    for files in file_list:
        data += read_contents(files)
    write_outputs(data)
    os.system('rm DatasciNodeGpuStatus.*')
