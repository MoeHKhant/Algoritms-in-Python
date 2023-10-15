from collections import deque


class Job:
    job_counter: int = 1

    def __init__(self, name: str, priority: int, burst_time: int) -> None:
        self.name = name
        self.priority = priority
        self.burst_time = burst_time
        self.job_number = Job.job_counter
        Job.job_counter += 1


def priority_rr_scheduling(jobs: List[Job], time_quantum: int) -> List[Tuple[int, int]]:
    """
    Perform Priority Round Robin scheduling.

    Parameters:
    - jobs (List[Job]): A list of Job objects representing the jobs to be scheduled.
    - time_quantum (int): The time quantum for the Round Robin scheduling.

    Returns:
    - List[Tuple[int, int]]: A list of tuples where each tuple contains the job number and the time at which
      the job completed its execution.

    Example:
    >>> job1 = Job("Job1", 2, 10)
    >>> job2 = Job("Job2", 1, 5)
    >>> job3 = Job("Job3", 3, 8)
    >>> job4 = Job("Job4", 1, 2)

    >>> jobs = [job1, job2, job3, job4]

    >>> time_quantum = 2

    >>> result = priority_rr_scheduling(jobs, time_quantum)
    >>> result
    [(2, 5), (4, 7), (1, 17), (3, 25)]
    """
    queue = deque(jobs)
    waiting_queue = deque()
    current_time = 0
    completed_jobs = []

    while queue or waiting_queue:
        if queue:
            current_job = queue.popleft()
        else:
            current_job = waiting_queue.popleft()

        if current_job.burst_time > time_quantum:
            current_job.burst_time -= time_quantum
            current_time += time_quantum
            waiting_queue.append(current_job)
        else:
            current_time += current_job.burst_time
            current_job.burst_time = 0
            completed_jobs.append((current_job.job_number, current_time))

        # Check for new arrivals
        while (
            queue and queue[0].priority > 0 and queue[0].priority > current_job.priority
        ):
            waiting_queue.append(queue.popleft())

    return completed_jobs


if __name__ == "__main__":
    # Take input for jobs
    num_jobs = int(input("Enter the toal number of jobs present: "))
    jobs = []

    for _ in range(num_jobs):
        name = input(f"Enter name for Job {Job.job_counter}: ")
        priority = int(input(f"Enter priority for Job {Job.job_counter}: "))
        burst_time = int(input(f"Enter burst time for Job {Job.job_counter}: "))
        jobs.append(Job(name, priority, burst_time))

    # Take input for time quantum
    time_quantum = int(input("Enter the time quantum: "))

    result = priority_rr_scheduling(jobs, time_quantum)

    print("\nJob Execution Order:")
    for job, time in result:
        print(f"Job{job} completed at time {time}")

# Reference Link - https://www.scaler.com/topics/operating-system/priority-scheduling-algorithm/
