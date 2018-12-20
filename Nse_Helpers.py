from nsepy import get_history
from Logging import *
from Date_Helpers import Date_Helpers as DH

CLOSE = 'Close'
PCLOSE = 'Prev Close'

class Nse_Helpers:
    """
    Helps in getting Stock Price
    """

    def __init__(self, stock_id=None, start_date=None, end_date=None, to_dt=True):
        self.stock_id = stock_id

        if to_dt:
            self.sdate = DH(date_string=start_date).string_to_dt_object
            self.edate = DH(date_string=end_date).string_to_dt_object
        else:
            self.sdate = start_date
            self.edate = end_date

    @property
    def stock_dataset_between_days(self):
        try:
            Info("Getting Stock price Dataset for stock={} for period".format(self.stock_id))
            dataset = get_history(symbol=self.stock_id, start=self.sdate, end=self.edate)
            return dataset
        except Exception as err:
            Critical(err)
            return 0


    @property
    def close_price_on_sdate(self):
        try:
            Info("Getting Close Price on {}".format(self.sdate))
            Close_Price = get_history(symbol=self.stock_id, start=self.sdate, end=self.sdate)[CLOSE].get_values()[0]
        except Exception as err:
            Critical(err)
            Critical("No Close Price for this month Hence Returing 0 ")
            return 0
        Info("{} Close Price on {} = {}".format(self.stock_id, self.sdate, Close_Price))
        return Close_Price

