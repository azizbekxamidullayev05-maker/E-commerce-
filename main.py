from database import Base, engine, SessionLocal
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from models import Product, Seller
#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


session = SessionLocal()

try:
    #stmt=select(Product).options(selectinload(Product.seller))
    #products = session.scalars(stmt).all()
    #for product in products:
        #print(product.name, product.price, product.seller.name)

    stmt=select(Seller).options(joinedload(Seller.products, innerjoin=True)) #1 to n, m2m
    sellers = session.execute(stmt).unique().scalars().all()
    for seller in sellers:
        print(seller.name)
        for product in seller.products:
            print(f"\t{product.name} - {product.price}")

except Exception as error:
    session.rollback()
    print(f"NIMADIR XATO KETDI: {error}")

finally:
    session.close()
