import pymysql.cursors


class DbFixture:

    def __int__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=username, password=password)


    def destroy(self):
        self.connection.close()