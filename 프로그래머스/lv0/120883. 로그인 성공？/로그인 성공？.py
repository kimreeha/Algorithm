def solution(id_pw, db):
    db_id = [i[0] for i in db]
    if id_pw in db:
        return 'login'
    for i in db:
        if (id_pw[0] in db_id) & (i[1] != id_pw[1]):
            return 'wrong pw'
        if id_pw[0] not in db_id:
            return 'fail'