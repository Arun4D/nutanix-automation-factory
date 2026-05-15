import requests
import json
import urllib3
import logging

# Disable insecure request warnings for self-signed Prism Central certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrismCentralAPI:
    """Helper class to interact with Nutanix Prism Central v3 REST APIs."""
    
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
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch cluster list: {str(e)}")
            raise

    def get_vm_list(self):
        """Fetch all VMs running in the environment."""
        url = f"{self.base_url}/vms/list"
        payload = {"kind": "vm"}
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch VM list: {str(e)}")
            raise

    def create_vm(self, vm_spec):
        """Create a new VM using the provided spec."""
        url = f"{self.base_url}/vms"
        try:
            response = self.session.post(url, json=vm_spec)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create VM: {str(e)}")
            raise

if __name__ == "__main__":
    logging.info("Prism Central API Helper initialized.")
