---
name: client-communication
description: When the user needs to contact clients, collect data, relay OTP codes, request approvals, or track pending items via WhatsApp (Evolution API) or Google Sheets. Also use when the user mentions "client communication," "WhatsApp message," "OTP," "Evolution API," "collect data from client," "client approval," "pending data," "verify with client," or "human intervention." For brainstorming client requirements, see brainstorming.
category: core
profile: marketing
---

# Client Communication

> Structured protocols for client interaction — OTP relay, data collection, approvals, and pending item tracking.

## When to Use

- Need to relay an OTP from a platform to a client
- Collecting bulk data via Google Sheets
- Requesting client approval for listing/website/content
- Tracking pending items that are blocking work
- Sending project completion confirmations

## Before Starting

1. Is Evolution API (WhatsApp) running on the server?
2. Do we have the client's WhatsApp number?
3. What specific data/approval is needed?
4. What's the urgency level? (blocking vs. nice-to-have)
5. Is Google Sheets access set up for bulk data?

## Core Framework

### Communication Channel Selection

| Data Size | Urgency | Channel | Example |
|-----------|---------|---------|---------|
| Single item | High | WhatsApp | OTP, yes/no approval |
| Single item | Low | WhatsApp | Logo request, address confirm |
| 5-20 items | Any | Google Sheets | Service descriptions, menu items |
| 20+ items | Any | Google Sheets + WhatsApp notification | Full product catalog |
| Formal | Any | Email | Contracts, detailed proposals |

### OTP Relay Protocol

```
Step 1: Browser agent triggers OTP on platform
Step 2: Send WhatsApp message:
  ──────────────────────────────────
  "Hi [Name], we're setting up your [Platform] account.
   An OTP was just sent to your phone ending in [last 4 digits].
   Please reply with the code here."
  ──────────────────────────────────
Step 3: Set timeout timer (5 minutes)
Step 4: If no response after 3 min → send reminder:
  "Quick reminder — we need the OTP code to continue setup."
Step 5: If received → relay to browser agent → continue
Step 6: If timeout (5 min) → flag as BLOCKED:
  "We'll pause this setup. Please share when convenient."
Step 7: If no response in 24h → escalate to human operator
```

### Data Collection Patterns

#### Quick Data (WhatsApp)
```
"Hi [Name], we need a few details for your website:
 1. Business operating hours
 2. Your official email address
 3. Any social media links

 Please reply when convenient. 🙏"
```

#### Bulk Data (Google Sheets)
```
1. Create Google Sheet with required columns
2. Pre-fill any known data
3. Add "Your Input" column highlighted in yellow
4. Share link via WhatsApp:
   "Hi [Name], please fill in the yellow columns:
    [Google Sheets link]
    Take your time — we'll continue building the site
    and add your details when ready."
5. Set reminder for 3 days if not filled
```

### Approval Request Patterns

| Type | Format | Example |
|------|--------|---------|
| Quick Approval | Screenshot + "Does this look good? Reply YES." | Listing preview |
| Detailed Review | Google Sheet with "Approved" column | 20 service descriptions |
| Final Approval | Screenshot set + checklist | Website before launch |

### Pending Items Register

Every project tracks pending items:

```markdown
## Pending Items — [Project Name]

| # | Item | Requested | Via | Status | Blocks |
|---|------|-----------|-----|--------|--------|
| 1 | Company logo (PNG) | [date] | WhatsApp | PENDING | Header, favicon |
| 2 | Service descriptions | [date] | Google Sheet | IN PROGRESS | Service pages |
| 3 | Business license copy | [date] | WhatsApp | RECEIVED ✅ | Platform listing |
```

**Status Flow:** PENDING → IN PROGRESS → RECEIVED → VERIFIED

**Escalation Rules:**
- 3 days pending → WhatsApp reminder
- 7 days pending → Second reminder + "blocking progress" note
- 14 days pending → Escalate to human operator

### Human Intervention Protocol

> When automation can't proceed, request human intervention clearly.

```
"⚠️ HUMAN INTERVENTION NEEDED

Task: [What was being done]
Blocker: [Exact issue — e.g., CAPTCHA, account locked, verification call]
Context: [What's been done so far]
Action needed: [Specific ask — e.g., "Please complete phone verification"]

Resume instructions: [How to continue after intervention]"
```

## Output Format

### Communication Log
```
## Communication Log — [Date]

| Time | Direction | Channel | Message Summary | Response |
|------|-----------|---------|----------------|----------|
| 10:00 | OUT | WhatsApp | OTP request for [Platform] | Pending |
| 10:03 | IN | WhatsApp | OTP: [code] | ✅ Used |
```

## Common Mistakes

- ❌ Sending 10 separate WhatsApp messages instead of batching
- ❌ Not tracking pending items → forgotten requirements
- ❌ Proceeding with unverified data
- ❌ Using WhatsApp for 50+ item data collection (use Google Sheets)
- ❌ Not sending completion confirmation after task is done
- ❌ Giving up after one failed OTP (try again, then escalate)

## Related Skills

- **brainstorming**: For discovering requirements through Socratic questions
- **business-listing**: For platform-specific data requirements
- **google-my-business**: For GMB-specific data requirements
