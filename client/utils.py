from threading import Lock as ThreadLock
import time


class SingleInstance:
    """
    作为一个用来实现单例的父类使用，
    当有一个类继承「包含多继承」于这个类时，这个类创建的实例对象必定符合单例模式。
    并且是线程安全的单例模式
    """

    __instance_lock = ThreadLock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            with cls.__instance_lock:
                if not hasattr(cls, "__instance"):
                    cls.__instance = object.__new__(cls)
        return cls.__instance


def single_instance(cls):
    """
    通过装饰器的实现任何类的单例模式
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


    def task(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        print(instance)


    for i in range(5):
        t = threading.Thread(target=task, args=(SingleInstance,))
        t.start()

    import time

    time.sleep(5)
    obj = SingleInstance()
    print(obj)
