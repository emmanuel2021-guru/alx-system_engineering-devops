# This script creates a file in /tmp/ with some requirements
file { '/tmp/school':
  ensure  => 'present',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
