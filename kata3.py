# A: Location Codes (nested loop). Print the codes for 3 aisles × 4 shelves, one row per aisle.
# Expected first row: A1-S1 A1-S2 A1-S3 A1-S4

TOTAL_AISLES = 3
SHELVES_PER_AISLE = 4

# Outer loop: one pass per aisle, which becomes one printed row
for aisle in range(1, TOTAL_AISLES + 1):
    location_codes = []

    # Inner loop: runs completely for EACH aisle, building every shelf code in that aisle
    for shelf in range(1, SHELVES_PER_AISLE + 1):
        location_codes.append(f"A{aisle}-S{shelf}")

    # Print after the inner loop finishes so all of an aisle's codes land on one line
    print("  ".join(location_codes))