def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


result = {"name": "George", "town": "Sofia", "age": 20}

print(get_info(**result))
