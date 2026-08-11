import allure
from utils.logger import Logger
from functools import wraps

class Reporter:

    @staticmethod
    def step(name):
        Logger.info(name)
        return allure.step(name)

    # @staticmethod
    # def step(name):
    #     def decorator(func):
    #         @wraps(func)
    #         def wrapper(*args, **kwargs):
    #             step_name = name.format(*args, **kwargs)
    #             Logger.info(name)
    #             with allure.step(step_name):
    #                 return func(*args, **kwargs)
    #             return wrapper
    #         return decorator
        
    