# 此方法有待确认
# val是不同的值！



from threading import Lock, Thread
# import time

class Singleton(object):
    # _instances = {}
    _instance_lock = Lock()
    val = None

    def __init__(self, val):
        # time.sleep(1)
        self.val = val

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance
        # with cls._instance_lock:
        #     if cls not in cls._instances:
        #         Singleton._instance = object.__new__(cls)  
        #         cls._instances[cls] = Singleton._instance
        # return cls._instances[cls]


def task(arg):
    # obj = Singleton()
    obj = Singleton(arg)
    print(obj, obj.val)

if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    for i in range(10):
        t = Thread(target=task,args=[i,])
        t.start()