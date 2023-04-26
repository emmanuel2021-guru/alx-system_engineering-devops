# This script installs flask from pip3
exec { 'pip3 install flask':
  command => '/usr/bin/pip3 install flask'
}
