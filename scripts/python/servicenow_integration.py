import requests
import json
import os

class ServiceNowHelper:
    def __init__(self, instance, user, password):
        self.base_url = f"https://{instance}.service-now.com/api/now"
        self.auth = (user, password)
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def create_incident(self, short_description, description, priority="3"):
        url = f"{self.base_url}/table/incident"
        payload = {
            "short_description": short_description,
            "description": description,
            "priority": priority
        }
        response = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json().get('result', {})

    def update_cmdb_ci(self, ci_name, attributes):
        url = f"{self.base_url}/table/cmdb_ci_server"
        payload = {"name": ci_name}
        payload.update(attributes)
        response = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json().get('result', {})

if __name__ == "__main__":
    print("ServiceNow Helper Module Ready.")
