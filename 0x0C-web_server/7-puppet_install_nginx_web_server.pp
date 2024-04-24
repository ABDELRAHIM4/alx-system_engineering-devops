#!/usr/bin/env bash
#practice configuring your server with Puppet!
package { 'nginx':
ensure   => present,
provider => 'apt',
}
