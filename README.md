Role Name
---------

It provides disk and memory threshold checks for 85% utilization. 


Requirements
------------
- Ansible 2.4 or higher
- Red Hat Enterprise Linux 7, Fedora, CentOS

Dependencies
------------

- Python psutil library (python2-psutil.x86_64|python3-psutil.x86_64)

Example Playbook
----------------
```
---
- hosts: 127.0.0.1
  connection: local
  gather_facts: true
  roles:
  - {role: role_check_disk_mem_util}
```

License
-------

GPLv3

Author Information
------------------
Author Name @canit00
