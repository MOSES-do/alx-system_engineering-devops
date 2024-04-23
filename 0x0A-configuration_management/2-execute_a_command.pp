#Kill a runnning process

exec { 'kill_process':
  command => 'kill 17818',
  onlyif  => 'ps -p 17818',
}
