#Updating config to refuse password authentication using puppet
file { '/etc/ssh/sshd_config':
  ensure  => 'file',
  content => file(/etc/ssh/sshd_config).content.gsub('#PasswordAuthentication yes', 'PasswordAuthentication no'),
}
