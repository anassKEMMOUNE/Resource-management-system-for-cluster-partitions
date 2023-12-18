import json
#result 0
info_to_show_scontrol_partitions = ["Nodes", "MaxCPUsPerNode", "MaxTime", "MaxNodes", "TotalNodes", "TotalCPUs", "DefMemPerCPU", "MaxMemPerCPU", "State"]

#result 1
info_to_show_sinfo = ["AVAIL", "TIMELIMIT", "NODES", "STATE", "NODELIST"]

#result 2
info_to_show_scontrol_nodes = ["CPUTot", "CPUAlloc", "CPULoad", "RealMemory", "AllocMem", "State", "Partitions", "CfgTRES", "AllocTRES"] #FreeMem = RealMemory - AllocMem

#result 3
info_to_show_squeue = ["PARTITION", "NAME", "USER", "ST", "TIME", "NODELIST(REASON)", "NODES"]

def transform_to_json(data_dict, info_list, file_path):
    transformed_dict = {}
    for node, node_info in data_dict.items():
        transformed_dict[node] = {key: node_info[key] for key in info_list if key in node_info}
    
    with open(file_path, 'w') as json_file:
        json.dump(transformed_dict, json_file)