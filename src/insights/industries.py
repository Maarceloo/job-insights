from typing import List, Dict
import src.insights.jobs as jobs


def get_unique_industries(path: str) -> List[str]:
    file = jobs.read(path)
    result = list()
    for row in file:
        if row["industry"] not in "" and row["industry"] not in result:
            result.append(row["industry"])
    return result


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []
    for job in jobs:
        if industry == job['industry']:
            result.append(job)
    return result
