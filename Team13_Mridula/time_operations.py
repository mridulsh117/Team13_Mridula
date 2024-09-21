import datetime

class TimeOperations:
    @staticmethod
    def display_date():
        #Function to display the current date in the foramt 'dd-mm-yyyy'
        try:
            print(f"Today's date is: {datetime.datetime.now().strftime('%d-%b-%Y').lower()}")
        except Exception as e:
            print(f"An error occurred while retrieving the date: {e}")

    @staticmethod
    def display_time():
        #Function to display the current time in the format 'HH:MM:SS'
        try:
            print(datetime.datetime.now().strftime("Current time is: %H:%M:%S"))
        except Exception as e:
            print(f"An error occurred while retrieving the time: {e}")
        
    @staticmethod
    def display_time_hours():
        #Function to display current hour
        try:
            print(datetime.datetime.now().strftime("Current time in hours is: %H"))
        except Exception as e:
            print(f"An error occurred while retrieving the hours: {e}")

    @staticmethod
    def display_time_minutes():
        #Function to display current minute
        try:
            print(datetime.datetime.now().strftime("Current time in minutes is: %M"))
        except Exception as e:
            print(f"An error occurred while retrieving the minutes: {e}")

    @staticmethod
    def display_time_seconds():
        # Function to display current second
        try:
            print(datetime.datetime.now().strftime("Current time in seconds is: %S"))
        except Exception as e:
            print(f"An error occurred while retrieving the seconds: {e}")
