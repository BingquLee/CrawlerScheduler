# -*- coding: utf-8 -*-

from global_config import conn
from global_utils import read_files


def add_file_to_db():
    cursor = conn.cursor()
    sql = "SELECT * FROM files"

    video_list = read_files(r'..\Videos')
    file_video_name_set = set(video_list)
    print(cursor.execute(sql).fetchall())
    db_video_name_set = set(["..\\Videos\\{}\\To_{}\\{}.mp4".format(i[1], i[2], i[0]) for i in cursor.execute(sql).fetchall()])
    sub_set = file_video_name_set - db_video_name_set
    if sub_set:

        insert_sql = """
            INSERT INTO
            files (id, channel, account, status)
            VALUES
            %s
        """
        insert_sql = insert_sql % ','.join(['("{}", "{}", "{}", "{}")'.format(i.split('\\')[-1].split('.')[0], i.split('\\')[-3], i.split('\\')[-2].split('_')[-1], 0) for i in sub_set])
        print(insert_sql)
        cursor.execute(insert_sql)
        conn.commit()
    else:
        pass
    cursor.close()


if __name__ == '__main__':
    add_file_to_db()
