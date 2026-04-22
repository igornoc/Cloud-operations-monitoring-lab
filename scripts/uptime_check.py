import csv
from datetime import datetime
from pathlib import Path
import requests

TARGETS = [
    ("demo-api-health", "http://localhost:8000/health"),
    ("github-api", "https://api.github.com"),
    ("httpbin-status", "https://httpbin.org/status/200"),
]

Path("outputs").mkdir(exist_ok=True)
outfile = Path("outputs/uptime_checks.csv")

rows = []
for name, url in TARGETS:
    status = "DOWN"
    http_status = ""
    latency_ms = ""
    try:
        response = requests.get(url, timeout=5)
        http_status = response.status_code
        latency_ms = int(response.elapsed.total_seconds() * 1000)
        status = "UP" if 200 <= response.status_code < 400 else "DEGRADED"
    except Exception:
        status = "DOWN"

    rows.append({
        "timestamp": datetime.utcnow().isoformat(),
        "target_name": name,
        "url": url,
        "status": status,
        "http_status": http_status,
        "latency_ms": latency_ms,
    })

write_header = not outfile.exists()
with outfile.open("a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    if write_header:
        writer.writeheader()
    writer.writerows(rows)

print(f"Saved uptime results to {outfile}")
for row in rows:
    print(f"{row['target_name']}: {row['status']} ({row['http_status']}) {row['latency_ms']} ms")
