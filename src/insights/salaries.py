from typing import Union, List, Dict
import src.insights.jobs as jobs


def get_max_salary(path: str) -> int:
    file = jobs.read(path)
    result = list()
    for row in file:
        if row["max_salary"].isnumeric():
            result.append(int(row["max_salary"]))
    salary = max(result)
    return salary


def get_min_salary(path: str) -> int:
    file = jobs.read(path)
    result = list()
    for row in file:
        if row["min_salary"].isnumeric():
            result.append(int(row["min_salary"]))
    salary = min(result)
    return salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max = int(job["max_salary"])
        min = int(job["min_salary"])
        money = int(salary)
        if min > max:
            raise ValueError("min_salary > max_salary")
        return min <= money <= max
    except (ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    newListJobs = []
    for job in jobs:
        try:
            isJob = matches_salary_range(job, salary)
            if isJob:
                newListJobs.append(job)
        except ValueError:
            continue
    return newListJobs
