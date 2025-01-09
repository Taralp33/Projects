import csv
import random
from datetime import datetime, timedelta

# Define the log data
attack_types = ["DDoS", "Brute Force", "Malware", "Memory Injection", "Phishing", "SQL Injection", "Cross-Site Scripting (XSS)", "Man-in-the-Middle", "SSL/TLS Vulnerability", "SYN Flood", "Session Hijacking", "Amplification Attack", "Ping Flood", "FTP Bounce", "Packet Sniffing", "Eavesdropping", "Email Spoofing"]
protocols = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS", "FTP", "Telnet", "SMTP"]
browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com", "https://www.linkedin.com", "https://www.github.com", "https://www.amazon.com", "https://www.microsoft.com", "https://www.apple.com", "https://www.netflix.com", "https://www.reddit.com"]
log_types = ["Application", "Logon Attempt", "Normal Traffic", "Security Event"]

# Generate random log entries with realistic distribution
log_data = []
start_time = datetime.now()
for i in range(25000):
    log_entry = {
        "count": i + 1,
        "time": start_time + timedelta(seconds=i),
        "src_ip": f"192.168.1.{random.randint(1, 255)}",
        "dest_ip": f"10.0.0.{random.randint(1, 255)}",
        "protocol": random.choices(protocols, weights=[30, 20, 10, 15, 10, 5, 5, 5])[0],
        "length": random.randint(40, 1500),
        "bytes": random.randint(500, 10000),
        "attack_type": random.choices(attack_types + ["None"], weights=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 50])[0],
        "browser": random.choice(browsers),
        "url": random.choice(urls),
        "type": random.choice(log_types)
    }
    log_data.append(log_entry)

# Write the log data to a CSV file
with open('detailed_security_logs.csv', 'w', newline='') as csvfile:
    fieldnames = ['Count', 'Time', 'Source IP', 'Destination IP', 'Protocol', 'Length', 'Bytes', 'Attack Type', 'Browser', 'URL', 'Type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for log in log_data:
        writer.writerow({
            'Count': log['count'],
            'Time': log['time'].strftime('%Y-%m-%d %H:%M:%S'),
            'Source IP': log['src_ip'],
            'Destination IP': log['dest_ip'],
            'Protocol': log['protocol'],
            'Length': log['length'],
            'Bytes': log['bytes'],
            'Attack Type': log['attack_type'],
            'Browser': log['browser'],
            'URL': log['url'],
            'Type': log['type']
        })

print("Log file created successfully with 25,000 entries.")
