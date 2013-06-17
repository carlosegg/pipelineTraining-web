from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, put
from fabric.contrib.console import confirm

def upload_repo():
  put('./modules/deploy/files/ss-develenv-repo-1.0-0.0.noarch.rpm', '/tmp')
  with cd('/root'):
    run('chattr -i /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm')
    run('rm /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm')
    run('mv /tmp/ss-develenv-repo-1.0-0.0.noarch.rpm /home/develenv/app/repositories/rpms/noarch')
    run('chcon -t httpd_sys_content_t /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm')
    run('chattr +i /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarhc.rpm')
    run('createrepo -s sha -d --update /home/develenv/app/repositories/rpms/noarch')
