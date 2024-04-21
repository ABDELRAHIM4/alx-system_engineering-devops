#Puppet to make changes to our configuration file.
file { '/home/vagrant/.ssh/config':
ensure  => file,
owner   => 'vagrant',
group   => 'vagrant',
mode    => '0600',
content =>"Host * \n IdentityFile ~/.ssh/school\n PasswordAuthentication no\n"
}
