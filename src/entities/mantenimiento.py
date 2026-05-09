import uuid

from sqlalchemy import Boolean, Column, DateTime, String,Numeric,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Mantenimiento(Base):
    __tablename__ = "tbl_Mantenimiento"

    id_Mantenimiento = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Fecha = Column(DateTime,default=True)
    Tipo_Servicio = Column(String(50), nullable=False)
    Costo = Column(Numeric(10,2),nullable=False)
   

        # --- Auditoria ---

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=True
    )

    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    # --- Llaves foráneas ---
    id_Auto = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Auto.id_Auto"), nullable=False
    )
    id_Empleado = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Empleado.id_Empleado"), nullable=False
    )
    # --- Relationships ---
    Auto = relationship("Auto", foreign_keys=[id_Auto])
    Empleado = relationship("Empleado", foreign_keys=[id_Empleado])