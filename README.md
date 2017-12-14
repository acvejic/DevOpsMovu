# DevOpsMovu
Test task for Senior DevOps position at Holycode - Movu project

Test environment:
  - Centos 7 or Ubuntu 16.04.3
  - Ansible 2.3.2.0
  - Python 2.7.5
  - Dopy (pip install dopy)

Prerequisites for integration with Digitalocean:
- API token from Digitalocean (https://cloud.digitalocean.com/settings/api/tokens)
  - saved in host_vars/localhost.yml - api_token variable
- ssh-key of the host mashine to Digitalocean account (https://cloud.digitalocean.com/settings/security)
  - add name of the key to host_vars/localhost.yml - ssh_key variable


Provision new VM on Digitalocean using playbook newVM.yml
 * ansible-playbook newVM.yml

Task 1.
  - Assume that you're getting "Too many open files" errors in logs and write an Ansible playbook which will set this limit to higher value.
  - Solution implemented in role "increaseUlimit"

Task 3.a
  - Install nginx mode Passanger
  - Solution implemented in role "nginx"
  
Task 3.b
  - Install potgresql and setup user
  - Solution implemented in role "postgresql"

Task 3.c
  - Install RVM and Ruby 2.2.4
Task 3.d
  - Initialize empty rails app
Task 3.e
  - Configure Nginx to server rails app
 
Solution for tasks 3.c, 3.d and 3.e implemented in role "ruby"

To provision VM with all neccesary software run playbook provisionVM.yml
  - ansible-playbook provisionVM.yml

Task 2
  - Python script to get IP info and save to DB
