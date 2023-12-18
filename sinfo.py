import json_parsing as jp

def parse_sinfo_partitions(output: str):
    """
    Parses the output of `sinfo` and returns a dictionary of partition dictionaries.

    Args:
        output: The entire output of the `sinfo` command.

    Returns:
        A dictionary of dictionaries, where each dictionary represents a partition and contains its information.
    """

    partitions = {}

    # Split the output into lines
    lines = output.strip().split("\n")

    # Skip the header line
    header = lines[0]
    lines = lines[1:]

    # Split header into column names
    column_names = header.split()

    # Iterate through each line
    for line in lines:
        # Skip empty lines
        if not line:
            continue

        # Split each line into columns
        columns = line.split(maxsplit=len(column_names) - 1)

        # Create a dictionary for each partition and append to the list
        partition_info = dict(zip(column_names, columns))
        partitions[partition_info["PARTITION"]] = partition_info

    info_show = jp.info_to_show_sinfo
    jp.transform_to_json(partitions,info_show,'static/json/result1.json')

    return partitions
