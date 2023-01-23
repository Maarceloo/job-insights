from functools import lru_cache
from typing import List, Dict
import csv


# PATH = "data/jobs.csv"


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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


# print(get_unique_job_types(PATH))
