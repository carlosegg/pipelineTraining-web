class deploy {
  include deploy::config
  include deploy::users
  include deploy::yumrepos
  include deploy::packages
  Class['config'] -> Class ['users'] -> Class [ 'yumrepos' ] -> Class ['packages']
}