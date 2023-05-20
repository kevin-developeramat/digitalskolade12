from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2023, 1, 1)
end_date = date(2023, 5, 14)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))