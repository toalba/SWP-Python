from aktien.alphavantage.api_request import API_utility, Datenverarbeitung
from aktien.alphavantage.config import default_conf
from aktien.alphavantage.depiction import Calculation, Depiction

#api = API_utility(default_conf['api_key'])
#aktien = api.get_aktienbylist(['SPY','IWM'])
#datenverarbeitung = Datenverarbeitung()
#datenverarbeitung.set_aktien(aktien)

calc = Calculation(['SPY','IWM'])
filtered_data = calc()
calc.depiction.output(filtered_data)