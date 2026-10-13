# Account Compromise Triage

## Purpose

Account alerts become urgent when several weak signals form one credible sequence. A failed login alone may be a typing mistake. A successful login after repeated failures, a new device, an unusual location, or a privileged action can change the risk. The analyst should preserve the timeline before making a judgment.

## First checks

Start with identity-provider logs and record the account, source address, authentication result, application, device identifier, and exact UTC time. Compare the source with the user's known devices and recent sign-in history. Check whether the address belongs to a corporate VPN, a common mobile carrier, or an anonymizing service. Do not label a geographic change impossible until normal travel and VPN use have been considered.

For repeated failures followed by success, **preserve the failed and successful sign-in events as one timeline**. Review multifactor authentication events, password-reset activity, mailbox rules, OAuth grants, and changes to recovery information. A success with a previously registered device is different from a success that also creates a new device registration.

## Containment

Containment should match the evidence. A confirmed hostile session should be revoked, the password reset through the approved identity process, and risky tokens invalidated. If compromise is uncertain, a step-up authentication challenge may preserve access while the analyst gathers evidence. Avoid asking a user to send a password or one-time code. Help-desk verification must use the organization's approved identity check.

## Documentation

Record facts separately from interpretations. "Twenty failures and one success from 203.0.113.25" is a fact. "Password spraying caused the success" is a hypothesis until supporting evidence exists. Document the reason for containment, who approved it, and the time each action occurred. Preserve relevant logs before short retention windows expire.
