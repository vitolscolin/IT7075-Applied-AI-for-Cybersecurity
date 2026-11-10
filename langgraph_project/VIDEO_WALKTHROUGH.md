# Live recording outline (about 7-9 minutes)

Use the notebook and terminal live, not slides or screenshots. Test the kernel before recording. Read the synthetic alerts and adjust any rationale you cannot defend; rerun and regenerate the report if you change data or policy.

1. **0:00-0:45 - Goal and execution.** Show the branch and `langgraph_project` folder. Restart the notebook kernel and run all cells on screen. Explain that the graph uses deterministic Python, not a hosted model.
2. **0:45-2:00 - Practice graph.** Show `TriageState`, `classify`, `route_by_risk`, and `investigate`. Point out partial state updates, the lookup tool, conditional edges, and END. Explain that the practice CVE lookup is fictional.
3. **2:00-3:00 - Own data.** Show the six/six label count. Read A06 and A07 with their rationales. A06 turns off production logging but contains none of the tested words. A07 contains administrator but has a matching approval. Show that `graph_input` excludes expected labels and notes.
4. **3:00-4:30 - Trace a decision.** Run Part 12 live. A01 is caught. A06 is missed by the baseline: classify -> quick_close. In G1, follow classify (low) -> context_review (high after the lookup) -> investigate. Also show A07's verified actor/asset/action/time leading to quick_close.
5. **4:30-5:45 - Results and staffing.** Explain each incremental word and the K2-to-G1 comparison. Separate missed incidents from over-escalations. A09 remains a false alarm; removing outbound loses A05. Explain why you would accept one backup review rather than miss that transfer.
6. **5:45-6:45 - Memory.** Run Part 13. Show incident-A06's retained event after a partial update, incident-A07 remaining unchanged, and the unseen thread having no state. An in-memory checkpointer is lost when Python stops. Reinvoking the same thread reruns this graph; it does not merge separate alerts intelligently.
7. **6:45-8:00 - Limits and checks.** Show boundary checks. Explain that approved text alone is not trusted, but fixture/structured metadata still is. Twelve authored cases are not unseen evaluation; propose analyst-reviewed holdout data, false alarms per day, and review time. Compare with the earlier straight LCEL retrieval chain.
8. **End - Artifacts.** Show the saved notebook and `results_mine.csv`. After uploading this recording, add its URL with `build_report.py --video-url`, then submit the PDF.

Do not claim the original lecture's stub URL verdict is a real model result, that context is live, or that zero observed misses proves a zero miss rate in deployment.
