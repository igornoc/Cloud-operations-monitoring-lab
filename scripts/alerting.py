from pathlib import Path

alerts_path = Path("outputs/alerts.txt")
summary_path = Path("outputs/incident_summary.txt")

print("=== INCIDENT RESPONSE OUTPUT ===")

if not alerts_path.exists():
    print("No alerts file found. Run detect_incidents.py first.")
else:
    print("\nAlerts")
    print("------")
    with open(alerts_path, "r", encoding="utf-8") as f:
        print(f.read())

if summary_path.exists():
    print("\nSummary")
    print("-------")
    with open(summary_path, "r", encoding="utf-8") as f:
        print(f.read())
