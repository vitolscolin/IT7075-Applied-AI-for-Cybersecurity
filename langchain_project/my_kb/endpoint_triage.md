# Endpoint Alert Triage

## Scope

Endpoint alerts often describe a process tree, a file, or a behavior without proving malicious intent. The analyst's job is to determine what executed, how it arrived, what it changed, and whether it spread. A detection name is a lead, not a complete incident conclusion.

## Process and file review

Capture the host name, user, process path, command line, parent process, child processes, file hash, signer, and alert time. A suspicious child of an Office application deserves attention because documents can launch scripts or installers. Compare the binary path and signer with known software inventory. Search the same hash and command line across other managed endpoints.

When a workstation downloads an executable and launches it, **record the parent-child process chain before isolating the host**. Also preserve the download URL, browser history if authorized, DNS queries, and the destination file path. Isolation can stop command-and-control traffic, but an analyst should avoid destroying volatile evidence or interrupting a critical system without considering business impact.

## Scope and containment

Check whether the same indicator appears on additional systems. Look for persistence mechanisms such as scheduled tasks, startup entries, services, or modified login scripts. Review outbound connections after execution and compare them with the process start time. If malicious behavior is confirmed, isolate affected endpoints through the approved tool, block validated indicators, and begin eradication under the incident plan.

## Recovery

Recovery requires more than closing the alert. Remove the persistence method, restore a trusted version of altered files, rotate exposed credentials, patch the exploited weakness, and monitor for recurrence. Record why the endpoint is safe to return to service. If the root cause remains unknown, state that uncertainty instead of treating the absence of new alerts as proof of recovery.
