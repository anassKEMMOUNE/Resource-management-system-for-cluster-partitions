def parse_squeue_job(output: str):
    """
    Extracts information from a single job output string of squeue command.

    Args:
        output: A string containing the output for a single job from squeue command.

    Returns:
        A list of dictionaries, each containing extracted information about a job.
    """
    jobs = []

    # Split the output into lines
    lines = output.strip().split('\n')

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
        jobs.append(job_info)

    return jobs



def parse_squeue_jobs(output: str):
    """
    Parses the output of `squeue` and returns a list of job dictionaries.

    Args:
        output: The entire output of the `squeue` command.

    Returns:
        A list of dictionaries, where each dictionary represents a job and contains its information.
    """
    jobs = []

    # Split the output into sections for each job
    job_sections = output.strip().split("\n\n")

    for job_section in job_sections:
        job = parse_squeue_job(job_section)
        if job:
            jobs.append(job)

    return jobs
