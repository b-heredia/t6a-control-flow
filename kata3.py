# A: Location Codes (nested loop). Print the codes for 3 aisles × 4 shelves, one row per aisle.
# Expected first row: A1-S1 A1-S2 A1-S3 A1-S4

for aisle in range(1, 4):
    row = []
    for shelf in range(1, 5):
        row.append(f"A{aisle}-S{shelf}")
    print("  ".join(row))