#!/bin/bash

set -x

# Script to correct repo package

# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi


# Erasing the incorrect package
chattr -i /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm 
rm /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm

# Moving the correct one and changing context and extended attrib
cp ./ss-develenv-repo-1.0-0.0.noarch.rpm /home/develenv/app/repositories/rpms/noarch/
chcon -t httpd_sys_content_t /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm
chattr +i /home/develenv/app/repositories/rpms/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm

# Creating repo
createrepo -s sha -d --update /home/develenv/app/repositories/rpms/noarch

# Installing the correct version of pipeline_plugin
# First erase the data on destination dir:
rm -rf /home/develenv/app/plugins/pipeline_plugin
tar -xvzf ./pipeline_plugin.tar.gz -C /home/develenv/app/plugins/
