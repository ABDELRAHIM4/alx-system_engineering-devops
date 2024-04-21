#Puppet to make changes to our configuration file.
file { '/etc/ssh/ssh_config':
ensure => present,
}
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  #context    => 'file/etc/ssh/ssh_config',
  line  =>  'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  #require => file['file/etc/ssh/ssh_config'],
}

# Declare identity file
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile /root/ssh/school',
  match => '^IdentityFile',
#require => file['file/etc/ssh/ssh_config'],
}
