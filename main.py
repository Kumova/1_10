from salary import calculate_salary as salary
from people import get_employees as people
from datetime import datetime, date, time

def datetime():
    print(datetime.now())


if __name__ == '__main__':
    datetime()
    salary.salary()
    people.people()