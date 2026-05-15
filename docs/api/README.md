# API Integrations

The Nutanix Automation Factory leverages custom Python scripts to interact with external APIs when native Ansible modules are insufficient or when complex logical abstraction is required.

## Prism Central API (`scripts/python/prism_api_helper.py`)
This helper class abstracts the Prism Central v3 REST API.
- **Authentication:** Basic Auth using Vault-stored credentials.
- **Capabilities:**
  - `get_cluster_list()`
  - `get_vm_list()`
  - `create_vm()`

## ServiceNow Integration (`scripts/python/servicenow_integration.py`)
This helper handles all dynamic ITSM interactions.
- **Capabilities:**
  - `create_incident()`: Opens P3 incidents dynamically upon playbook failure.
  - `update_cmdb_ci()`: Updates existing Configuration Items with drift data (e.g., modified CPU/RAM specs).
