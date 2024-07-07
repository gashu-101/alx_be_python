import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    return formatted_date

formatted_current_datetime = display_current_datetime()
print("Current date and time:", formatted_current_datetime)

formatted_future_date = calculate_future_date()
print("Future date:", formatted_future_date)