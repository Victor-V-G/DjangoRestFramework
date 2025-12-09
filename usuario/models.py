from django.db import models
from empleado.models import Empleado  # ajusta el import según tu estructura real
from django.contrib.auth.models import User

class Usuario(models.Model):

    id_usuario = models.AutoField(
        primary_key=True,
    )

    # ============================================================
    # LLAVES FORÁNEAS
    # ============================================================

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil"
    )

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        related_name="usuario",
        db_column="empleado_id",
        null=True,
        blank=True
    )

    # ============================================================
    # CLASE META
    # ============================================================

    class Meta:
        db_table = 'Usuario'

    # ============================================================
    # MÉTODO STR
    # ============================================================

    def __str__(self):
        return f"ID: {self.id_usuario} | EMPLEADO: {self.empleado} | PERFIL: {self.user}"
