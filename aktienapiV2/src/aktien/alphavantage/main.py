from aktien.alphavantage.api_request import API_utility, Datenverarbeitung
from aktien.alphavantage.config import default_conf

api = API_utility(default_conf['api_key'])
aktien = api.get_aktienbylist(default_conf['etf_list'])
datenverarbeitung = Datenverarbeitung()
datenverarbeitung.set_aktien(aktien)
