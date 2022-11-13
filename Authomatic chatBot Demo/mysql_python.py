import string
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#creamos la tabla de productos
class Producto(Base):
    __tablename__ = 'producto'
    idProducto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    precio = Column(Integer)
    cantidad_producto = Column(Integer)
    clave_almacen = Column(String(8))
    #creamos la relacion con la tabla de almacen
    Producto_Pedido = relationship("ProductoPedido", back_populates="producto", cascade="all, delete-orphan")

def __repr__(self):
    return f"Producto(idProducto = {self.idProducto!r},nombre={self.nombre!r}, descripcion={self.descripcion!r}, precio={self.precio!r}, cantidad_producto={self.cantidad_producto!r}, clave_almacen={self.clave_almacen!r})"

#creamos la tabla de producto pedido
class ProductoPedido(Base):
    __tablename__ = 'producto_pedido'
    idProductoPedido = Column(Integer, primary_key=True, autoincrement=True)
    idProducto = Column(Integer, ForeignKey('producto.idProducto'))
    idPedido = Column(Integer, ForeignKey('pedido.idPedido'))
    cantidad = Column(Integer)
    producto = relationship("Producto", back_populates="Producto_Pedido", cascade="all, delete-orphan")
    pedido = relationship("Pedido", back_populates="Producto_Pedido", cascade="all, delete-orphan")

def __repr__(self):
    return f"ProductoPedido(idProductoPedido = {self.idProductoPedido!r},idProducto={self.idProducto!r}, idPedido={self.idPedido!r}, cantidad={self.cantidad!r})"
    

#creamos la tabla de cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    idCliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(250), nullable=False)
    telefono = Column(Integer)
    #creamos la relacion con la tabla de pedido
    Cliente_Pedido = relationship("Pedido", back_populates="cliente")

def __repr__(self):
    return f"Cliente(idCliente = {self.idCliente!r},nombre={self.nombre!r}, telefono={self.telefono!r})"

#creamos la tabla de cita
class Cita(Base):
    __tablename__ = 'cita'
    idCita = Column(Integer, primary_key=True, autoincrement=True)
    fechaYhora = Column(String(500), nullable=False)
    direccion = Column(String(350))
    cita_relation = relationship("Pedido", back_populates="cita")

    
#creamos la tabla de pedido
class Pedido(Base):
    __tablename__ = 'pedido'
    idPedido = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, ForeignKey('cliente.idCliente'))
    idCita = Column(Integer, ForeignKey('cita.idCita'))
    #creamos la relacion con la tabla de cliente
    cliente = relationship("Cliente", back_populates="pedido", cascade="all, delete-orphan")
    #creamos la relacion con la tabla de cita
    cita = relationship("Cita", back_populates="cita_relation", cascade="all, delete-orphan")

def __repr__(self):
    return f"Pedido(idPedido = {self.idPedido!r},idCliente={self.idCliente!r}, idCita={self.idCita!r})"

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@localhost/Nenis?charset=utf8mb4", echo=True)
Base.metadata.create_all(engine)