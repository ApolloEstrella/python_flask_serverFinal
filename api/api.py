from dbconn.db import DbConnection  


class Authors:
    @staticmethod
    def allAuthors():
        db = DbConnection.dbConn()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM author INNER JOIN movie where author.id = movie.author_id order by author.name")
        return cursor.fetchall()

class Movies:
    @staticmethod
    def allMovies():
        db = DbConnection.dbConn()
        cursor = db.cursor()
        cursor.execute("SELECT id, name, score, author_id FROM movie")
        return cursor.fetchall()
