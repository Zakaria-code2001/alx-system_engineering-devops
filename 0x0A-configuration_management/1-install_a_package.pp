# installs the package puppet-lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
} 
# Installs the package Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['puppet-lint'],
}
