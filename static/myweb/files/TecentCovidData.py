import requests
import pymysql
import time
import json
import traceback  #追踪异常


def get_tencent_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    r = requests.get(url)
    res = json.loads(r.text)  # json字符串转字典
    data_all = json.loads(res['data'])

    details = []  # 当日详细数据
    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # list 25个国家
    data_province = data_country[0]["children"]  # 中国各省
    for pro_infos in data_province:
        province = pro_infos["name"]  # 省名
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return details

def get_conn():
    #创建连接
    conn=pymysql.connect(host="localhost",
                  user="root",
                  password="123456",
                  db="corona")
    #创建游标
    cursor=conn.cursor()#执行完毕返回的结果集默认以元组显示
    return conn,cursor

def close_conn(conn,cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def update_details():
    conn=None
    cursor=None
    try:
        li=get_tencent_data()
        conn,cursor=get_conn()
        sql="insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values (%s,%s,%s,%s,%s,%s,%s)"
        sql_query="select %s=(select update_time from details order by id desc limit 1)" #对于当前最大时间戳
        cursor.execute(sql_query,li[0][0])  #为什么这里填li[0][0]正确，而填写li[0]就错误呢？我感觉应该写li[0]？
        if not cursor.fetchone()[0]:  #必须加上"[0]"
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql,item)  #这一句中逗号后面具体写什么，要看便历的item所对应的数据是什么数据类型，
                #假如是字典类型就要用下面一句话这种形式。
                #cursor.execute(sql, [item["range"],item["image"],item["title"],item["recommend"],item["author"],item["times"],item["price"]])
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

if __name__ == "__main__":
        update_details()