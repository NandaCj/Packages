from datetime import date, timedelta , datetime as dt

class Date_Helpers:
    """
    This package uses python datetime module to create
    useful methods

    each method return the datetime object respectively
    Mandatory : Date Format - 01-Jan-2018
    example
    """

    def __init__(self, date_string):
        self.date_string = date_string
        self.date_format = '%d-%b-%Y'

    @property
    def string_to_dt_object(self):
        """
        :return: converts the string into datetime object used for other purpose
        """
        dt_obj = dt.strptime(self.date_string, self.date_format)
        return dt_obj


    @property
    def next_business_day (self):
        """
        returns the next business day
        :param dt_obj: datetime object
        :return:
        """
        next_business_day = ''
        return next_business_day

    @property
    def previous_business_day(self):
        pass

    @property
    def month_first_business_day(self):
        pass

    @property
    def month_last_business_day(self):
        pass

    @property
    def year_first_business_day(self):
        pass

    @property
    def year_last_business_day(self):
        pass

    @property
    def is_weekday(self):
        pass

    @property
    def is_weekend(self):
        pass

    def add_days(self, no_of_days):
        """
        Adds the given number of days to datetime object
        :return: datetime object
        """
        new_dt = self.date_string + no_of_days
        return new_dt

    def next_n_day(self, n):
        """
        returns date after given n days
        :param date_string: can be string or datetime object
        :return: next day dt object
        """
        next_day = ''
        return next_day

    def get_months_between(self, start_date, end_date):
        pass

    def get_years_between(self, start_date, end_date):
        pass

    def get_weeks_between(self, start_date, end_date):
        pass

    def get_days_between(self, start_date, end_date):
        pass


if __name__ == '__main__':
    Test_Date = '01-Jan-2018'
    DH = Date_Helpers(date_string=Test_Date)
    date = DH.string_to_dt_object
    print(date.month, type(date))

