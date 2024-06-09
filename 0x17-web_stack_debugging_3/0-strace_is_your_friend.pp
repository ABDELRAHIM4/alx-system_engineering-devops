#Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/use/local/bin/:/bin/'
}
file_line { 'append_newline':
  path  => '/root/alx-system_engineering-devops/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp',
  line  => '',
  match => '\n$',
}
