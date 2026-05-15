# Operational Runbooks

These runbooks provide step-by-step instructions for executing the automated pipelines within the Nutanix Automation Factory.

## Day-0: Cluster Deployment
1. Ensure `group_vars/nutanix.yml` is populated with the correct target nodes and IPAM details.
2. Ensure the Nutanix Foundation VM is accessible.
3. Execute the playbook:
   ```bash
   ansible-playbook -i inventory/dev/hosts playbooks/day0_cluster_build.yml
   ```
4. Verify the new cluster appears in Prism Central and the CMDB CI is created in ServiceNow.

## Day-1: Windows Server Provisioning
1. This workflow is primarily driven via GitHub Actions (`github-actions/windows-build.yml`).
2. Trigger the Action manually via the GitHub UI (`workflow_dispatch`), providing the `vm_name` and `cluster` inputs.
3. The pipeline will invoke the Prism API to clone the Golden Image, and then execute the PowerShell baselining script via WinRM.

## Day-2: Patching (Linux)
1. Ensure the target hosts are listed in the correct inventory group (`linux_servers`).
2. Execute the playbook:
   ```bash
   ansible-playbook -i inventory/prod/hosts playbooks/day2_patch_linux.yml
   ```
3. The playbook will take a Nutanix Snapshot, open a ServiceNow CR, patch the OS via DNF, reboot if necessary, and close the CR.
