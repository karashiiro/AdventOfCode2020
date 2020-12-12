import sys

with open(sys.argv[1]) as f:
    pw_records = [line for line in str(f.read()).split("\n")]

valid_pws = 0
for pwr in pw_records:
    pwr_split = pwr.split(" ")
    i1, i2 = [int(n) - 1 for n in pwr_split[0].split("-")]
    char = pwr_split[1][0:-1]
    pw = pwr_split[2]
    if (pw[i1] == char and pw[i2] != char) or (pw[i2] == char and pw[i1] != char):
        valid_pws += 1

print("Valid passwords: %d" %valid_pws)
