---
description: Create business listings on external marketplace platforms using the harness pattern for token-efficient automation.
---

# /setup-listing — Platform Listing Setup

## Prerequisites
- Client brand folder set up
- Business data available (name, address, phone, licenses, images)
- Platform credentials or OTP access via client

## Steps

1. **Identify target platforms**
   - Ask: Which platforms does this business need listings on?
   - Check if we have existing harness scripts for those platforms
   - If new platform → this will include a Golden Run (higher token cost)
   - Expected: Platform list with harness availability status

2. **Verify listing data**
   - Load `business-listing` skill for platform-specific requirements
   - Check all required data is available (name, address, licenses, images)
   - If data missing → use `@client-coordinator` to collect via WhatsApp/Sheets
   - Expected: Data verification complete, all requirements met

3. **Harness decision**
   - If NO existing script for this platform:
     a. Run **Golden Run** — browser agent processes one listing manually
     b. Document all selectors, fields, OTP triggers
     c. **Crystallize** — create Playwright script + rules file
     d. Test script with one real listing
   - If existing script available:
     → Skip to step 4
   - Expected: Working harness script ready

4. **Login / OTP flow**
   - Navigate to platform login page
   - Enter client credentials
   - If OTP triggered → `@client-coordinator` relays via WhatsApp
   - Wait for OTP (5 min timeout, 1 reminder)
   - If no OTP → flag as BLOCKED, request human intervention
   - Expected: Successfully logged into platform

5. **Create listing**
   - Run harness script with client data
   - Upload images from Google Drive
   - Fill all required fields
   - Expected: Listing form completed

6. **Pre-submit verification**
   - Capture screenshot of final listing preview
   - Run through `listing_rules.md` checks (character limits, image specs)
   - Expected: Screenshot ready, all rules pass

7. **Client approval**
   - Send screenshot to client via `@client-coordinator`
   - Wait for "YES" approval
   - Expected: Client approves listing

8. **Submit listing**
   - Click submit
   - Capture confirmation page/screenshot
   - Record listing URL (if available immediately)
   - Expected: Listing submitted successfully

9. **Post-submission**
   - Verify listing appears on platform (may take 24-48h for some platforms)
   - Send completion confirmation to client
   - Log listing in project's `artifacts/` folder
   - Expected: Listing confirmed live
