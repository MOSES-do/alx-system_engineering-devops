# Update nginx.conf to allow it accept and serve more requests

exec {'modify maximum open files limit setting':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}


#exec { 'modify max open files limit setting':
#  command => 'sed -i "s/^worker_rlimit_nofile.*/worker_rlimit_nofile 10000;/" /etc/nginx/nginx.conf && systemctl restart nginx',
#  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
#}
