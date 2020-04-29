import pymysql


class DbConnection:
    cursor: any
    @staticmethod
    def dbConn():
        sqldb = pymysql.connect(
            host='127.0.0.1',
            port=3308,
            user='root',
            passwd='javalinux',
            db='public',
            cursorclass=pymysql.cursors.DictCursor
        )
        return sqldb
