# Using strace, find out why Apache is returning a 500 error.
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php && echo "" >> /root/alx-system_engineering-devops/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp',
  path    => ['/usr/local/bin', '/bin'],
}

