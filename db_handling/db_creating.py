import sys, random
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class CreateDataBase():
    print(QSqlDatabase.drivers())


if __name__ == '__main__':
    CreateDataBase()