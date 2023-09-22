#execute pkill command to kill a process named killmenow by creating a manifest using puppet

exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
