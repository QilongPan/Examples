import pymysql.cursors

class MysqlDB(object):
    
    def __init__(self,**kwargs):
        self.host = kwargs.get("host","127.0.0.1")
        self.user = kwargs.get("user","root")
        self.password = kwargs.get("password","root")
        self.database = kwargs.get("database","qa")
        self.connection = pymysql.connect(host = self.host,user = self.user, 
                                            password = self.password,database = self.database)

    def select(self,sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
                return result
        finally:
            pass

    def select_all(self,sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def insert(self,sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()     

    def delete(self):
        pass

    def update(self,sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)     
        self.connection.commit()       

    def drop_table(self,table_name):
        sql = "drop table %s"%(table_name)
        self.execute(sql)

    def create_table(self,sql):
        self.execute(sql)
        
    def show_tables(self):
        sql = "show tables like 'real_evil_phones2'"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    def is_exist_table(self,table_name):
        sql = "show tables like '%s'"%(table_name)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) > 0:
                return True
            else:
                return False

    def execute(self,sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)

    def import_csv(self,file_path,table_name):
        sql  = "load data infile '%s' INTO TABLE %s FIELDS TERMINATED BY ',';"%(file_path,table_name)
        self.execute(sql)
        self.connection.commit()
    
    def export_csv(self):
        pass

    def close(self):
        self.connection.close()

class OperateTable(object):

    def __init__(self,host,user,password,database,table_name) -> None:
        self.db = MysqlDB(host = host,user = user, password = password,database = database)
        self.table_name = table_name

    def insert(self,id,score):
        if not self.db.is_exist_table(self.table_name):
            self.db.create_table(f"create table {self.table_name}(id int(11),score float8,PRIMARY KEY (id));")     
        result = self.db.select(f"SELECT * from {self.table_name} where id = '{id}'")
        if result is not None and len(result) > 0:
            self.db.update(f"update {self.table_name} set score='{score}' where id = '{id}'")
        else:
            self.db.insert(f"INSERT INTO `{self.table_name}` (`id`, `score`) VALUES ({id}, {score})")       

    def getHighScoreData(self,data_num):
        datas = self.db.select_all(f"select * from {self.table_name};")
        datas = sorted(datas,key = lambda x:x[1],reverse=True)
        datas = datas[0:data_num]
        result = dict()
        for i in range(len(datas)):
            result[datas[i][0]] = datas[i][1]
        print(result)
        return result

    def close(self):
        self.db.close()


if __name__ == '__main__':
    host = "127.0.0.1"
    user = "root"
    password = "root"
    database = "qa"
    table_name = "scores"
    ot = OperateTable(host,user,password,database,table_name)
    ot.insert(2000,100)
    ot.getHighScoreData(10)
    ot.close()
    # db = MysqlDB(host = host,user = user, password = password,database = database)
    # if not db.is_exist_table(table_name):
    #     db.create_table(f"create table {table_name}(id int(11),score float8,PRIMARY KEY (id));")
    # id = 10007
    # score = 99
    # result = db.select(f"SELECT * from {table_name} where id = '{id}'")
    # if result is not None and len(result) > 0:
    #     new_score = 105
    #     db.update(f"update {table_name} set score='{new_score}' where id = '{id}'")
    # else:
    #     db.insert(f"INSERT INTO `{table_name}` (`id`, `score`) VALUES ({id}, {score})")
    # db.close()