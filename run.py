#!/usr/bin/env python

import yaml
import os
import sys
from subprocess import Popen
from time import sleep
from utils import banner

conf = yaml.load(open("./config.yml", 'r'))


def start_all():
    print(banner.info('Starting all applications'))

    processes = []
    for project_id in conf['projects']:
        project = conf['projects'][project_id]
        path = conf['parameters']['projects_dir'] + '/' + project_id

        if not os.path.exists(path):
            print(banner.info('Ignoring ' + project['name'] + ' (not installed)'))
            continue

        properties = yaml.load(open(path + '/.p-properties.yml', 'r'))

        if 'run' not in properties:
            print(banner.info('Ignoring ' + project['name'] + ' (no running configuration)'))
            continue

        for command in properties['run']:
            print(banner.info('Starting ' + project['name']))

            processes.append(Popen(command, shell=True, cwd=path))
            sleep(2)

    print(banner.success('All projects started!'))
    print('Press Ctrl-C to quit.')

    for process in processes:
        try:
            process.wait()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    start_all()
