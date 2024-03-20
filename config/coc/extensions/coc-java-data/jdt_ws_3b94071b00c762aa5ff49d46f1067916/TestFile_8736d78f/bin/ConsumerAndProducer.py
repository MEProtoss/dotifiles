import threading
import time
import random

# 共享缓冲区
buffer = []
buffer_size = 5

# 锁对象用于保护共享缓冲区
buffer_lock = threading.Lock()

# 生产者函数
def producer():
    while True:
        item = random.randint(1, 100)
        with buffer_lock:
            if len(buffer) < buffer_size:
                buffer.append(item)
                print(f"Produced {item}. Buffer: {buffer}")
        time.sleep(random.uniform(0.1, 0.5))

# 消费者函数
def consumer():
    while True:
        with buffer_lock:
            if buffer:
                item = buffer.pop(0)
                print(f"Consumed {item}. Buffer: {buffer}")
        time.sleep(random.uniform(0.1, 0.5))

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 启动线程
producer_thread.start()
consumer_thread.start()

# 主线程等待子线程结束
producer_thread.join()
consumer_thread.join()

