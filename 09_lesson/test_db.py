from db import Database
from db import transaction
from db import connection


sub = Database()

def test_db():
    sub.test_add_subject()
    sub.test_update_subject()
    sub.test_delete_subject()

    transaction.commit()
    connection.close()
