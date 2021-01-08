### kafka单分区，多个客户端共同消费一个topic



#### 安装kafka-python

```
pip install kafka-python
```

[kafka-python官网](https://kafka-python.readthedocs.io/en/master/index.html)

#### 生产 Productor

- 1s 生产一条消息

```python

import json
from kafka import KafkaProducer
from time import sleep

def start_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092', # kafka服务地址
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),

    )
    for i in range(0, 100):
        msg = {'task_type':'mpc','task_id':i}
        future=producer.send('topic_test', msg, partition=0)
        sleep(1)
        # future.get(timeout=10)

if __name__ == '__main__':
    start_producer()

```



#### 消费端

> `kafka消费`
>
> 1.相同group_id的消费者，只有一个消费者能够消费到消息
>
> 2.不同group_id的消费者，接受到的消息都是一样的
>
> 以下代码消费一次(接收到消息)，就close，其他消费者就能开始消费了

```python


from kafka import KafkaConsumer, TopicPartition
import time
import random

def start_consumer():
    consumer = KafkaConsumer('topic2', bootstrap_servers = 'localhost:9092',
                             group_id='group1')
    msg = next(consumer)
    print(msg.value.decode())
    consumer.close()


def main():

    while True:
        start_consumer()
        r_num = random.randint(1, 4)
        print(f'mpc1 doing[{r_num}s]...')
        time.sleep(r_num)


if __name__ == '__main__':
    main()
```



#### 效果如下：

- consumer1

```
...
{"task_type": "mpc", "task_id": 37}
mpc1 doing[2s]...
{"task_type": "mpc", "task_id": 39}
mpc1 doing[2s]...
{"task_type": "mpc", "task_id": 40}
mpc1 doing[1s]...
{"task_type": "mpc", "task_id": 42}
mpc1 doing[4s]...
{"task_type": "mpc", "task_id": 44}
mpc1 doing[3s]...
{"task_type": "mpc", "task_id": 46}
mpc1 doing[1s]...
{"task_type": "mpc", "task_id": 48}
mpc1 doing[4s]...
{"task_type": "mpc", "task_id": 50}
mpc1 doing[4s]...
{"task_type": "mpc", "task_id": 53}
...
```



- consumer2

```
...
{"task_type": "mpc", "task_id": 35}
mpc2 doing[2s]...
{"task_type": "mpc", "task_id": 36}
mpc2 doing[4s]...
{"task_type": "mpc", "task_id": 38}
mpc2 doing[3s]...
{"task_type": "mpc", "task_id": 41}
mpc2 doing[3s]...
{"task_type": "mpc", "task_id": 43}
mpc2 doing[3s]...
{"task_type": "mpc", "task_id": 45}
mpc2 doing[3s]...
{"task_type": "mpc", "task_id": 47}
mpc2 doing[2s]...
{"task_type": "mpc", "task_id": 49}
mpc2 doing[4s]...
{"task_type": "mpc", "task_id": 51}
mpc2 doing[1s]...
{"task_type": "mpc", "task_id": 52}
...
```

