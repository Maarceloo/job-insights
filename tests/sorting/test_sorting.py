from src.pre_built.sorting import sort_by

job_list = [
    {
        "id": 1,
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "1997-06-27",
    },
    {
        "id": 2,
        "min_salary": 8000,
        "max_salary": 9000,
        "date_posted": "2000-06-05",
    },
    {
        "id": 3,
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "1995-01-25",
    },
]

list_min_salary = [
    {
        "id": 1,
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "1997-06-27",
    },
    {
        "id": 3,
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "1995-01-25",
    },
    {
        "id": 2,
        "min_salary": 8000,
        "max_salary": 9000,
        "date_posted": "2000-06-05",
    }
]

list_max_salary = [
    {
        "id": 2,
        "min_salary": 8000,
        "max_salary": 9000,
        "date_posted": "2000-06-05",
    },
    {
        "id": 3,
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "1995-01-25",
    },
    {
        "id": 1,
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "1997-06-27",
    },
]

list_date_posted = [
    {
        "id": 2,
        "min_salary": 8000,
        "max_salary": 9000,
        "date_posted": "2000-06-05",
    },
    {
        "id": 1,
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "1997-06-27",
    },
    {
        "id": 3,
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "1995-01-25",
    },
]


def test_sort_by_criteria():
    sort_by(job_list, "min_salary")
    assert job_list == list_min_salary

    sort_by(job_list, "max_salary")
    assert job_list == list_max_salary

    sort_by(job_list, "date_posted")
    assert job_list == list_date_posted
