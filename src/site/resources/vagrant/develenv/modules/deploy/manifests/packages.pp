class deploy::packages {
 # Needed packages for develenv installation  
  package {
    'ss-develenv-core':             ensure => installed;
    'ss-develenv-jenkins-examples': ensure => installed;
  }	
}