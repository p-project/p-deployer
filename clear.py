#!/usr/bin/env python

import yaml
import shutil
from utils import banner

config = yaml.load(open('./config.yml', 'r'))
projects_dir = config['parameters']['projects_dir']


def confirm_removal():
    print(banner.info('BEWARE! All projects will be deleted!'))

    print('History will be lost, and all code in ' + projects_dir + ' folder will be deleted. '
          'There is no coming back. Continue? [y/N] ')

    choice = input().lower()
    if choice != 'y':
        exit(1)


def remove_projects():
    shutil.rmtree(projects_dir)

    print(banner.success('All projects were deleted.'))


if __name__ == '__main__':
    confirm_removal()
    remove_projects()
