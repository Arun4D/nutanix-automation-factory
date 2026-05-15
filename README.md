# Nutanix Automation Factory

Welcome to the **Nutanix Automation Factory**, an enterprise-grade infrastructure-as-code repository designed to automate the entire lifecycle of a Nutanix-based virtualization environment.

This project uses a decoupled, Multi-Agent architecture to orchestrate Nutanix Foundation, Prism Central, Ansible Automation Platform, GitHub Actions, and ServiceNow into a seamless CI/CD pipeline.

---

## 🏗️ Architecture Overview

The factory is divided into distinct operational phases:

- **Day-0 (Cluster Build):** Automated hardware validation, IPAM/DNS checks, Nutanix Foundation deployment, and Prism Central registration.
- **Day-1 (Provisioning):** Golden image cloning, Active Directory domain joining, OS baselining, and enterprise agent orchestration (CrowdStrike, Datadog, Rubrik) for both Windows and Linux endpoints.
- **Day-2 (Operations):** Automated patch orchestration (with pre-patch Nutanix snapshots), DSC compliance validation, Defender signature enforcement, and DR failovers.

---

## 🚀 Quick Start

### 1. Prerequisites
- Nutanix AHV Cluster & Prism Central (v3 API enabled)
- Ansible Automation Platform (AAP)
- GitHub Actions runners (for Windows DSC/PowerShell tasks)
- ServiceNow Instance (for ITSM integration)

### 2. Configuration
All environment-specific variables are managed via Ansible Vault. Populate the following files in the `group_vars/` directory before running any playbooks:
- `group_vars/all.yml` (Global variables and secrets)
- `group_vars/nutanix.yml` (Cluster-specific overrides)
- `group_vars/windows.yml` (Windows domain and agent configurations)
- `group_vars/linux.yml` (Linux baseline variables)

### 3. Execution Example (Day-1 Provisioning)
```bash
ansible-playbook -i inventory/prod/hosts playbooks/day1_vm_build_linux.yml --ask-vault-pass
```

---

## 🤖 Copilot Multi-Agent Architecture

This repository contains specialized AI agents designed to assist engineers in extending the factory's capabilities. They can be found in `.github/copilot/agents/`:
- `day0.agent.yaml`: For expanding cluster deployment logic.
- `day1.agent.yaml`: For adding new OS baselines and agent deployments.
- `day2.agent.yaml`: For expanding patching and compliance scripts.
- `servicenow.agent.yaml`: For modifying ITSM API integrations.

---

## 📚 Documentation Navigation
For deep dives into specific operational areas, refer to the `docs/` directory:
- [Architecture Details](docs/architecture/README.md)
- [Operational Runbooks](docs/runbooks/README.md)
- [Rollback Strategies](docs/rollback/README.md)
- [API Integrations](docs/api/README.md)
