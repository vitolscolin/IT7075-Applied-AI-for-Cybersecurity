# Sources and scenario provenance

All 12 alerts are original synthetic coursework scenarios drafted with AI assistance, not copied console records. The student should review the labels and explain them in the recording. Public sources establish event/technique meanings; the specific assets, actors, times, approvals, and labels are invented lab assumptions. No source validates the simulated change records. Accessed November 10, 2026.

| Ref | Source | Use |
|---|---|---|
| S1 | [MITRE ATT&CK T1190: Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | A01 exploitation scenario; A08 contrasts a deliberately generated lab signature with evidence of production compromise. |
| S2 | [MITRE ATT&CK T1486: Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/) | A02 mass encryption and loss of file availability. |
| S3 | [Microsoft SecurityEvent query examples](https://github.com/MicrosoftDocs/azure-monitor-docs/blob/main/articles/azure-monitor/reference/queries/securityevent.md) | A03/A07 group membership event types, including 4728; approval context and the support group are synthetic. |
| S4 | [MITRE ATT&CK T1003: OS Credential Dumping](https://attack.mitre.org/techniques/T1003/) | A04 suspicious access to authentication material. |
| S5 | [MITRE ATT&CK T1041: Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/) | General data-transfer risk motivating A05/A09. These alerts do not establish a C2 channel or claim a confirmed T1041 attribution. |
| S6 | [AWS CloudTrail StopLogging API](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopLogging.html) | A06: stopping a trail suspends recording and log delivery. |
| S7 | [Microsoft Windows event 4625](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625) | A11 failed logon meaning; A10's verified reset is an invented routine-account contrast, not a 4625 event. |
| S8 | [LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) | Typed state, node updates, conditional edges, compilation, and END. |
| S9 | [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Checkpoints and thread-scoped state. The in-memory implementation here does not survive process exit. |

A12 is a generic synthetic sensor-health heartbeat, with no product-specific event claim.

## Course and earlier work

- `../06_LangGraph/assignments/project/MiniProject_Agent.pdf`: requirements and grading.
- `../06_LangGraph/assignments/project/MiniProject_Agent_Starter.ipynb`: practice scaffolding copied into this student's completed notebook; original remains unchanged.
- `../06_LangGraph/assignments/project/alerts_template.json`: schema adapted for the 12 custom alerts, with additional structured event metadata and source references.
- `../06_LangGraph/assignments/project/alerts.json`: unchanged practice-only set.
- `../06_LangGraph/code/langgraph_state_nodes.ipynb` and `langgraph_branch_tools.ipynb`: lecture practice, executed through guarded no-key paths.
- `../langchain_project/` and `../rag_project/`: prior incident-triage retrieval coursework, preserved on the parent branch. This project changes the task to deterministic routing; it does not claim an LLM or reuse retrieval scores as triage scores.

The practice tool's `CVE-2026-0001` is a fictional course stub. It is not a verified CVE or live threat-intelligence result.
