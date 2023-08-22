# Increases the amount of traffic an Nginx server can handle.

exec { 'nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
