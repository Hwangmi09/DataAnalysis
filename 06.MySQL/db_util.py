import pymysql

# 월별 매출/이익
def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 거래처별 매출/이익
def get_correspondent_revenue(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany, SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY scompany
            ORDER BY revenue;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 거래처별 판매제품 및 수량
def get_correspondent_sales(config, company):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
         SELECT  pname, sum(sunit)
            FROM sales_book
            WHERE scompany=%s
            GROUP BY pname;
    """
    
    category_sales = []
    cur.execute(sql, (company,))
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 제품별 판매수량/매출/이익
def get_product_sales(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname  AS '제품', SUM(sunit) AS '판매수량',
            SUM(revenue) AS '매출', sum(profit) AS '이익'
            FROM sales_book
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 카테고리별 매출/이익
def get_category_sales(config):

    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pcategory AS '카테고리',
            SUM(revenue) AS '매출', sum(profit) AS '이익'
            FROM sales_book
            GROUP BY pcategory;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 거래처별 판매제품 및 수량 - 강사님 풀이
def get_correspondent_sales2(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
         SELECT  scompany, pname, sum(sunit) as unit
            FROM sales_book
            GROUP BY scompany, pname
            order by scompany;
    """
    
    category_sales = []
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results