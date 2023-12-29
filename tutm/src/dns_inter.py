import dns.message
import dns.query

def dns_filter(query, allowed_domains):
    domain = str(query.question[0].name)
    if domain in allowed_domains:
        # Allow the DNS request
        print(f"Allowed DNS request: {domain}")
        return True
    else:
        # Drop or log the DNS request
        print(f"Blocked DNS request: {domain}")
        return False

def intercept_dns():
    allowed_domains = ['example.com', 'trusteddomain.com']

    while True:
        # Capture DNS request
        query = dns.message.from_wire(sniff(filter="udp and port 53", count=1)[0][0].load)

        # Apply DNS filtering
        if not dns_filter(query, allowed_domains):
            # Modify DNS response or drop the request
            pass

# Example usage
intercept_dns()
