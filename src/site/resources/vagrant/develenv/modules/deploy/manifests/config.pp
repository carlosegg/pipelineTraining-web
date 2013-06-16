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
  file { "/etc/hosts":
      content => "127.0.0.1\tlocalhost localhost.localdomain localhost4 localhost4.localdomain4\n::1\tlocalhost localhost.localdomain localhost6 localhost6.localdomain6\n127.0.0.1\t$hostname\n192.168.33.3\tintegration\n192.168.33.4\tqa\n192.168.33.5\tprod-frontend\n192.168.33.6\tprod-backend\n",
    }
}
