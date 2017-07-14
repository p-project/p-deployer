#!/usr/bin/env python

import yaml
import sys
import os
from subprocess import call
from utils import banner
from check import check_requirements

conf = yaml.load(open("./config.yml", 'r'))

cloning_method = 'ssh'
if len(sys.argv) > 1 and sys.argv[1] == 'https':
    cloning_method = 'https'


def self_update():
    print(banner.info('Self-updating...'))

    call(['git', 'checkout', 'master'])
    call(['git', 'pull'])


def update_confirmation():
    print(banner.info('Are you sure you want to continue?'))
    print('I will stash potential uncommitted changes, checkout master and pull the last commit from origin. '
          'Continue? [y/N] ')

    choice = input().lower()
    if choice != 'y':
        exit(1)


def update(name, path):
    print(banner.info('Now updating ' + name))

    update_confirmation()

    call(['git', 'stash', 'save'], cwd=path)
    call(['git', 'checkout', 'master'], cwd=path)
    call(['git', 'pull'], cwd=path)


def install(name, url, path):
    print(banner.info('Now installing ' + name))

    print(banner.info('Using ' + cloning_method + ' cloning method'))
    print('You may change the cloning method by passing https or ssh as an argument.')

    call(['git', 'clone', url, path])


def deploy():
    for project_id in conf['projects']:
        project = conf['projects'][project_id]
        path = conf['parameters']['projects_dir'] + '/' + project_id

        if os.path.exists(path):
            update(project['name'], path)
        else:
            install(project['name'], project['repository'][cloning_method], path)

        check_requirements(project_id)

        properties = yaml.load(open(path + '/.p-properties.yml', 'r'))
        for command in properties['install']:
            call(command, shell=True, cwd=path)

    print(banner.success('Deployment is done!'))
    print('Please check execution traces as installation scripts errors are ignored.')
    print('You may also need to pop stashed changes in repositories.')


if __name__ == '__main__':
    self_update()
    deploy()
