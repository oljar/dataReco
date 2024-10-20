import datetime


class Generator:

    def __init__(self,delta_time,current_time):
        self.current_time = current_time
        if not isinstance(delta_time, int):
            delta_time = 3
        self.interval = datetime.timedelta(seconds=delta_time)

    def infinite_time_generator(self):
        while True:
            yield self.current_time
            self.current_time += self.interval








