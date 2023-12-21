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
    
    def create_index_time_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS update_time (table_name VARCHAR(20) PRIMARY KEY,date DATE)")

    def create_table(self,symbol):
        cursor = self.connection.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {symbol} (date DATE PRIMARY KEY, open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume BIGINT)")
        self.connection.commit()

    def check_if_table_exists(self, symbol):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM information_schema.tables where table_name = '{symbol}')")
        c = cursor.fetchone()[0]
        print(c)
        return c    
    def check_if_key_exits_in_table(self,symbol,key):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT EXISTS(SELECT * FROM {symbol} WHERE date='{key}')")
        return cursor.fetchone()[0]
    
    def get_close_open_by_symbol(self,symbol):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT date, close, open FROM {symbol}")
        return cursor.fetchall()

    def __enter__(self):
        return self.connection.cursor()
    
    def __close__(self):
        self.connection.commit()
        self.connection.close()

connection = DatabaseConction()