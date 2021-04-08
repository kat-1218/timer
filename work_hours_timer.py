import datetime

## Timer class and methods
class TimeCalculator: 

    def initiate_timer(self, value):
        if value == "yes":
            start_timer = input('Start your day? (y/n)')
            self.start_time_log(start_timer)
        elif value == "no":
            print("Okay, let me know when you are ready to start")
            self.initiate_timer('yes')
        else:
            print("Either 'yes' or 'no' should be entered")
            self.initiate_timer('yes')      
        return start_timer

    def start_time_log(self, start_timer):
        value = start_timer
        if value == 'y':
            self.start_time = datetime.datetime.now()
            print(self.start_time)
            print("start time logged")
            self.time_log_questions(value)
        elif value == 'n':
            print("No problem, press y when ready")
            self.initiate_timer('yes')
        else:
            print("Either 'y' or 'n' should be entered")
            self.initiate_timer('yes')
        return self.start_time

    def time_log_questions(self, value):
        answer = input('Log another time? (y/n)')
        if answer == 'y':
            value_1 = input('Are you taking a break? (y/n)')
            if value_1 == 'y':
                self.log_break_time()
            elif value_1 == 'n':
                self.log_decimal_hours()
            else:
                print("Either 'y' or 'n' should be entered")
                self.time_log_questions('y')
        elif answer == 'n':
            print("Okay, waiting for next time log")
            self.time_log_questions('y')
        else:
            print("Either 'y' or 'n' should be entered")
            self.time_log_questions('y')
        return self.start_break, self.stop_break, self.break_time
    
    def log_decimal_hours(self):
        value_3 = input('Are you stopping for the day? (y/n)')
        if value_3 == 'y':
            self.stop_time_calc()
            print("Calculating decimal hours")
            self.calculate_hours()
        elif value_3 == 'n':
            print("Okay, waiting for next time log")
            self.time_log_questions('y')
        else:
            print("Either 'y' or 'n' should be entered")
            self.time_log_questions('y')
        return value_3

    def log_break_time(self):
        self.start_break_calc()
        print("break time started")
        value_2 = input('Have you completed your break? (y/n)')
        if value_2 == 'y':
            self.stop_break_calc()
            self.break_time_calc()
            print("break time logged")
            self.time_log_questions('y')
        elif value_2 == 'n':
            print("Okay, break continuing")
            self.time_log_questions('y')
        else:
            print("Either 'y' or 'n' should be entered")
            self.time_log_questions('y')
        return self.break_time

    def stop_time_calc(self):
        self.stop_time = datetime.datetime.now()
        print(self.stop_time)
        print("Stop time logged")
        return self.stop_time


    def start_break_calc(self):
        self.start_break = datetime.datetime.now()
        print(self.start_break)
        return self.start_break

    def stop_break_calc(self):
        self.stop_break = datetime.datetime.now()
        print(self.stop_break)
        return self.stop_break

    def break_time_calc(self):
        self.break_time = self.stop_break - self.start_break
        return self.break_time

    def calculate_hours(self):
        if hasattr(self, 'break_time') == True:
            raw_hours = (self.stop_time - self.start_time) - self.break_time
        elif hasattr(self, 'break_time') == False:
            raw_hours = self.stop_time - self.start_time
        secs = raw_hours.total_seconds()
        mins = int(secs/60) % 60
        hours = int(secs / 3600)
        decimal_hours = round((hours + (mins/60)), 2)
        print("Today you have worked " + str(decimal_hours) + " hours")
        exit()
        return decimal_hours


if __name__ == "__main__":
    ## Run script to start the timer
    t = TimeCalculator()
    t.initiate_timer("yes")
