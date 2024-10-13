def get_info(name, age, town):
    print(f"This is {name} from {town} and he is {age} years old")


get_info(**{"name": "Angel", "age": 24, "town": "Panagyurishte"})
