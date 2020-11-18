import pymysql

# 打开数据库连接,参数1：主机名或者IP；参数2：用户名；参数3：密码；参数4：数据库名称
db = pymysql.connect("localhost","root","123456","python")
# 使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()
# 使用execute()方法执行sql语句
cursor.execute("SELECT VERSION()")
# 使用fetchclone()方法获取单挑数据
data = cursor.fetchone()
print("Database version : %s" % data)
# 关闭数据库连接
db.close()