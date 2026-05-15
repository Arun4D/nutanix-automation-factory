# Nutanix Automation Factory - Architecture

This document describes the high-level design and toolchain utilized within the Nutanix Automation Factory.

## Core Toolchain

1. **Hypervisor & Control Plane:** Nutanix AHV + Prism Central. All infrastructure deployments target the Prism Central v3 REST API.
2. **Configuration Management:** Ansible Automation Platform (AAP) is the primary orchestrator for Linux workloads and overall playbook execution.
3. **Windows Automation:** GitHub Actions paired with PowerShell and Desired State Configuration (DSC) drive Windows server baselining and patching.
4. **ITSM / CMDB:** ServiceNow. All builds dynamically register as Configuration Items (CIs), and Day-2 operations open Change Requests (CRs) before execution.

## Repository Structure

```text
nutanix-automation-factory/
├── group_vars/          # Environment variables and Vault secrets
├── inventory/           # Static and dynamic inventory definitions (dev/prod/dr)
├── playbooks/           # Core orchestrations (Day-0, Day-1, Day-2)
├── roles/               # Reusable, modular task sets (baselining, patching)
├── scripts/             # Python API helpers and PowerShell scripts
├── github-actions/      # Windows CI/CD pipelines
└── docs/                # Comprehensive documentation
```

## Security & Audit
- **Secrets Management:** Ansible Vault is used for all sensitive data (passwords, API keys).
- **Audit Logging:** The `audit_export.py` script ensures every major operation (builds, patches, decommissions) is centrally logged in `logs/audit/` in structured JSON format.
