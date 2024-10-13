def cookbook(*recipes):
    cuisines = {}
    text_to_print = []

    for recipe in recipes:
        name = recipe[0]
        cuisine = recipe[1]
        ingredients = recipe[2]
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append([name, ingredients])

    for cuisine in sorted(cuisines, key=lambda x: (-len(cuisines[x]), x)):
        recipes_for_current_cuisine = cuisines[cuisine]
        recipes_count = len(cuisines[cuisine])
        text_to_print.append(f"{cuisine} cuisine contains {recipes_count} recipes:")
        for recipe in sorted(recipes_for_current_cuisine):
            name = recipe[0]
            ingredients = recipe[1]
            text_to_print.append(f"  * {name} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(text_to_print)


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

print(cookbook(("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
         ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
         ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
         ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
         ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
         ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
         ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
         ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))