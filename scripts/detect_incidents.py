import pandas as pd
from pathlib import Path

Path("outputs").mkdir(exist_ok=True)

df = pd.read_csv("data/sample_logs.csv")
alerts = []

error_rate = (df["status"] != 200).mean()
avg_response_time = df["response_time_ms"].mean()
ip_counts = df["ip"].value_counts()
top_ip = ip_counts.idxmax()
top_ip_requests = ip_counts.max()

failed_login_events = df[(df["endpoint"] == "/login") & (df["status"].isin([403, 500]))]

if error_rate > 0.25:
    alerts.append(f"[HIGH] Elevated error rate detected: {error_rate:.2%}")

if avg_response_time > 700:
    alerts.append(f"[MEDIUM] High average response time detected: {avg_response_time:.2f} ms")

if top_ip_requests > 50:
    alerts.append(f"[HIGH] Suspicious traffic concentration from IP {top_ip}: {top_ip_requests} requests")

if len(failed_login_events) > 20:
    alerts.append(f"[MEDIUM] Repeated failed login-related events detected: {len(failed_login_events)}")

with open("outputs/alerts.txt", "w", encoding="utf-8") as f:
    if alerts:
        for alert in alerts:
            f.write(alert + "\n")
    else:
        f.write("No critical issues detected.\n")

with open("outputs/incident_summary.txt", "w", encoding="utf-8") as f:
    f.write("Incident Detection Summary\n")
    f.write("==========================\n")
    f.write(f"Total log records: {len(df)}\n")
    f.write(f"Error rate: {error_rate:.2%}\n")
    f.write(f"Average response time: {avg_response_time:.2f} ms\n")
    f.write(f"Top source IP: {top_ip} ({top_ip_requests} requests)\n")
    f.write(f"Failed login-related events: {len(failed_login_events)}\n\n")
    f.write("Detected Alerts\n")
    f.write("---------------\n")
    if alerts:
        for alert in alerts:
            f.write(alert + "\n")
    else:
        f.write("No critical issues detected.\n")

print("Incident detection complete.")
print("Files created:")
print("- outputs/alerts.txt")
print("- outputs/incident_summary.txt")
if alerts:
    print("\nDetected alerts:")
    for alert in alerts:
        print(alert)
else:
    print("\nNo critical issues detected.")
