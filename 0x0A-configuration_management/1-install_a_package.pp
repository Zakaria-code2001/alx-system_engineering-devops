# Installs Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['flask'], # Ensure Flask is installed first
}
