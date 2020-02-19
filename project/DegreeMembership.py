class DegreeMembership:
    import numpy as np
    import pymysql
    import json
    import math
    # global a
    # a = {"host": '127.0.0.1', "user": 'root', "passwd": '110', "db": 'jingzhen1', "port": 3306, "charset": 'utf8'}
    def __init__(self):
       self.a=""

    #=========================隶属度函数BEGIN=====================================================
    #金钱标准化函数
    def Money_normalize(self,money):
        return money / 2500000
    #次数标准化函数
    def Times_normalize(self,times):
        return times / 150
        

    def membershipFun(self,money, times, Actor_a=0.6, Actor_b=0.4):
        #金钱标准化函数
        money_x = self.Money_normalize(money)
        times_x = self.Times_normalize(times)
        result=Actor_a*self.math.tanh(money_x)+Actor_b*self.math.tanh(times_x)
        return result
        
    #=========================隶属度函数END=====================================================





        