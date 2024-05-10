# Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet

exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/'
}
