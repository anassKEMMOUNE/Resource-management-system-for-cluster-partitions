# Resource Management System for Cluster Partitions

## Introduction

This web application allows users to select a partition and automatically displays the number of available CPUs and GPUs in that partition. The application leverages scontrol, squeue, and sinfo commands for data collection and uses Dash to create a user interface. It is primarily developed using Python's Flask, JavaScript, HTML, and CSS.

## How to Install and Run

1. Activate the Python virtual environment using the following command:
    ```
    source venv/bin/activate
    ```
2. Run the application with the command:
    ```
    python3 app.py
    ```
3. Open the following link in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## How to Use

Connect to the UM6P network directly or via UM6P's VPN accessible at this link: [https://196.200.180.32/my.policy](https://196.200.180.32/my.policy)

Login using your UM6P username in the format "name.lastname" (without "@simlab-cluster.um6p.ma"). Enter your UM6P Simlab password.

Once logged in, select your preferred Partition/Node, and you will receive all the relevant information about it.

To end your session, use the Logout button.

## Credits and Improvements

This application was developed by:
- Anass Kemmoune ([GitHub](https://github.com/anassKEMMOUNE))
- Adnane Ait Magourt ([GitHub](https://github.com/adnanemagourt))
- Zineb Abercha ([GitHub](https://github.com/zinebabercha))

With the guidance of Professor Imad Kissami ([GitHub](https://github.com/imadki)).

For further improvements and questions, please contact [anass.kemmoune@um6p.ma](mailto:anass.kemmoune@um6p.ma).
