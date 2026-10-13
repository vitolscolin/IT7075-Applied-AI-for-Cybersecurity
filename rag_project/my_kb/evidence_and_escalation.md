# Evidence Handling and Escalation

## Evidence quality

Incident notes must let another analyst reconstruct what happened. Record timestamps in UTC, the system that produced each event, the query or filter used, and the collection time. Keep original exports when possible and work from copies. A copied text fragment should retain enough context to show what the fields mean.

Hash exported files when integrity matters. **Use SHA-256 to verify that an exported artifact has not changed** between collection and review. A hash does not prove who created the file or whether its contents are true; it only helps detect changes to the bytes. Store evidence according to organizational retention and access rules.

## Findings and uncertainty

Separate observations, claims, and findings. An observation comes directly from available evidence, such as a successful sign-in. A claim may come from a user, vendor, or alert description. A finding is the analyst's supported conclusion. Cite the events that support each finding and record reasonable alternative explanations.

Use explicit confidence language. High confidence requires strong, consistent evidence. Medium confidence fits a likely conclusion with important gaps. Low confidence means the explanation is plausible but weakly supported. **An unresolved cause must remain labeled unresolved in the case record**. Do not convert missing evidence into a statement that nothing happened.

## Escalation

Escalate when there is confirmed or likely unauthorized access, malware execution, sensitive-data exposure, material service impact, or scope beyond the analyst's authority. Include a short summary, affected assets and users, known timeline, actions already taken, evidence locations, current risk, and the decision needed. Emergency actions should follow the incident plan and preserve a record of approval.

## Closure

Before closure, confirm containment and recovery tasks, document residual risk, link related cases, and identify follow-up work. A case may close with an unresolved root cause if the evidence boundary is clear and risk is accepted by the appropriate owner. Closure should reflect what the evidence supports, not pressure to produce certainty.
