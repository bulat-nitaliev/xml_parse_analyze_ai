import xml.etree.ElementTree as ET
import psycopg2 
from django.conf import settings
from datetime import datetime
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from decouple import config




def xml_to_dict_recursive(root):
        """
        Recursively walk through the root and turn it into a dict.
        :param root: <class 'xml.etree.ElementTree.Element'>
        :return: dict
        """
        
        for children in root.iter():
            if len(children) == 0:
                if root.text is not None:
                    return {root.tag: root.text.strip()}
            else:
                return  {root.tag: list(map(xml_to_dict_recursive, children))}



def lst_products(path, lst_product=None)->list:
    root = ET.parse(path).getroot()
    date_product = root.get('date')
    if lst_product is None:
        lst_product = []
    dic = xml_to_dict_recursive(root)
    
    # print(dic)
    for i in dic['sales_data'][0]['products']:
        prod_id = None if i['product'][0] is None else i['product'][0]['id']
        name = None if i['product'][1] is None else i['product'][1]['name']
        quantity = None if i['product'][2] is None else i['product'][2]['quantity']
        price = None if i['product'][3] is None else i['product'][3]['price']
        category = None if i['product'][4] is None else i['product'][4]['category']
        lst_product.append((prod_id, name, quantity, price, category, date_product))

    return lst_product


def insert_data(data):
    db = settings.DATABASES['default']
    print(db)
    name, user, pwd, host, port = db['NAME'], db['USER'], db['PASSWORD'], db['HOST'], db['PORT']

    dsn = f'''dbname={name} user={user} password={pwd} host={host} port={port}'''
    with psycopg2.connect(dsn) as conn:
        cur = conn.cursor()
        key = '''insert into core_product (prod_id, name, quantity, price, category, date_product) values %s'''
        psycopg2.extras.execute_values(cur, key, data, page_size=1000)



def generate_report(date):
    db = settings.DATABASES['default']
    name, user, pwd, host, port = db['NAME'], db['USER'], db['PASSWORD'], db['HOST'], db['PORT']
    
    dsn = f'''dbname={name} user={user} password={pwd} host={host} port={port}'''
    
    date_str = datetime.strptime(date, '%Y-%m-%d').date()

    with psycopg2.connect(dsn) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT SUM(price * quantity) FROM core_product
            WHERE date_product = %s
        """, (date_str,))
        total_revenue = cur.fetchone()

        # 2. Топ-3 товара по продажам
        cur.execute("""
            SELECT name, SUM(quantity) as total_sold
            FROM core_product
            WHERE date_product = %s
            GROUP BY name
            ORDER BY total_sold DESC
            LIMIT 3
        """, (date_str,))
        top_products = cur.fetchall()

        # 3. Распределение по категориям
        cur.execute("""
            SELECT category, SUM(quantity) as total_quantity
            FROM core_product
            WHERE date_product = %s
            GROUP BY category
        """, (date_str,))
        categories = cur.fetchall()

        # Закрытие курсора
        cur.close()

        # Формируем отчет
        report = {
            "total_revenue": total_revenue,
            "top_products": top_products,
            "categories": categories
        }
        return report

    

def analytical_report(prompt):
    llm = GigaChat(
        credentials=config('TOKEN'),
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        # Отключает проверку наличия сертификатов НУЦ Минцифры
        verify_ssl_certs=False,
        streaming=False,
    )
    messages = [
        SystemMessage(
            content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
        )
    ]

    
    messages.append(HumanMessage(content=prompt))
    res = llm.invoke(messages)
    messages.append(res)
    result = res.content
    return result




        
     
