import yaml
import os
from subprocess import call
from utils import banner


def check_result(res):
    if res == 0:
        print(' ✓')
    else:
        print(' ✗')

    return res


def check_requirements(project_id):
    res = 0
    conf = yaml.load(open('config.yml', 'r'))
    path = conf['parameters']['projects_dir'] + '/' + project_id
    properties = yaml.load(open(path + '/.p-properties.yml', 'r'))

    print(banner.info('Checking requirements for ' + conf['projects'][project_id]['name']))

    dependencies = properties['dependencies']
    for bin_dependency in dependencies.get('bin', []):
        print('Checking if ' + bin_dependency + ' is installed...', end='')
        res = check_result(call(['which', bin_dependency], stdout=open(os.devnull, 'w'))) or res

    for script_dependency in dependencies.get('script', []):
        print('Running script ' + script_dependency + '...', end='')
        res = check_result(call(script_dependency, shell=True, stdout=open(os.devnull, 'w'))) or res

    if res:
        print(banner.error('Some requirements are missing!'))
        print('Check the script trace and run the update script to finish installation.')
        exit(res)
    else:
        print(banner.success('Your system meets requirements'))
