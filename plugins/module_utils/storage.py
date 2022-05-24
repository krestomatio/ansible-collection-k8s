from __future__ import absolute_import, division, print_function
__metaclass__ = type

import math
from ansible.module_utils.facts.hardware import linux
from ansible.module_utils.facts.utils import get_mount_size


def get_mount_info(module):
    lh = linux.LinuxHardware(module)
    bind_mounts = lh._find_bind_mounts()
    mtab_entries = lh._mtab_entries()
    mount_info = {}
    for fields in mtab_entries:
        # Transform octal escape sequences
        fields = [lh._replace_octal_escapes(field) for field in fields]

        (device, mount, fstype, options) = (fields[0], fields[1],
                                            fields[2], fields[3])

        if ((not device.startswith('/') and ':/' not in device)
                or (fstype == 'none')
                or (module.params['path'] != mount)):
            continue

        mount_info = get_mount_size(mount)
        mount_info['mount'] = mount
        mount_info['device'] = device
        mount_info['fstype'] = fstype
        mount_info['options'] = options

        if mount in bind_mounts:
            # only add if not already there, we might have a plain /etc/mtab
            if not lh.MTAB_BIND_MOUNT_RE.match(options):
                mount_info['options'] += ',bind'

        if module.params['path'] == mount:
            break

    return mount_info


def b_to_gib(bytes):
    gib = round(int(bytes) / 1024 ** 3, 1)
    return gib


def below_twenty_pct(size_available, size_total):
    float_size_total = float(size_total)
    float_size_available = float(size_available)

    if float_size_total < 0 or float_size_available < 0:
        return False

    return bool(percentage(float_size_available, float_size_total)
                < 20.0)


def percentage(part, whole):
    return round(100 * float(part) / float(whole), 1)


def recommended_size_gib(
    current_gib,
    increment_gib=25,
    cap_gib=1000,
    expansion_required=False,
):

    float_cap_gib = float(cap_gib)
    float_current_gib = float(current_gib)
    float_increment_gib = float(increment_gib)

    # get next bigger multiple of 'increment_gib' from 'current_gib'
    autoexpand_gib = math.ceil(float_current_gib / float_increment_gib) \
        * float_increment_gib

    # Increment GiB (value from 'increment_gib') as long as expansion is required and
    # 'current_gib' is 20% closer to next bigger multiple of 'increment_gib'
    if expansion_required and float_current_gib > autoexpand_gib * 0.8:
        autoexpand_gib += float_increment_gib

    # Return 'autoexpand_gib' unless cap is reached
    if autoexpand_gib < float_cap_gib:
        return autoexpand_gib
    else:
        return float_cap_gib
