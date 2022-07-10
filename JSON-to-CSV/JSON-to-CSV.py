import json

if __name__ == "__main__":

    try:
        with open("input.json", "r") as f:
            data = json.loads(f.read())
        output = ",".join([*data[0]])
        for obj in data:
            output += f'\n{obj["firstName"]},{obj["lastName"]},{obj["address"]}'

        with open("output.csv", "w") as f:
            f.write(output)

    except Exception as ex:
        print(f"error {str(ex)}")