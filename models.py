from database import Base
from sqlalchemy import Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Seller(Base):
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True,)
    products: Mapped[list["Product"]] = relationship("Product", back_populates="seller",
                                                     cascade="all, delete-orphan")
    
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True,)
    description: Mapped[str] = mapped_column(String(length=500))
    price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    seller_id: Mapped[int] = mapped_column(Integer, ForeignKey("sellers.id"))
    seller: Mapped["Seller"] = relationship("Seller", back_populates="products")
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customers.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    product: Mapped["Product"] = relationship("Product", back_populates="orders")

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True,)
    orders: Mapped[list["Order"]] = relationship( "Order", back_populates="customer",
                                                 cascade="all, delete-orphan")
    