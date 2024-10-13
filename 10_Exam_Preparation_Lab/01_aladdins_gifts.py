from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while magic and materials:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_magic + current_material
    if result < 100:
        if result % 2 == 0:
            result = (current_material * 2) + (current_magic * 3)
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if not 100 <= result <= 499:
        continue

    if 100 <= result < 200:
        gifts["Gemstone"] += 1
    elif 200 <= result < 300:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= result < 400:
        gifts["Gold"] += 1
    elif 400 <= result < 500:
        gifts["Diamond Jewellery"] += 1

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for k, v in sorted(gifts.items()):
    if v > 0:
        print(f"{k}: {v}")
