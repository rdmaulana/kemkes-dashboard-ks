# ==============================
#     Insert / update log
# ==============================


def insertUpdateLog(db_conn, cursor, survei_individu_detail_id, id_exist, execute_success, updated_at):
    sql_insert_update_log = "INSERT INTO public.log values (%s,%s, %s,%s) ON CONFLICT (survei_individu_detail_id) DO UPDATE SET " \
                            "survei_individu_detail_id = excluded.survei_individu_detail_id, id_exist = excluded.id_exist, execute_success = excluded.execute_success," \
                            "updated_at = excluded.updated_at;"
    val = (survei_individu_detail_id, id_exist, execute_success, updated_at)
    cursor.execute(sql_insert_update_log, val)
    db_conn.commit()