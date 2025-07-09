from database.DB_connect import DBConnect
from model.go_retailers import Go_retailers


class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAllNations():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select distinct(gr.Country) 
                from go_retailers gr 
                order by gr.Country"""
        cursor.execute(query,)
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(stato):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select *
                from go_retailers gr 
                where gr.Country = %s"""
        cursor.execute(query, (stato,))
        for row in cursor:
            result.append(Go_retailers(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(anno, retailer_01: Go_retailers, retailer_02: Go_retailers):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select t3.R1, t3.R2, COUNT(distinct(t3.Product_number)) as peso
                from (
                select t1.Retailer_code as R1, t2.Retailer_code as R2, t1.Product_number
                from ((select *
                from go_daily_sales gds1
                where gds1.Retailer_code = %s and year(gds1.`Date`)=%s) t1
                inner join
                (select *
                from go_daily_sales gds2
                where gds2.Retailer_code = %s and year(gds2.`Date`)=%s) t2
                on t1.Product_number = t2.Product_number)) t3
                group by t3.R1, t3.R2"""
        cursor.execute(query, (retailer_01.Retailer_code, anno, retailer_02.Retailer_code, anno,))
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            conn.close()
            return None
        arco = (row["R1"], row["R2"], row["peso"])
        cursor.close()
        conn.close()
        return arco