import json
import random
import string
import uuid

def generate_cracked_uid():
    # Read data from the JSON file
    with open('../data/nickname.json') as f:
        data1 = json.load(f)

    # Check if UUID is None
    if data1["User-info"][0]["UUID"] is None:
        # Generate a new UUID
        uid = uuid.uuid4().hex
        data1["User-info"][0]["UUID"] = str(uid)
       # Write the updated data back to the JSON file
        with open('../data/nickname.json', 'w') as js_set:
            json.dump(data1, js_set, indent=4)

        print(uid)

        with open('../data/options.json') as f2:
            data2 = json.load(f2)

        data2["uuid"] = f"{generate_cracked_uid()}"

        with open('../data/options.json', 'w') as js_set:
            json.dump(data2, js_set, indent=4)

    elif data1["User-info"][0]["UUID"] is not None:
        # If UUID is already present, retrieve it
        uid = data1["User-info"][0]["UUID"]
        print(uid)
        return None

# Call the function to generate or retrieve UUID


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random password generated:", result_str)


