#open a file without any error message.
exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/50000" /etc/security/limits.conf',
  path    => 'usr/local/bin/:/bin/',
}

exec { 'change soft -os-configuration-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000" /etc/security/limits.conf',
  path    => 'usr/local/bin/:/bin/',
}
