from itertools import filterfalse as where_not
import sys

EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
req_fields.sort()

def is_record_valid(record: str) -> bool:
    fields = dict(map(lambda field: field.split(":"), record.split(" ")))

    field_keys = list(filter(lambda key: key != "cid", fields.keys()))
    field_keys.sort()
    if req_fields != field_keys:
        return False

    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    try:
        hgt = int(fields["hgt"][0:-2])
    except ValueError:
        return False
    if fields["hgt"].endswith("cm") and (hgt < 150 or hgt > 193):
        return False
    elif fields["hgt"].endswith("in") and (hgt < 59 or hgt > 76):
        return False

    if len(fields["hcl"]) != 7 or fields["hcl"][0] != "#":
        return False
    try:
        int(fields["hcl"][1:], 16)
    except ValueError:
        return False

    if not fields["ecl"] in EYE_COLORS:
        return False

    if len(fields["pid"]) != 9:
        return False
    try:
        int(fields["pid"])
    except ValueError:
        return False

    return True

with open(sys.argv[1]) as f:
    data_raw = str(f.read())

records_all = [r.replace("\n", " ") for r in data_raw.split("\n\n")]
records_valid = list(where_not(
    lambda r: not is_record_valid(r),
    records_all,
))

print("Total records: %d" %len(records_all))
print("Valid records: %d" %len(records_valid))
