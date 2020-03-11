from Date_Helpers import Date_Helpers


class Interest_Calculator_Helpers:
    """
    Operations for calculating interest amount, Maturity Amount etc...
    """
    def __init__(self):
        pass

    def calc_interest_amount(self, start_date, end_date, interest_rate, period, principal_amount):
        """
        find number of days, weeks, months, years between start and end_date
        perform interest calculation based on the period
        :param start_date: str : format :'%d-%b-%Y'
        :param end_date: str : format : '%d-%b-%Y'
        :param interest_rate: float : interest rate ex:11.5
        :param period: daily, monthly, weekly, annually
        :param principal_amount: float
        :return: calculated interest_amount , maturity_amount (principal+interest_amount)
        """

        interest_amount = None
        maturity_amount = None

        return interest_amount, maturity_amount

