import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

Path("data").mkdir(exist_ok=True)
random.seed(42)

logs = []
base_time = datetime.now()

normal_ips = [f"192.168.1.{i}" for i in range(1, 26)]
suspicious_ip = "192.168.1.250"
endpoints = ["/", "/login", "/dashboard", "/api/orders", "/api/users", "/api/auth", "/health"]

for i in range(500):
    timestamp = base_time - timedelta(minutes=(500 - i))
    if i < 90:
        ip = suspicious_ip
    else:
        ip = random.choice(normal_ips)

    endpoint = random.choice(endpoints)

    if ip == suspicious_ip:
        status = random.choice([403, 403, 500, 500, 200])
        response_time = random.randint(900, 2400)
    else:
        status = random.choice([200, 200, 200, 200, 200, 403, 500])
        response_time = random.randint(70, 450) if status == 200 else random.randint(700, 1800)

    logs.append({
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "endpoint": endpoint,
        "status": status,
        "response_time_ms": response_time
    })

df = pd.DataFrame(logs)
df.to_csv("data/sample_logs.csv", index=False)

print("Log generation complete.")
print("File created: data/sample_logs.csv")
print(f"Total records: {len(df)}")
print(f"Unique IPs: {df['ip'].nunique()}")
print(f"Average response time: {df['response_time_ms'].mean():.2f} ms")
