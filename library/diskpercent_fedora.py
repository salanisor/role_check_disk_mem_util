#!/usr/bin/env /usr/libexec/platform-python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, canit00 <[email protected]>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: diskpercent_fedora
short_description: Gathers disk percent utilization
description:
    - Determines local path and gathers utilization %
    - If % >= 85% raise alert
version_added: "2.7"
options:
  path:
    description:
      - The local volume to query
    required: yes
    type: path
author:
    - @canit00
'''

RETURN = '''
msg:
    description: Just returns volume information
    returned: always
    type: dict
    sample: {"changed": false, "/var/lib/docker": [0.3], "/var/lib/containers": [0.2], "/var/lib/openshift": [0.3]}
'''

EXAMPLES = '''
- name: check disk utilization %
  diskpercent_fedora:
    path: "/"
  register: disk
  when: ansible_distribution == "Fedora"

- name: check disk utilization %
  diskpercent_fedora:
    path: "{{ item }}"
  loop:
  - /
  - /tmp
  register: disk
  when: ansible_distribution == "Fedora"
'''

import psutil,json,os
from ansible.module_utils.basic import AnsibleModule

def main():
    result = dict(
        changed=False,
        disk_utilization='',
        disk_threshold=False
    )

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='list', required=True)
        )
    )

    path = module.params
    volumes = path['path']
    disk_threshold = False

    for vol in volumes:
        path_exists = os.path.exists(vol)
        if not path_exists:
            module.fail_json(rc=257, changed=False, msg='Volume %s does not exist !' % vol)
            continue
        else:
            for vol in volumes:
                disk_usage = psutil.disk_usage(vol)
                if disk_usage.percent < 85.0:
                    result['disk_utilization'] = disk_usage.percent
                elif disk_usage.percent >= 85.0:
                    result['disk_utilization'] = disk_usage.percent
                    result['disk_threshold'] = True
                    result['changed'] = True

        '''module.exit_json(disk_threshold=disk_threshold, disk_utilization=disk_utilization)'''
        module.exit_json(**result)
            
if __name__ == '__main__':
    main()
