# Shell / Command output callback for Ansible

This python script is an Ansible callback you can use to get a decent output of
commands run by your playbooks.

## Setup
Edit your `/etc/ansible/ansible.cfg`:
* `callback_whitelist = cleanoutput`
* `stdout_callback = cleanoutput`
* `callback_plugins = /your/callbacks/folder`

Copy the script to your callbacks folder:
* `cp cleanoutput.py /your/callbacks/folder/`

## Example

```
~ cat example_playbook.yml
---
- hosts: localhost
  tasks:
    - shell: dmesg|tail -n5|cut -c -70
      register: dmesgout
    - debug: msg="{{ dmesgout.stdout }}"

    - shell: ls /notexistingfile
      ignore_errors: true

~ ansible-playbook -i 'localhost,' -c local example_playbook.yml

PLAY [localhost] **************************************************************

TASK [shell] ******************************************************************
changed: [localhost]

TASK [debug] ******************************************************************
ok: [localhost] => {}
MSG:
[16768.355511] i2c /dev entries driver
[18212.031911] perf: interrupt took too long (2501 > 2500), lowering k
[18927.745179] perf: interrupt took too long (3129 > 3126), lowering k
[19890.924800] perf: interrupt took too long (3915 > 3911), lowering k
[24721.153358] perf: interrupt took too long (4897 > 4893), lowering k


TASK [shell] ******************************************************************
fatal: [localhost]: FAILED! => {
    "changed": true,
    "cmd": "ls /notexistingfile",
    "delta": "0:00:00.007585",
    "end": "2018-05-31 16:05:19.651025",
    "rc": 2,
    "start": "2018-05-31 16:05:19.643440"
}
STDERR:
ls: cannot access '/notexistingfile': No such file or directory

MSG:
non-zero return code

...ignoring

PLAY RECAP ********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0

```
