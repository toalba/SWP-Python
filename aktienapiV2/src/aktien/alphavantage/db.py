import ZODB, ZODB.FileStorage


class DatabaseConction:

    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        storage = ZODB.FileStorage.FileStorage('var/db/mydata.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        return connection.root
    
    def close(self):
        self.connection._p_jar.close()


connection = DatabaseConction().connection['aktien']