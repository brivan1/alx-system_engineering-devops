# using Puppet to  install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  creates => '/usr/local/lib/python3.*/dist-packages/flask',
  require => Package['python3-pip'],
}
