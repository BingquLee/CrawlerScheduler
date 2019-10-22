# -*- coding: utf-8 -*-
import time

from Crawlers.Tiktok.TiktokUploader import video_uploader
from global_config import conn
from global_utils import ts2date_min


def get_jobs():
    cursor = conn.cursor()
    sql = "SELECT * FROM jobs WHERE publish_time <= '%s' and status=0 ORDER BY publish_time ASC" % ts2date_min(int(time.time()))
    job_list = cursor.execute(sql).fetchall()
    for job in job_list:
        print(job)
        if job[1] == 'Tiktok':
            file_sql = "SELECT * FROM files WHERE status=0 AND account='{}' LIMIT {}".format(job[2], job[6])
            file_list = cursor.execute(file_sql).fetchall()
            for file in file_list:
                video_uploader(job[2], r'E:\Documents\PythonProjects\CrawlerScheduler\Videos\{}\To_{}\{}.mp4'.format(file[1], file[2], file[0]))
                file_update_sql = "UPDATE files SET status=1 WHERE id='{}';".format(file[0])
                cursor.execute(file_update_sql)
                conn.commit()
            sql_update_job = "UPDATE jobs SET status=1 WHERE id='{}'".format(job[0])
            cursor.execute(sql_update_job)
            conn.commit()

    cursor.close()


if __name__ == '__main__':
    get_jobs()
