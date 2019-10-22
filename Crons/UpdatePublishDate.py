# -*- coding: utf-8 -*-
from global_config import conn
from global_utils import today


def update_publish_date():
    cursor = conn.cursor()
    sql = "SELECT * FROM jobs WHERE publish_freq=='Everyday' ORDER BY publish_time ASC"
    update_data = cursor.execute(sql).fetchall()
    if update_data:
        update_sql = """
            UPDATE jobs SET
                publish_time = CASE id
                %s
                END
            WHERE id in (%s)
        """
        update_sql = update_sql % ('\n'.join(['WHEN {} THEN "{}"'.format(i[0], '{} {}'.format(today(), i[3].split(' ')[-1])) for i in update_data]), ','.join([str(i[0]) for i in update_data]))
        cursor.execute(update_sql)
        conn.commit()
    else:
        pass
    cursor.close()


if __name__ == '__main__':
    update_publish_date()
