# *-* coding: utf-8 -*-
import time
import sys
import os

from fabric.api import *
from fabric.contrib.files import upload_template


# Set the working directory to the root of our repo,
# assuming that fabfile is on it.
os.chdir(os.path.dirname(__file__))


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


def _upload_project(rev, stamp):
    """
    Upload a specified revision to the server
    """
    package = '%s.zip' % stamp

    # Create a zip package with a specified revision.
    local('git archive --format=zip --output=%s --prefix=%s/ %s' % \
        (package, stamp, rev))

    # Put the package on the server.
    put(package, '~/srv/%s' % package)

    # Unpack it on the server.
    with cd('~/srv'):
        run('unzip %s' % stamp)
        run('rm %s' % package)

    # Delete the local zip file
    local('rm %s' % package)


def server_migrate():
    """
    Run syncdb and migrate command on the server
    """
    with cd('~/pythoncampus.org'):
        run('./scripts/remote_migrate')


def _activate_package(stamp):
    """
    Set the server symlink to a specific uploaded package.
    """
    run('rm -f pythoncampus.org')
    run('ln -s ~/srv/%s pythoncampus.org' % stamp)
    run('rm -f pythoncampus.org/local_settings.py')
    run('ln -s ~/srv/local_settings.py ~/pythoncampus.org/project/local_settings.py')
