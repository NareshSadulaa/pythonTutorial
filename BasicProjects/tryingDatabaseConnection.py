import mysql.connector

cnx = mysql.connector.connect(user='root',password='root@123',
                              host='localhost',
                              port='3306',
                              database='e-com')
cursor = cnx.cursor()
query = ("INSERT INTO `e-com`.`products` (`products_id`, `products_name`, `products_unit`, `price_per_product`) VALUES('2', 'BackCovers', '1', '100')")
cursor.execute(query)
cnx.close()

