# After establishing the SSH connection
import paramiko
import getpass
import scontrol as sc
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

