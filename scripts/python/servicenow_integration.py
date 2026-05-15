import requests
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceNowHelper:
    """Helper class to manage ITSM interactions via the ServiceNow REST API."""
    
    def __init__(self, instance, user, password):
        self.base_url = f"https://{instance}.service-now.com/api/now"
        self.auth = (user, password)
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def create_incident(self, short_description, description, priority="3"):
        """Creates a new incident ticket in ServiceNow."""
        url = f"{self.base_url}/table/incident"
        payload = {
            "short_description": short_description,
            "description": description,
            "priority": priority
        }
        try:
            response = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
            response.raise_for_status()
            logging.info(f"Successfully created incident: {short_description}")
            return response.json().get('result', {})
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create ServiceNow incident: {str(e)}")
            raise

    def update_cmdb_ci(self, ci_name, attributes):
        """Creates or updates a Configuration Item (CI) in the CMDB."""
        url = f"{self.base_url}/table/cmdb_ci_server"
        payload = {"name": ci_name}
        payload.update(attributes)
        try:
            response = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
            response.raise_for_status()
            logging.info(f"Successfully updated CI: {ci_name}")
            return response.json().get('result', {})
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to update CMDB CI: {str(e)}")
            raise

if __name__ == "__main__":
    logging.info("ServiceNow Helper Module Ready.")
