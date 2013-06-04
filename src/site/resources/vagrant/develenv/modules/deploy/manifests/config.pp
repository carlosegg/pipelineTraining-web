class deploy::config {
  define develenvconfig($administratorId="develenv", $password="develenv", $profile="http://develenv.googlecode.com/svn/trunk/develenv/src/main/filters/softwaresano.properties") {
    $str = "-Dadministrator.id=$administratorId -Dpassword=$password -Dorg=$profile"
    file { "/etc/develenv/":
      ensure  => directory
    }
    file { "/etc/develenv/develenv.properties":
      content => "$str",
      require => File['/etc/develenv'],
    }
  }

  develenvconfig{'config':
    administratorId => $administratorId,
    password        => $password,
    profile         => $profile,
  }
}