import pymongo
from urllib import parse

# 连接mongo，获取mongo客户端
client = pymongo.MongoClient('mongodb://%s:%s@%s:%s/%s' % ('mongoit', parse.quote_plus('mongoitdb@123'), '106.14.47.3', '28017', 'admin'))
# 指定数据库
db = client.mongoit

#总记录数
def query_count(collect, query):
    # 指定集合
    collection = db[collect]
    return collection.find(query).count()

# 分页查询
def query_by_page(collect, query, pageNum, pageSize):
    # 指定集合
    collection = db[collect]

    skip = (pageNum - 1) * pageSize

    return collection.find(query).skip(skip).limit(pageSize)

# 插入数据
def save_to_mongo(product, collect):
    # 指定集合
    collection = db[collect]
    """
    保存数据到mongo数据库
    :param result:
    :return:
    """
    try:
        condition = None
        temp = None
        if "products" == collect:
            condition = {'productId': product['productId']}
        elif "dzdp-goods" == collect:
            condition = {'goodsId': product['goodsId']}
        elif "dzdp-shop" == collect:
            condition = {'shopId': product['shopId']}

        if not condition is None:
            temp = collection.find_one(condition)

        if not temp is None:
            product['_id'] = temp['_id']
            collection.update_one(condition, {'$set': product})
        else:
            collection.insert(product)
        print("保存数据到mongo数据库成功")
    except Exception as e:
        print("保存数据到mongo数据库失败,失败原因：", e)

# 保存失败记录
def save_fail_record(record):
    # 指定集合
    collection = db["dzdp-fail-record"]
    """
    保存失败记录mongo数据库
    :param result:
    :return:
    """
    try:
        collection.insert(record)
        print("保存失败记录到mongo数据库成功")
    except Exception as e:
        print("保存失败记录到mongo数据库失败,失败原因：", e)