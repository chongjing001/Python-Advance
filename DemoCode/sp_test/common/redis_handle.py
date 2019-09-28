import json

import redis


class RedisHandle(object):
    """
    redis String、List、Hash 操作类
    """

    def __init__(self, host='localhost', port='6379', db_sign=None, decode_responses=True):
        """
        初始化连接
        :param host: ip
        :param port: 端口
        :param db_sign: 数据库序号标志
        """
        db = self.__judge_db(db_sign)
        self.db_connect = redis.Redis(host=host, port=port, db=db, decode_responses=decode_responses)

    @staticmethod
    def __judge_db(db_sign):
        if db_sign == 'on_line':
            db = 1
        else:
            db = 0
        return db

    def get_all_keys(self):
        """
        获取所有的key
        :return: [key1,key2,...]
        """
        return self.db_connect.keys()

    def add_data(self, value: tuple):
        """
        存储key-value
        :param value:
        :return:
        """
        self.db_connect.set(value[0], value[1])

    def get_data(self, name):
        """
        获取数据
        :param name: key值
        :return:
        """
        return self.db_connect.get(name)

    def update_data(self, name, value):
        """
        更新数据
        :param name: key
        :param value: 新值
        :return:
        """
        self.db_connect.getset(name, value)

    def set_add_data(self, name, *values):
        """
        集合中的元素都是不重复的,向键为name的集合中添加元素
        :param name: 键名；
        :param value: 值，可为多个
        """
        self.db_connect.sadd(name, *values)

    def set_remove_data(self, name, *values):
        """
        从键为name的集合中删除元素
        :param name: 键名；
        :param value: 值，可为多个
        """
        self.db_connect.srem(name, *values)

    def set_get_data(self, name):
        """
        返回键为name的集合的所有元素
        :param name: 键名
        """
        return self.db_connect.smembers(name)

    def list_add_data(self, name, value):
        """
        列表尾部插入数据
        :param name:
        :param value:
        :return:
        """
        item_list = self.list_get_data(name)
        print(item_list)
        print(value)
        if value in item_list:
            return
        self.db_connect.rpush(name, value)

    def list_customer_add_data(self, name, value):
        """
        针对客户队列 去重
        :param name:
        :param value:
        :return:
        """
        item_list = [json.loads(i)[0] for i in self.list_get_data(name)]
        value1 = json.loads(value)[0]
        if value1 in item_list:
            return
        self.db_connect.rpush(name, value)

    def list_head_add_data(self, name, value):
        """
        列表头部插入数据
        :param name:
        :param value:
        :return:
        """
        self.db_connect.lpush(name, value)

    def list_len(self, name):
        """
        获取列表的长度
        :param name:
        :return:
        """
        return self.db_connect.llen(name)

    def list_get_data(self, name):
        """
        获取列表数据
        :param name:
        :return:
        """
        return self.db_connect.lrange(name, 0, -1)

    def list_index_item(self, name, index):
        """
        获取列表 对应下表的元素
        :param name: 列表
        :param index: 下标
        :return:
        """
        return self.db_connect.lindex(name, index)

    def list_rm_by_value(self, name, value):
        """
        通过value删除对应元素
        :param name: 列表
        :param value: 值
        :return:
        """
        self.db_connect.lrem(name, value, 0)

    def list_lpop(self, name):
        """
        从列表头部部取出第一个元素，返回该元素值并从列表删除(先进先出)
        :param name:
        :return:
        """
        return self.db_connect.lpop(name)

    def hash_add_or_up_data(self, table, name, value):
        """
        hash 类型存储(设置一个键值对)
        :param table: 表名
        :param name:
        :param value:
        :return:
        """
        if name != 'None' and name:
            self.db_connect.hset(table, name, value)

    def hash_add_mdata(self, table, value: dict):
        """
        hash中批量设置键值对
        :param table:
        :param value:{key:value,...}
        :return:
        """
        self.db_connect.hmset(table, value)

    def hash_get_data(self, table, name):
        """
        获取指定name对应的值
        :param table: 表名
        :param name: key
        :return:
        """
        return self.db_connect.hget(table, name)

    def hash_get_all_data(self, table):
        """
        获取table中所有键值对
        :param table:
        :return:
        """
        return self.db_connect.hgetall(table)

    def hash_del_data(self, table, name):
        """
        删除name对应的的值
        :param table: 表
        :param name: key
        :return:
        """
        self.db_connect.hdel(table, name)

    def zset_add_data(self, name, key, value):
        """
        有序集合添加数据
        :param name:
        :param key:
        :param value:
        :return:
        """
        self.db_connect.zadd(name, value, key)

    def zset_get_data_by_item(self, name, key):
        """
        有序集合获取制定元素的下表
        :param name:
        :param key:
        :return:
        """
        return self.db_connect.zrank(name, key)

    def zset_rm_item(self, name, key):
        """
        移除指定的元素
        :param name:
        :param key:
        :return:
        """
        self.db_connect.zrem(name, key)

    def zset_len(self, name):
        """
        获取有序列表的元素个数
        :param name:
        :return:
        """
        return self.db_connect.zcard(name)

    def zset_get_all_data(self, name):
        """
        获取所有数据（从小到大）
        :param name:
        :return:
        """
        return self.db_connect.zrange(name, 0, -1, withscores=True)

    def flush_db_data(self):
        """
        清空Redis
        :return:
        """
        self.db_connect.flushall()

    def close_connect(self):
        self.db_connect.connection_pool.disconnect()
