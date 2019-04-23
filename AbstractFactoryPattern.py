#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
大话设计模式
设计模式——抽象工厂模式
抽象工厂模式(Abstract Factory Pattern):提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类
"""
import sys

#抽象用户表类
class User(object):

    def get_user(self):
        pass

    def insert_user(self):
        pass

#抽象部门表类
class Department(object):

    def get_department(self):
        pass

    def insert_department(self):
        pass


#操作具体User数据库类-Mysql
class MysqlUser(User):

    def get_user(self):
        print('MysqlUser get User')

    def insert_user(self):
        print('MysqlUser insert User')

#操作具体Department数据库类-Mysql
class MysqlDepartment(Department):

    def get_department(self):
        print('MysqlDepartment get department')

    def insert_department(self):
        print('MysqlDepartment insert department')

#操作具体User数据库-Oracle
class OracleeUser(User):

    def get_user(self):
        print('OracleUser get User')

    def insert_user(self):
        print('OracleUser insert User')

#操作具体Department数据库类-Oracle
class OracleeDepartment(Department):

    def get_department(self):
        print('OracleDepartment get department')

    def insert_department(self):
        print('OracleDepartment insert department')

#抽象工厂类
class AbstractFactory(object):

    def create_user(self):
        pass

    def create_department(self):
        pass

class MysqlFactory(AbstractFactory):

    def create_user(self):
        return MysqlUser()

    def create_department(self):
        return MysqlDepartment()

class OracleeFactory(AbstractFactory):

    def create_user(self):
        return OracleeUser()

    def create_department(self):
        return OracleeDepartment()

if __name__ == "__main__":

    db = input('请输入数据库类型(仅支持Mysql和Oracle)：')
    myfactory = ''
    if db == 'Mysql':
        myfactory = MysqlFactory()
    elif db == 'Oracle':
        myfactory = OracleeFactory()
    else:
        print("不支持的数据库类型")
        exit(0)
    user = myfactory.create_user()
    department = myfactory.create_department()
    user.insert_user()
    user.get_user()
    department.insert_department()
    department.get_department()