##########################################################
# Puppet profile for install develenv                    # 
#--------------------------------------------------------#
# Review administratorId, password and profile variables # 
# and apply the profile with:                            #
# puppet apply deploy-develenv.pp                        #
##########################################################    
# Review administratorId, password and profile variables
$administratorId="develenv"
$password="develenv"
# Configuration profile
#Select a profile (softwaresanoProfile, tidProfile, googleProfile,...)
$tidProfile="http://develenv.googlecode.com/svn/trunk/develenv/src/main/filters/tid.properties"
$softwaresanoProfile="http://develenv.googlecode.com/svn/trunk/develenv/src/main/filters/softwaresano.properties"
$googleProfile="http://develenv.googlecode.com/svn/trunk/develenv/src/main/filters/google.properties"
$profile=$softwaresanoProfile
#---------------------------------------------------------
# Develenv repository section   
# Select repository where develenv is available.
#---------------------------------------------------------
#Select yum repository for install develenv(develenvWithVagrant, develenvInTid, develenvProduction)
$develenvInTid="http://artifacts.hi.inet/develenv/noarch/ss-develenv-repo-1.0-0.0.noarch.rpm"
# For development develenv in vagrant use
$develenvWithVagrant="http://develenvms.softwaresano.com/public/downloads/repos/vagrant/ss-develenv-repo-1.0-0.0.noarch.rpm"
#Repo with develenv production repo
$develenvProduction="http://develenvms.softwaresano.com/public/downloads/repos/ss-develenv-repo-1.0-0.0.noarch.rpm"
$develenvrpmrepo=$develenvProduction
$javaurlrepo = "http://servilinux.hi.inet/java/yum/7/\$basearch"
class{'deploy': }

 
