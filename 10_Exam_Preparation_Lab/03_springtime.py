def start_spring(**kwargs):
    text_to_print = ""
    types = {}
    for name_of_spring_object, type_of_spring_object in kwargs.items():
        if type_of_spring_object not in types:
            types[type_of_spring_object] = []
        types[type_of_spring_object].append(name_of_spring_object)

    for obj_type, obj_name in sorted(types.items(), key=lambda x: (-len(x[1]), x[0])):
        text_to_print += f"{obj_type}:\n"
        for name in sorted(obj_name):
            text_to_print += f"-{name}\n"

    return text_to_print


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}

print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
