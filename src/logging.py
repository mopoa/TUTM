# Example: Simple logging
import logging

logging.basicConfig(filename='utm_log.txt', level=logging.INFO)

def log_event(event):
    logging.info(event)

# Example usage
log_event("Firewall rule violation: Blocked incoming connection.")

