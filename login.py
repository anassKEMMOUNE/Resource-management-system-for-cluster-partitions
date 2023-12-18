# After establishing the SSH connection
import paramiko
import getpass
import scrontrol as sc
import sinfo as si
import squeue as sq

# Function to establish an SSH connection to the cluster
def establish_ssh_connection(username,password):
    # username = input("Enter your username: ")  # Prompt the user for the username
    # password = getpass.getpass("Enter your password: ")  # Prompt the user for the password

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect('simlab-cluster.um6p.ma', username=username, password=password)
        return ssh
    except Exception as e:
        print(f"Error connecting to the cluster: {str(e)}")
        return None

# Establish SSH connection
# ssh_connection = establish_ssh_connection()

# # Check if the connection was successful before proceeding
# if ssh_connection:
#     # Now you can use the 'ssh_connection' variable to interact with the cluster
#     stdin, stdout, stderr = ssh_connection.exec_command("scontrol show partitions")

#     result = sc.parse_scontrol_partitions(stdout.read().decode("utf-8"))
#     print(result)

#     stdin, stdout, stderr = ssh_connection.exec_command("sinfo")

#     result1 = si.parse_sinfo_partitions(stdout.read().decode("utf-8"))
#     print(result1)

#     stdin, stdout, stderr = ssh_connection.exec_command("scontrol show nodes")
#     result2 = sc.parse_scontrol_nodes(stdout.read().decode("utf-8"))
#     print(result2)
    
#     stdin, stdout, stderr = ssh_connection.exec_command("squeue")
#     result3 = sq.parse_squeue_jobs(stdout.read().decode("utf-8"))
#     print(result3)

#     # Close the SSH connection when done
#     ssh_connection.close()
    