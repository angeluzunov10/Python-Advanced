def accommodate_new_pets(available_capacity: int, max_weight_limit: float, *data):
    accommodated_pets = {}
    text_to_print = []

    for pet_type, pet_weight in data:
        if available_capacity <= 0:
            text_to_print.append("You did not manage to accommodate all pets!")
            break

        if pet_weight > max_weight_limit:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        available_capacity -= 1
    else:
        text_to_print.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    text_to_print.append("Accommodated pets:")
    [text_to_print.append(f"{pet_type}: {pets_count}") for pet_type, pets_count in sorted(accommodated_pets.items())]

    return "\n".join(text_to_print)


# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))

# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
