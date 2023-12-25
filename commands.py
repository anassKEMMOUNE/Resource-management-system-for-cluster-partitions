import scontrol as sc
import sinfo as si
import squeue as sq
import gpuInfo as gi
import json
import sys

def all_commands(ssh_connection) :
    stdin, stdout, stderr = ssh_connection.exec_command("scontrol show partitions")
    result0 = sc.parse_scontrol_partitions(stdout.read().decode("utf-8"))
        

    stdin, stdout, stderr = ssh_connection.exec_command("sinfo")
    result1 = si.parse_sinfo_partitions(stdout.read().decode("utf-8"))



    with open('static/json/result0.json', 'r') as file1:
        data1 = json.load(file1)


    with open('static/json/result1.json', 'r') as file2:
        data2 = json.load(file2)


    merged_data = {key: {**data1[key], **data2[key]} for key in data1.keys()}


    with open('static/json/result01.json', 'w') as merged_file:
        json.dump(merged_data, merged_file, indent=2)

    print("Merged JSON data saved to 'result01.json'")


    stdin, stdout, stderr = ssh_connection.exec_command("scontrol show nodes")
    result2 = sc.parse_scontrol_nodes(stdout.read().decode("utf-8"))
    
    
    stdin, stdout, stderr = ssh_connection.exec_command("squeue")
    result3 = sq.parse_squeue_jobs(stdout.read().decode("utf-8"))

    command = r'''
    (squeue -t RUNNING -o "%N %b %C" | awk "NR>1 {split(\$2, gpuArray, \":\"); nodes[\$1]+=\$2; gpus[\$1]+=gpuArray[2]; cpus[\$1]+=\$3} END {for (node in nodes) print node, 1-gpus[node], 44-cpus[node]}" && \
    sinfo -p gpu --states=idle --noheader -o "%n %G %c" | grep -v -e "maint" -e "drain" -e "resv" | awk "{{gsub(/[^0-9]/, \"\", \$2); print \$1, \$2, \$3}}") | \
    grep -F "$(sinfo -o "%n %G" | grep "gpu" | awk "{{print \$1}}")" | column -t
    '''

    stdin, stdout, stderr = ssh_connection.exec_command(command)
    result4 = gi.parse_gpuInfo(stdout.read().decode("utf-8"))

    
    return result0,result1,result2,result3,result4
                