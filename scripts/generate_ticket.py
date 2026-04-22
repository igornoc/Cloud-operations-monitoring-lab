from pathlib import Path
from datetime import datetime

alerts_file = Path("outputs/alerts.txt")
ticket_file = Path("outputs/incident_ticket.md")

if not alerts_file.exists():
    print("No alerts found. Run detect_incidents.py first.")
    raise SystemExit(1)

alerts = alerts_file.read_text(encoding="utf-8").strip().splitlines()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

severity = "Low"
if any("[HIGH]" in a for a in alerts):
    severity = "High"
elif any("[MEDIUM]" in a for a in alerts):
    severity = "Medium"

body = f"""# Incident Ticket

**Title:** Monitoring alert review required  
**Created:** {timestamp}  
**Severity:** {severity}  
**Status:** Open  
**Owner:** SOC / Cloud Operations  

## Summary
Automated monitoring flagged one or more conditions requiring analyst review.

## Triggered Alerts
"""
for alert in alerts:
    body += f"- {alert}\n"

body += """
## Initial Triage Actions
- Validate whether the alert reflects a real service issue or suspicious activity
- Review source IP concentration and failed authentication patterns
- Check response-time trend and error-rate trend
- Escalate if user impact or repeated malicious behaviour is confirmed

## Suggested Next Steps
- Confirm affected endpoint(s)
- Compare current behaviour to baseline
- Contain suspicious traffic if needed
- Update the incident status after investigation
"""

ticket_file.write_text(body, encoding="utf-8")
print(f"Incident ticket created: {ticket_file}")
