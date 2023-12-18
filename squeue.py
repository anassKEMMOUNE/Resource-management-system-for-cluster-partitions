import json_parsing as jp

def parse_squeue_jobs(output: str):
    """
    Parses the output of `squeue` and returns a dictionary of job dictionaries.

    Args:
        output: The entire output of the `squeue` command.

    Returns:
        A dictionary of dictionaries, where each dictionary represents a job and contains its information.
    """

    jobs = {}

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

        # Create a dictionary for each job and append to the list
        job_info = dict(zip(column_names, columns))
        jobs[job_info["JOBID"]] = job_info
    info_show = jp.info_to_show_squeue
    jp.transform_to_json(jobs,info_show,'static/json/result3.json')

    return jobs
