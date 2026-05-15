Build complete nutanix-automation-factory repo exactly as defined in
.github/copilot/agents/nutanix-automation-factory-architect.agent.yaml

Requirements:
- Create exact folder structure
- Build Day-0 / Day-1 / Day-2
- Ansible for Linux
- GitHub Actions for Windows
- Shell/Python/PowerShell scripts
- ServiceNow integration
- Audit + rollback
- README + docs 

---
**STATUS UPDATE:**
The initial project scaffolding has been successfully built according to these requirements. All core Playbooks (Day 0, 1, 2), GitHub Actions workflows, ServiceNow API scripts, and modular roles are initialized. We can now proceed with expanding individual modules iteratively.

**STATUS UPDATE (Phase 2):**
- Day-0: Fully expanded to include Foundation, Network/VLAN, image baseline, and prechecks.
- Day-1 (Windows): Expanded to include Crowdstrike, Datadog, and Rubrik agent orchestration.
- Day-2: Compliance playbooks created for Defender validation and DSC drifting checks.
