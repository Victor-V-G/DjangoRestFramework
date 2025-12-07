from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import re

# Create your models here.
class Empleado(models.Model):

    #Validaciones
    def validacion_rut_real(value):
        expresion = r"^\d{7,8}-[\dK]$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('Ingrese un rut valido (01234567-k) con guion y sin puntos.')
    
    def validacion_nombre_y_apellido_real(value):
        expresion = r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('No se permiten numeros y caracteres especiales')
        
    def validacion_edad_negativa(value):
        if value < 0:
            raise ValidationError('No se permiten edades negativas')
        
    def validacion_largo_y_solo_numeros(value):
        expresion = r"^9\d{8}$"
        validarInput = str(value)
        if value < 0:
            raise ValidationError('No se permiten numeros negativos')
        if len(validarInput) != 9:
            raise ValidationError('El numero telefonico debe tener exactamente 9 digitos')
        if not validarInput.isdigit():
            raise ValidationError('Solo se permiten números')
        if re.match(expresion, validarInput):
            return value
        else:
            raise ValidationError("El número debe comenzar con 9 y tener exactamente 9 dígitos numéricos.")


    #Modelos
    id_empleado = models.AutoField(
        primary_key=True
    )

    rut_empleado = models.CharField(
        max_length=10, 
        verbose_name="Rut (01234567-k)",
        validators=[validacion_rut_real],
        error_messages={'unique': 'El rut ingresado ya se encuentra registrado, Por favor, verifique.'}
    )

    nombre_empleado = models.CharField(
        max_length=20, 
        verbose_name="Nombre del empleado",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(3, message="Por favor, ingrese un nombre real")
        ]
    )

    apellido_empleado = models.CharField(
        max_length=55, 
        verbose_name="Apellido del empleado",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(3, message="Por favor, ingrese un apellido real")
        ]
    )

    edad_empleado = models.IntegerField( 
        verbose_name="Edad",
        validators=[
            validacion_edad_negativa,
            MinValueValidator(18, message="Debes tener al menos 18 años"),
            MaxValueValidator(99, message="Edad invalida, no puede tener mas de 100 años")
        ]
    )

    numero_telefonico = models.IntegerField(
        verbose_name="Telefono (912345678)",
        validators=[validacion_largo_y_solo_numeros]
    )


    #clase meta
    class Meta:
        db_table = 'Empleado'
        constraints = [
            # Asegura que no haya dos registros con el mismo ID.
            UniqueConstraint(fields=['id_empleado'], name='unique_id_empleado'),
            # Asegura que el RUT sea único entre todos los empleados.
            UniqueConstraint(fields=['rut_empleado'], name='unique_rut_empleado'),
        ]


    #metodo str
    def __str__(self):
        return f"Nombre Completo: {self.nombre_empleado} {self.apellido_empleado}, Rut: {self.rut_empleado}"
