# Suspicious Email Triage

## Preserve the message

A screenshot is useful for communication but does not contain all evidence. Preserve the original message or an approved export so headers, attachment hashes, URLs, and routing details remain available. Handle potentially malicious attachments in an authorized analysis environment and never open them on a normal workstation.

## Header and sender review

Compare the visible From address with the envelope sender and Return-Path. Review Authentication-Results for SPF, DKIM, and DMARC, while remembering that an authenticated compromised account can still send harmful mail. Inspect Received headers from the bottom upward to understand the route. Similar-looking domains, reply-to changes, urgency, and an unusual request can support a phishing assessment.

For a suspected phishing message, **preserve the original message with full headers and attachment hashes**. Normalize URLs for comparison without visiting them directly. Search the mail environment for matching sender addresses, subjects, URLs, and attachment hashes. Document how many recipients received the message and whether any recipient clicked, replied, entered credentials, or executed a file.

## Containment and follow-up

Quarantine matching messages using the approved mail-security process. If a recipient entered credentials, follow the account-compromise procedure, revoke sessions, and review sign-ins and mailbox rules. If a file executed, follow endpoint triage. Block a domain or hash only when the indicator is specific enough to avoid unnecessary disruption.

## Communication

Ask the reporter what they did after opening the message, using neutral language. Do not blame the user; fast reporting reduces harm. Provide a case reference and explain any required password reset or device check. Close the incident only after the message scope, recipient actions, and linked account or endpoint activity are addressed.
