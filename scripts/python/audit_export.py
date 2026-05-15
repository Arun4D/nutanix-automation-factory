import datetime
import json
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def export_audit_log(event_type, resource_name, details, status="SUCCESS"):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "event_type": event_type,
        "resource": resource_name,
        "status": status,
        "details": details
    }
    
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs/audit'))
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"audit_{datetime.datetime.utcnow().strftime('%Y%m%d')}.log")
    
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
        
    logging.info(f"Audit exported for {event_type} on {resource_name}")

if __name__ == "__main__":
    export_audit_log("TEST_EVENT", "system", {"message": "Audit export helper initialized."})
