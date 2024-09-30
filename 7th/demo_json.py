import json

JSON_PATH = "file.json"


def Demo_json_dump_to_string():
    data = {
        "users": [
            {
                "id": 42,
                "username": "john",
            },
            {
                "id": 11,
                "username": "sam",
            },
        ],
    }
    print(data)
    print(type(data))
    print(data["users"])

    data_string = json.dumps(data, indent=2)

    print(type(data_string))
    print(data_string)
    print(data_string[10:20])

def demo_JSON_load_string():
    data_json_string = '{"users": [{"id": 42, "username": "john"}, {"id": 11, "username": "sam"}]}'
    # print(type(data_json_string))
    # print(data_json_string)

    data = json.dumps(data_json_string)
    print(type(data_json_string))
    print(data_json_string)
    print(data)

def demo_JSON_dump_and_load_to_file():
    data = {
        "users": [
            {
                "id": 42,
                "username": "john",
            },
            {
                "id": 11,
                "username": "sam",
            },
        ],
    }
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)
        # data_string = json.dumps(data)
        # f.write(data_string)

    with open(JSON_PATH, "r") as f:
        data_from_file = json.load(f)

    print(type(data_from_file))
    print(data_from_file)


def demo_json_lines():
    user1 = {"id": 1, "name": "John", "friends": [2, 3]}
    user2 = {"id": 2, "name": "Sam", "friends": [1, 3]}
    user3 = {"id": 3, "name": "Nick", "friends": [1, 2]}

    # with open("file.jl", "a") as f:
    with open("file.jl", "w") as f:
        for user_data in [user1, user2, user3]:
            json.dump(user_data, f)
            f.write("\n")

    with open("file.jl", "r") as f:
        for line in f:
            if not line:
                continue
            user_data = json.loads(line)
            print("user_data:", user_data)
            print("id:", user_data["id"], "name:", user_data["name"])
def main():
    # Demo_json_dump_to_string()
    # demo_JSON_load_string()
    # demo_JSON_dump_and_load_to_file()
    demo_json_lines()

if __name__ == "__main__":
    main()

