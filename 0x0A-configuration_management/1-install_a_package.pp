# Install flask using puppet and pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  command  => '/usr/bin/python3 -m pip',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
