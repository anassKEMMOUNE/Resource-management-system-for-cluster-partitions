def parse_scontrol_partition(output: str):
  """
  Extracts information from a single partition output string.

  Args:
    output: A string containing the output for a single partition.

  Returns:
    A dictionary containing extracted information about the partition.
  """
  partition_info = {}

# Split the output into lines
  lines = output.split('\n')

  # Iterate through each line
  for line in lines:
      # Skip empty lines
      if not line:
          continue
     
      for elm in line.split(" "):
        elms = list(map(str.strip, elm.split('=')))
        if len(elms) == 2:
          # Split each line into key-value pairs
          key, value = elms

          # Store the key-value pairs in the dictionary
          partition_info[key] = value

  return partition_info

def parse_scontrol_partitions(output: str):
  """
  Parses the output of `scontrol show partitions` and returns a list of partition dictionaries.

  Args:
    output: The entire output of the `scontrol show partitions` command.

  Returns:
    A list of dictionaries, where each dictionary represents a partition and contains its information.
  """
  partitions = {}
  current_partition = ""
  partition_data = ""
  for line in output.split("\n"):
    if line.startswith("PartitionName="):
      # Start parsing a new partition
      current_partition = line.split("=")[1]
      partition_data = ""
    elif current_partition:
      # Accumulate data for the current partition
      partition_data += line + "\n"
    else:
      # Ignore lines not related to any partition
      continue
    if not line.strip():
      # Partition data complete, extract information and add to list
      partitions[current_partition] = parse_scontrol_partition(partition_data)
      current_partition = ""
      partition_data = ""
  return partitions



# #result = output of scontrol show partitions

# partitions = parse_scontrol_partitions(result)

def parse_scontrol_node(output: str):
  """
  Extracts information from a single node output string.

  Args:
    output: A string containing the output for a single node.

  Returns:
    A dictionary containing extracted information about the node.
  """
  node_info = {}

# Split the output into lines
  lines = output.split('\n')

  # Iterate through each line
  for line in lines:
      # Skip empty lines
      if not line:
          continue
     
      linesplit = line.split(" ")

      if linesplit[0].startswith("OS="):
        elms = list(map(str.strip, linesplit[0].split('=')))
        key = elms[0]
        value = " ".join(elms[1:])
        node_info[key] = value
        continue

      for elm in linesplit:
        elms = list(map(str.strip, elm.split('=')))
        if len(elms) == 2:
          # Split each line into key-value pairs
          key, value = elms
          node_info[key] = value
        elif len(elms) > 2:
          node_info_tmp = {}
          key = elms[0]
          valuetemp = "=".join(elms[1:])
          for telm in valuetemp.split(","):
            telms = list(map(str.strip, telm.split('=')))
            if len(telms) == 2:
              # Split each line into key-value pairs
              tkey, tvalue = telms
              node_info_tmp[tkey] = tvalue
          # Store the key-value pairs in the dictionary
          node_info[key] = node_info_tmp

  return node_info

def parse_scontrol_nodes(output: str):
  """
  Parses the output of `scontrol show nodes` and returns a list of node dictionaries.

  Args:
    output: The entire output of the `scontrol show nodes` command.

  Returns:
    A list of dictionaries, where each dictionary represents a node and contains its information.
  """
  nodes = {}
  current_node = ""
  node_data = ""
  for line in output.split("\n"):
    if line.startswith("NodeName="):
      # Start parsing a new node
      first = line.split()
      current_node = first[0].split("=")[1]
      node_data = " ".join(first[1:]) + "\n"
    elif current_node:
      # Accumulate data for the current node
      node_data += line + "\n"
    else:
      # Ignore lines not related to any node
      continue
    if not line.strip():
      # node data complete, extract information and add to list
      nodes[current_node] = parse_scontrol_node(node_data)
      current_node = ""
      node_data = ""
  return nodes