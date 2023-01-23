from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        result = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(result)


def get_unique_job_types(path: str) -> List[str]:
    file = read(path)
    result = list()
    for row in file:
        if row["job_type"] not in "" and row["job_type"] not in result:
            result.append(row["job_type"])
    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job_type == job['job_type']:
            result.append(job)
    return result
