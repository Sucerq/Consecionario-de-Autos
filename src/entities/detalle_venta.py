# src/entities/detalle_venta.py
import uuid

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Detalle_Venta(Base):
    __tablename__ = "tbl_Detalle_Venta"

    id_Detalle_Venta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # --- Auditoría (FK corregida: tbl_usuario.id_Usuario) ---
    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=True
    )

    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    # --- Llaves foráneas ---
    id_Venta = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Venta.id_Venta"), nullable=False
    )
    id_Auto = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Auto.id_Auto"), nullable=False
    )

    # --- Relationships (corregidos: cada uno apunta a su modelo real) ---
    Venta = relationship("Venta", foreign_keys=[id_Venta])
    Auto = relationship("Auto", foreign_keys=[id_Auto])