# This script fixes an apache web server returning a 500 error

exec { 'wordpress-fix':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
