# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

# Store the interval and count in named variables so they are easy to change later
CHECK_INTERVAL_MINUTES = 15
TOTAL_CHECKS = 10

# range() stops BEFORE its end number, so we go to TOTAL_CHECKS + 1 to include check 10.
# We start at 1 (not 0) because the first check happens 15 minutes in, not at minute 0.
for check_number in range(1, TOTAL_CHECKS + 1):
    # Each check happens one interval after the previous one
    minutes_after_start = check_number * CHECK_INTERVAL_MINUTES
    print(f"Check {check_number}: {minutes_after_start} minutes after shift start")