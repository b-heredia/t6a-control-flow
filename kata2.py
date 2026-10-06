# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

DAYS_IN_MONTH = 30
CYCLE_COUNT_EVERY = 3
SCANNER_AUDIT_EVERY = 5

# range() stops before its end number, so +1 makes sure day 30 is included
for day in range(1, DAYS_IN_MONTH + 1):
    # % gives the remainder; a remainder of 0 means the day divides evenly
    is_cycle_count_day = day % CYCLE_COUNT_EVERY == 0
    is_scanner_audit_day = day % SCANNER_AUDIT_EVERY == 0

    # Check the "both" case FIRST. Python stops at the first true condition,
    # so if we checked cycle count first, days 15 and 30 would never reach FULL AUDIT.
    if is_cycle_count_day and is_scanner_audit_day:
        activity = "FULL AUDIT"
    elif is_cycle_count_day:
        activity = "Cycle count"
    elif is_scanner_audit_day:
        activity = "Scanner audit"
    else:
        activity = "Normal operations"

    print(f"Day {day}: {activity}")