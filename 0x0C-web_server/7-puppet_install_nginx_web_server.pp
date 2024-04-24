#!/usr/bin/env bash
#practice configuring your server with Puppet!
package { 'nginx':
ensure   => present,
provider => 'apt',
}
file {'/etc/nginx/sites-available/default':
  ensure    => file,
  content  => "server {
  	listen 80 default_server;
	location / {
	return 200 'Hello World!';
}
}"
