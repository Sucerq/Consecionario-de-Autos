import uuid

from sqlalchemy import Boolean, Column, DateTime, String,Numeric,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Venta(Base):
    __tablename__ = "tbl_Venta"

    id_Venta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha = Column(DateTime,nullable=False)
    Precio_Venta = Column(Numeric(10,2), nullable=False)
    Metodo_Pago = Column(String(100), nullable=False)


    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_Usuarios"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuarios.id_Usuarios"), nullable=True
    )

    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    # --- Llaves foráneas ---
    id_Cliente = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Cliente.id_Cliente"), nullable=False
    )
    id_Empleado = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Empleado.id_Empleado"), nullable=False
    )
    # --- Relationships ---
    Cliente = relationship("Auto", foreign_keys=[id_Cliente])
    Empleado = relationship("Empleado", foreign_keys=[id_Empleado])