def parse_sinfo_partition(output: str):
    """
    Extracts information from a single partition output string of sinfo command.

    Args:
        output: A string containing the output for a single partition from sinfo command.

    Returns:
        A list of dictionaries, each containing information about a partition.
    """
    partitions = []

    # Split the output into lines
    lines = output.split('\n')

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

        # Create a dictionary for each partition
        partition_info = dict(zip(column_names, columns))
        partitions.append(partition_info)

    return partitions


def parse_sinfo_partitions(output: str):
    """
    Parses the output of `sinfo` and returns a list of partition dictionaries.

    Args:
        output: The entire output of the `sinfo` command.

    Returns:
        A list of dictionaries, where each dictionary represents a partition and contains its information.
    """
    partitions = []
    # Split the output into sections for each partition
    partition_sections = output.strip().split("\n\n")

    for partition_section in partition_sections:
        partitions.append(parse_sinfo_partition(partition_section))

    return partitions