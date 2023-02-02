from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    PATH = "tests/mocks/brazilians_jobs.csv"
    arquivo = read_brazilian_file(PATH)
    for job in arquivo:
        assert 'title' in job
        assert 'salary' in job
        assert 'type' in job
