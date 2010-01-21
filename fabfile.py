# *-* coding: utf-8 -*-
import time
import sys
import os

from fabric.api import *
from fabric.contrib.files import upload_template


def setup_server():
    """
    Setup a host server. Run this once before the first deploy.
    """
    # Create the directory that will store deployed packages.
    # Assume we'll have only one project per Dreamhost user.
    run('mkdir -p ~/srv')

    # Prompt for database configurations.
    prompt('What database engine?', 'db_engine', 'mysql')
    prompt('What database name?', 'db_name', 'pythoncampus')
    prompt('What database host?', 'db_host')
    prompt('What database user?', 'db_user')
    prompt('What database password?', 'db_passwd')

    # Render local_settings.py with specific server configurations.
    upload_template('project/local_settings.example',
        '~/srv/local_settings.py', env)

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
    run('pkill python')
    
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
    run('rm -f pythoncampus.org/local_settings.py')
    run('ln -s ~/srv/local_settings.py ~/pythoncampus.org/project/local_settings.py')
