import pymongo
from urllib import parse

# 连接mongo，获取mongo客户端
client = pymongo.MongoClient('mongodb://%s:%s@%s:%s/%s' % ('mongoit', parse.quote_plus('mongoitdb@123'), '106.14.47.3', '28017', 'admin'))
# 指定数据库
db = client.mongoit
# 指定集合
collection = db.products
# 插入数据
def save_to_mongo(product):
    """
    保存数据到mongo数据库
    :param result:
    :return:
    """
    try:
        collection.insert(product)
        print("保存数据到mongo数据库成功")
    except Exception as e:
        print("保存数据到mongo数据库失败,失败原因：", e)