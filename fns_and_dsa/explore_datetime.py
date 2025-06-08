from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(format)

def calculate_future_date():
    days = int(input("enter a number of days to add to the current date: "))
    today = datetime.today()
    future_date = today + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(formatted_future_date)

display_current_datetime()
calculate_future_date()
