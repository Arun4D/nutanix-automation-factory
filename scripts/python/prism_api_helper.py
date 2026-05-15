import requests
import json
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class PrismCentralAPI:
    def __init__(self, pc_ip, username, password):
        self.pc_ip = pc_ip
        self.username = username
        self.password = password
        self.base_url = f"https://{self.pc_ip}:9440/api/nutanix/v3"
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.verify = False
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get_cluster_list(self):
        """Fetch all registered Nutanix clusters."""
        url = f"{self.base_url}/clusters/list"
        payload = {"kind": "cluster"}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_vm_list(self):
        """Fetch all VMs running in the environment."""
        url = f"{self.base_url}/vms/list"
        payload = {"kind": "vm"}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def create_vm(self, vm_spec):
        """Create a new VM."""
        url = f"{self.base_url}/vms"
        response = self.session.post(url, json=vm_spec)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    print("Prism Central API Helper initialized.")
