#!/bin/bash

read -p "Enter your password: " -s password

expect -c "
spawn ssh -CY anass.kemmoune@simlab-cluster.um6p.ma
expect {
    \"assword:\" {
        send \"$password\r\"
        interact
    }
    timeout {
        puts \"Connection timed out\"
        exit 1
    }
}
"
