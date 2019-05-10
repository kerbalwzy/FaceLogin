from threading import Lock as ThreadLock


def single_instance(cls):
    """
    通过装饰器的实现任何类的单例模式，并且通过线程锁，实现了单例模式的线程安全
    """
    __instance = dict()
    __instance_lock = ThreadLock()

    def _single_instance(*args, **kwargs):
        if cls not in __instance:
            with __instance_lock:
                if cls not in __instance:
                    __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return _single_instance


if __name__ == '__main__':
    import threading
    import time


    def task(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        print(instance)


    def test_single_decorator(cls, *args, **kwargs):
        print("+++++++++++++++++++++++++")
        args = cls, *args
        for i in range(5):
            t = threading.Thread(target=task, args=args, kwargs=kwargs)
            t.start()
        time.sleep(3)
        obj = cls()
        print(obj)
        print("==========================")


    @single_instance
    class Test001:
        pass


    @single_instance
    class Test002:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return super().__str__() + self.name


    test_single_decorator(Test001)
    test_single_decorator(Test002, name="小王", age=19)
