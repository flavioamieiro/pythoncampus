# *-* coding: utf-8 -*-
import time
import sys
import os

from fabric.api import *

env.hosts = ['pythoncampus.org']
env.user = 'pythoncampus'


def setup():
    run('mkdir -p ~/srv')
    # TODO: render template for local_settings.py on remote server

##
# Entry-point commands
##
def deploy(**kwargs):
    "Deploy the contents of a given revision"
    if 'rev' in kwargs:
        rev = kwargs['rev']
    else:
        print 'ERROR: No revision given. Cannot deploy.'
        print 'To deploy the current revision, use the following command:'
        print '$ fab deploy:rev=`git rev-parse HEAD`'
        sys.exit(1)

    stamp = time.strftime("%Y%m%d-%Hh%Mm%Ss")

    #run_test()

    upload_project(rev, stamp)
    set_current(stamp)
    #migrate()
    
    # Tag the deployed revision
    local("git tag -a deploy/%s %s -m ''" % (stamp, rev))
    local("git push --tags")


def upload_project(rev, stamp):
    "Upload project source code to the server"
    # create the local package
    dirname = os.path.dirname(__file__)
    package = '%s.zip' % stamp
    local('cd %s && git archive --format=zip --output=%s --prefix=%s/ %s' % \
        (dirname, package, stamp, rev))

    # put it on the server
    run('mkdir -p ~/srv')
    put(package, '~/srv/%s' % package)

    # unpack it
    with cd('~/srv'):
        run('unzip %s' % stamp)
        run('rm %s' % package)
    
    # local cleanup
    local('rm %s' % package)

        
def migrate():
    "Runs the project's migrations"
    require('project_dir', 'active_project', 'deploy_moment')
    with cd('~/pythoncampus.org'):
        run('./scripts/remote_migrate')


def set_current(stamp):
    "Set a deploy_moment as the current one"
    run('rm -f pythoncampus.org')
    run('ln -s ~/srv/%s pythoncampus.org' % stamp)
