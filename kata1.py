# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

interval = 15

for check_number in range(1, 11):
    minutes = check_number * interval
    print(f"Check {check_number}: {minutes} minutes after shift start")