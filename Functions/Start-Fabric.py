#!/usr/bin/python3
#pip install fabric
#https://docs.python-guide.org/scenarios/admin/
# http://www.fabfile.org/
#  https://docs.fabfile.org/en/2.5/

from fabric.api import cd, env, prefix, run, task

env.hosts = ['hostname']

@task
def memory_usage():
    run('free -m')

