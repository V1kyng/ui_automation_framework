import datetime


class DateTimeHelper:

    def __init__(self):
        self.today: int = datetime.date.today().day

    def get_current_day(self) -> str:
        """
        :return: get current date to choose date in calendar
        """
        return str(self.today)

    def get_next_day(self) -> str:
        """
        :return: get next day from current date to choose date in calendar
        """
        return str(self.today + 1)

    def get_day_after_tomorrow(self) -> str:
        """
        :return: get next day from current date to choose date in calendar
        """
        return str(self.today + 2)

    def get_past_day(self) -> str:
        """
        :return: get past day from  current date to choose date in calendar
        """
        return str(self.today - 1)
