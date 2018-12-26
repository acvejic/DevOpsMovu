# DevOpsMovu

Holycode - Movu project

Test environment:
  - Ubuntu 16.04.3
  - Ansible 2.4.2.0 (https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-16-04)
  - Python 2.7.12
  - Pip (apt-get install python-pip)
  - Dopy (pip install dopy)

Prerequisites for integration with Digitalocean:
- API token from Digitalocean (https://cloud.digitalocean.com/settings/api/tokens)
  - saved in host_vars/localhost.yml - api_token variable
- ssh-key generated - will be added to Digitalocean account
 

************************************************************
                Create new VM on Digitalocean
                  ansible-playbook newVM.yml
************************************************************

Task 1.
  - Assume that you're getting "Too many open files" errors in logs and write an Ansible playbook which will set this limit to higher value.
  - Solution implemented in role "increaseUlimit"

        ansible-playbook provisionVM.yml --tags "increaseUlimit"


Task 3.a
  - Install nginx mode Passanger
  - Solution implemented in role "nginx"

        ansible-playbook provisionVM.yml --tags "nginx"
 
Task 3.b
  - Install potgresql and setup user
  - Solution implemented in role "postgresql"

        ansible-playbook provisionVM.yml --tags "postgresql"

Task 3.c
  - Install RVM and Ruby 2.2.4

Task 3.d
  - Initialize empty rails app

Task 3.e
  - Configure Nginx to point to rails app
 
Solution for tasks 3.c, 3.d and 3.e implemented in role "ruby"

      ansible-playbook provisionVM.yml --tags "ruby"


************************************************************************

    To provision VM with all neccesary software run playbook provisionVM.yml
  
                  ansible-playbook provisionVM.yml

************************************************************************

Task 2
  - Python script to get IP info and save to DB
  
  For convience VM created in task 2 is used.
  SSH password authentification is disabled, use same ssh key, if you want to enable password authentification
  edit /etc/ssh/sshd_config by adding "PasswordAuthentication yes" and restart sshd service.
  Also for faster development following are used:
      db_user = 'ror_app'
      db_password = 'testpass'
      db_name = 'geo_test'
      db_table_name = 'geo_test_data'
  That parametars are configurable in script

  Dependencies:
   - Pip (apt install python-pip)
   - requests (pip install requests)
   - psycopg2
   - xmltodict
  
  To run script:
      cd script
      ./geoip.py 8.8.8.8
          


TODO: 
  - move some of the "ugly" shell module solutions to ansible modules
  - further investigation regarding runtime javasript -nodejs dependency
  - parametrize varibales: app name, password, user etc
  - store sensitive data (passwords, sshkeys, API tokens etc.) in Vault
