class deploy::yumrepos {
  class {'::yumrepos':
    repos   => [javarepo,develenv]
  }
}