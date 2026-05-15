# Rollback Strategies

Automated rollback strategies are a critical component of the Day-2 operations pipeline.

## Pre-Patching Snapshots
All Day-2 patching playbooks (`day2_patch_linux.yml`, `day2_patch_windows.yml`) contain a `pre_tasks` block that leverages the `nutanix.ncp.vm_snapshot` module.

```yaml
- name: Create Pre-Patching Snapshot in Nutanix
  nutanix.ncp.vm_snapshot:
    pc_ip: "{{ nutanix_prism_central_ip }}"
    username: "{{ nutanix_prism_username }}"
    password: "{{ nutanix_prism_password }}"
    vm_name: "{{ inventory_hostname }}"
    snapshot_name: "PRE-PATCH-{{ ansible_date_time.date }}"
```

### Executing a Rollback
If a patch causes application failure:
1. Log into Prism Central.
2. Locate the impacted VM.
3. Select the `PRE-PATCH-*` snapshot.
4. Select **Restore**.
5. Once restored, update the associated ServiceNow Change Request with a `failure` close code.
