from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:789@localhost:5432/QA"
db = create_engine(db_connection_string)
connection = db.connect()
transaction = connection.begin()


class Database:


    def test_add_subject(self, subject_id: int = 21, subject_title: str ="Basketball"):
        sql = text("insert into subject (\"subject_title\", \"subject_id\") values (:subject_title, :subject_id)")
        connection.execute(sql, {'subject_title':f'{subject_title}', 'subject_id': f'{subject_id}'})
        self.test_delete_subject(21)


    def test_update_subject(self, subject_id: int = 18, subject_title: str ="Basketball"):
        self.test_add_subject()
        sql = text("update subject set subject_id = :subject_id where subject_title = :subject_title")
        connection.execute(sql, {"subject_id": f'{subject_id}', "subject_title": f'{subject_title}'})
        self.test_delete_subject(18)

    def test_delete_subject(self, subject_id = 21):
        self.__test_add_subject(f'{subject_id}')
        sql = text("delete from subject where subject_id = :subject_id")
        connection.execute(sql, {"subject_id":f'{subject_id}'})


    def __test_add_subject(self, subject_id: int = 21, subject_title: str ="Basketball"):
        sql = text("insert into subject (\"subject_title\", \"subject_id\") values (:subject_title, :subject_id)")
        connection.execute(sql, {'subject_title':f'{subject_title}', 'subject_id': f'{subject_id}'})