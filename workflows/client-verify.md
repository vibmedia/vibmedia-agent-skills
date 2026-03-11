---
description: Send data to client for verification, collect approvals, and track pending items. Use when you need client sign-off before proceeding.
---

# /client-verify — Client Data Verification

## Prerequisites
- Data/content ready for client review
- Client's WhatsApp number available
- Evolution API (WhatsApp) running on server

## Steps

1. **Prepare review package**
   - Compile data that needs client review
   - Format based on volume:
     - Single item → WhatsApp screenshot + text
     - 5-20 items → Google Sheet with "Approved" column
     - Full page/listing → Screenshot set
   - Expected: Review package ready for sending

2. **Select channel & send**
   - Load `client-communication` skill
   - For quick approval → WhatsApp message with screenshot
   - For bulk review → Share Google Sheet link via WhatsApp
   - For final approval → Send screenshot set + checklist summary
   - Include clear instructions: "Reply YES to approve" or "Mark items in sheet"
   - Expected: Review request sent to client

3. **Wait for response**
   - Set timeout based on urgency:
     - OTP/blocking → 5 minutes
     - Normal review → 48 hours
     - Non-blocking → 7 days
   - If timeout → send one reminder
   - Expected: Response received or escalated

4. **Process response**
   - If APPROVED → proceed with next step in parent workflow
   - If CHANGES REQUESTED → apply changes, re-verify
   - If PARTIAL → apply approved items, track remaining as PENDING
   - If NO RESPONSE → flag in pending items register, continue non-blocked work
   - Expected: Clear next action determined

5. **Update tracking**
   - Update pending items register in brand's `artifacts/` folder
   - Log communication in project notes
   - If all items approved → send completion confirmation
   - Expected: All tracking updated, client informed
