# Nutanix Automation Factory

Enterprise-grade Nutanix automation factory covering Day-0, Day-1, and Day-2 operations with Ansible Automation Platform, GitHub Actions, ServiceNow, and Nutanix Prism.

## Architecture
- **Hypervisor**: Nutanix AHV
- **Control Plane**: Prism Central
- **Automation**: Ansible (Linux) / GitHub Actions (Windows)
- **ITSM**: ServiceNow

## Quick Start
1. Configure credentials in `group_vars/all.yml` (Use Ansible Vault)
2. Run Day-0: `ansible-playbook -i inventory/prod playbooks/day0_cluster_build.yml`
3. Run Day-1: `ansible-playbook -i inventory/prod playbooks/day1_vm_build_linux.yml`
