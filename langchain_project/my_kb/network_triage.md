# Network Alert Triage

## Establish context

Network detections need asset and traffic context. Record source and destination addresses, ports, protocol, sensor, direction, bytes transferred, rule name, and exact UTC window. Map internal addresses to hosts and owners using current inventory or DHCP records. Check whether the destination is expected for the application and whether the connection pattern is new.

## DNS and outbound connections

For a new-domain alert, preserve the DNS query, resolved addresses, requesting host, process information when available, and follow-on connections. A newly registered domain can be suspicious, but age alone does not prove malicious use. Compare timing with software installation, user browsing, scheduled jobs, and threat intelligence that is permitted for the investigation.

For suspected command-and-control traffic, **correlate DNS, proxy, firewall, and endpoint timestamps in UTC**. Repeated low-volume connections at regular intervals may indicate beaconing, but monitoring agents and update tools can behave similarly. Examine interval consistency, destination reputation, TLS metadata, transferred bytes, and the responsible process before reaching a conclusion.

## Scanning and lateral movement

Many connection attempts across ports or hosts may be scanning. Determine whether the source is an approved vulnerability scanner, administrator workstation, or unmanaged device. For possible lateral movement, review authentication logs and remote-service use around the network timestamps. SMB, RDP, SSH, and remote management traffic can be normal; unexpected account and host combinations increase concern.

## Response

Use the least disruptive control that safely limits harm. Options include blocking a validated destination, isolating a host, disabling a compromised account, or increasing monitoring. Preserve the alert and related flow records before retention expires. Record both supporting and contradicting evidence so later reviewers can understand why the case was escalated or closed.
