#Puppet to make changes to our configuration file.
file { '/etc/ssh/ssh_config':
ensure  => file,
owner   => 'vagrant',
group   => 'vagrant',
mode    => '0600',
#content =>"Host * \n IdentityFile ~/.ssh/school\n PasswordAuthentication no\n"
#require  => package['openssh-client'],
}
augeas { 'Turn off passwd auth':
  context    => 'file/etc/ssh/ssh_config',
  changes   => ['set PasswordAuthentication no',
  ],
  #require => file['file/etc/ssh/ssh_config'],
}

# Declare identity file
augeas { 'Declare identity file':
  path    => 'file/etc/ssh/ssh_config',
  context    => 'IdentityFile /root/ssh/school',
  #require => file['file/etc/ssh/ssh_config'],
}
