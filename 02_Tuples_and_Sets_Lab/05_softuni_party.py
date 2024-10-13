number_of_guests = int(input())
codes = set()

for _ in range(number_of_guests):
    code = input()
    codes.add(code)

guest = input()
while guest != "END":
    if guest in codes:
        codes.remove(guest)
    guest = input()

print(len(codes))
for code in sorted(codes):
    print(code)
