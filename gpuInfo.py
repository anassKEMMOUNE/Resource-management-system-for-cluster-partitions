import json


def parse_gpuInfo(output) :
    transformed_dict =  {}
    lines = output.split("\n")

    # Skip the header line


    for line in lines :
        if line != "":
            li = line.split("  ")
            transformed_dict[li[0]] = int(li[1])

    with open("static/json/result4.json", 'w') as json_file:
        json.dump(transformed_dict, json_file)

    return transformed_dict



