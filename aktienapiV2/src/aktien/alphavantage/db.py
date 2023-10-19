import psycopg2
from aktien.alphavantage.config import db_conf
# als verstaendnis unter den imports, fuers developtment verwenden wir psycopg2, production wird mit psycopg2-binary empfohlen

class DatabaseConction:

    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        
        return psycopg2.connect(
            database=db_conf['database'],
            host=db_conf['host'],
            user=db_conf['user'],
            password=db_conf['password'],
            port=db_conf['port']
        )
    
    def create_table(self,symbol):
        cursor = self.connection.cursor()
        cursor.execute(f"CREATE TABLE {symbol} (date DATE PRIMARY KEY, open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume INT)")
        self.connection.commit()
        self.connection.close()

    def check_if_table_exists(self, symbol):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='{symbol}')")
        return cursor.fetchone()[0]
    
    def check_if_key_exits_in_table(self,symbol,key):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM {symbol} WHERE date='{key}')")
        return cursor.fetchone()[0]

    def __enter__(self):
        return self.connection.cursor()
    
    def __close__(self):
        self.connection.commit()
        self.connection.close()

connection = DatabaseConction()