import scontrol as sc
import sinfo as si
import squeue as sq

def all_commands(ssh_connection) :
    stdin, stdout, stderr = ssh_connection.exec_command("scontrol show partitions")
    result0 = sc.parse_scontrol_partitions(stdout.read().decode("utf-8"))
        

    stdin, stdout, stderr = ssh_connection.exec_command("sinfo")
    result1 = si.parse_sinfo_partitions(stdout.read().decode("utf-8"))
    

    stdin, stdout, stderr = ssh_connection.exec_command("scontrol show nodes")
    result2 = sc.parse_scontrol_nodes(stdout.read().decode("utf-8"))
    
    
    stdin, stdout, stderr = ssh_connection.exec_command("squeue")
    result3 = sq.parse_squeue_jobs(stdout.read().decode("utf-8"))
    
    return result0,result1,result2,result3
                