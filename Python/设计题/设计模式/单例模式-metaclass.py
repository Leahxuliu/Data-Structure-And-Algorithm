'''
基于metaclass + 锁
'''

"""
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""



from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}
    _lock = Lock()
    
    # 通过call 实现类装饰器.
    def __call__(self, *args, **kwargs):

        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with self._lock:
            if self not in self._instances:
                # super() 函数是用于调用父类(超类)的一个方法
                self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    value = None

    def __init__(self, value):
        self.value = value

    def some_business_logic(self):
        return

def test_singleton(value):
    singleton = Singleton(value)
    print(singleton, singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    for i in range(10):
        process = Thread(target=test_singleton, args=(i,))
        process.start()
