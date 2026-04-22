import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("outputs/figures").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/sample_logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(8, 5))
df["status"].value_counts().sort_index().plot(kind="bar")
plt.title("HTTP Status Code Distribution")
plt.xlabel("Status Code")
plt.ylabel("Request Count")
plt.tight_layout()
plt.savefig("outputs/figures/status_distribution.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["response_time_ms"])
plt.title("Response Time Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/figures/response_time_over_time.png")
plt.close()

plt.figure(figsize=(9, 5))
df["ip"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Source IPs by Request Volume")
plt.xlabel("IP Address")
plt.ylabel("Request Count")
plt.tight_layout()
plt.savefig("outputs/figures/top_source_ips.png")
plt.close()

print("Metric visualisation complete.")
print("Charts saved to outputs/figures/")
