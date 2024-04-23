# Install flask using puppet and pip3

exec {'install_flask_with_pip3':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['usr/bin', '/usr/local/bin'],
  unless  => 'usr/bin/pip3 show flask | grep Version | grep 2.1.0'
}

exec {'install_werkzeug_with_pip3':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  path    => ['usr/bin', '/usr/local/bin'],
  unless  => 'usr/bin/pip3 show werkzeug | grep Version | grep 2.1.1'
}
