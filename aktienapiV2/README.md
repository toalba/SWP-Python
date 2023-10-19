in python!
venv mit requirements!

- auf seite https://www.alphavantage.co/ registrieren und API key besorgen
- API ansehen und monatsapi raussuchen https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo (hier wird IBM benutzt, mit einem gültigen key kann man anstell IBM zB SPY und IWM einsetzen)

- maximale menge an daten von den ETFs: SPY und IWM besorgen

- beim aufruf des script muss man die 2 ticker(ETF) angeben, es muss eine andere kombination wie SPY,QQQ auch möglich sein

- config file für DB zugang + datenbankname, API key erzeugen

- postgre DB benutzen, für jedes ETF eine tabelle erstellen und aus den API daten alle spalten in die tabelle speichern

- daten aus API müssen aktualisiert werden, aufrufdatum des python scripts vergleichen mit dem letzten dateneintrag zB wenn heute 25SEP und letzter eintrag 31 AUG keine daten weil kein monat abstand, ist zB 05-OKT und letzter eintrag ist 31 AUG dann muss man daten laden und aktualisieren

- tabelarisch für jedes jahr folgendes berechnen und im terminal darstellen (daten aus der DB benutzen!):

Jahr | Close_SEP - Open_JAN SPY as A| Close_SEP - Open_JAN IWM as B| A-B | Close_DEZ - Open SEP SPY as X | Close_DEZ - Open SEP IWM as Y |  X-Y

- das ganz in git mit vernünftigen .gitignore