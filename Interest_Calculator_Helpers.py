from Date_Helpers import Date_Helpers


class Interest_Calculator_Helpers:
    """
    Operations for calculating interest amount, Maturity Amount etc...
    """
    def __init__(self):
        pass

    def interest_calc(self, principal_amount, interest_rate):
        """

        :param principal_amount:
        :param interest_rate:
        :return:
        """
        interest_amount = None

        return interest_amount

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

        total_interest_amount = None
        maturity_amount = None


        return total_interest_amount, maturity_amount

