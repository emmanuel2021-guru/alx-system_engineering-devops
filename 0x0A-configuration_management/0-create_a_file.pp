# This script creates a file in /tmp/ with some requirements
school { '/tmp/school':
  ensure => '/tmp/school'
  group => 'www-data'
  owner => 'www-data'
  mode => '0744'
  content => 'I love Puppet'
}
