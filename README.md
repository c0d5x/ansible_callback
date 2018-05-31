=Shell / Command output callback=

This python script is an Ansible callback you can use to get a decent output of
commands run by your playbooks.

==Setup==
Edit your `/etc/ansible/ansible.cfg`:
* `callback_whitelist = cleanoutput`
* `stdout_callback = cleanoutput`
* `callback_plugins = /your/callbacks/folder`

Copy the script to your callbacks folder:
* `cp cleanoutput.py /your/callbacks/folder/`

==Example==

```ansible-playbook -i 'localhost,' -c local example_playbook.yml ```
