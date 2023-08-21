import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import Publisher, create_tables,Book, Shop, Stock, Sale
import datetime


def Tables_fill(session):
    pb1 = Publisher(publisher_name="Эксмо")
    pb2 = Publisher(publisher_name="ACT")
    session.add_all([pb1, pb2])
    session.commit()

    book1 = Book(title="Отличное чтение", publisher=pb2)
    book11 = Book(title="Неплохая книга", publisher=pb1)
    book2 = Book(title="Просто книга", publisher=pb2)
    book21 = Book(title="Не оторваться...", publisher=pb2)
    session.add_all([book1, book11, book2, book21])
    session.commit()

    shop1 = Shop(shop_name="Буквоед")
    shop2 = Shop(shop_name="Лабиринт")
    shop3 = Shop(shop_name="Книги на Ямской")
    shop4 = Shop(shop_name="Научная книга")
    session.add_all([shop1, shop2, shop3, shop4])
    session.commit()

    st1 = Stock(book=book1, shop=shop1, count=123)
    st2 = Stock(book=book21, shop=shop2, count=18)
    st3 = Stock(book=book2, shop=shop1, count=155)
    st4 = Stock(book=book21, shop=shop4, count=14)
    session.add_all([st1, st2, st3, st4])
    session.commit()

    sal1 = Sale(price=560, count=126, stock=st1, data_sale=datetime.datetime.strptime('2023-08-08', '%Y-%m-%d').date())
    sal2 = Sale(price=200, count=12, stock=st2, data_sale=datetime.datetime.strptime('2023-08-01', '%Y-%m-%d').date())
    sal3 = Sale(price=220, count=44, stock=st1, data_sale=datetime.datetime.strptime('2023-07-09', '%Y-%m-%d').date())
    sal4 = Sale(price=561, count=52, stock=st2, data_sale=datetime.datetime.strptime('2022-12-08', '%Y-%m-%d').date())
    sal5 = Sale(price=488, count=44, stock=st3, data_sale=datetime.datetime.strptime('2023-07-09', '%Y-%m-%d').date())
    sal6 = Sale(price=610, count=52, stock=st4, data_sale=datetime.datetime.strptime('2022-12-08', '%Y-%m-%d').date())
    session.add_all([sal1, sal2, sal3, sal4, sal5, sal6])
    session.commit()

def Query_execute(session):
   publ_input= input("Введите издателя: ")
   q=session.query(Book.title, Shop.shop_name, Sale.price, Sale.data_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.publisher_name==publ_input)
   for s in q.all():
    print(f"{s.title:20} | {s.shop_name:16} | {s.price} | {s.data_sale}")

if __name__ == '__main__':
    DSN = "postgresql://postgres:post_oxana@localhost:5432/oxana_db"
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Tables_fill(session)
    Query_execute(session)



