from django.db import models

# Create your models here.


class Persona(models.Model):
    # Opciones(Choices)
    GENEROS = [
        ('MUJER', 'Mujer'),
        ('HOMBRE', 'Hombre')
    ]

    ESTATUS = [
        ('AMIGO', 'Amigo'),
        ('PASIVO', 'Pasivo'),
        ('ACTIVO', 'Activo')
    ]

    ESTADO_CIVIL = [
        ('SOLTERO', 'Soltero(a)'),
        ('CASADO', 'Casado(a)'),
        ('UNION LIBRE', 'Union Libre'),
        ('SEPARADO', 'Separado(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
        ('VIUDO', 'Viudo(a)')
    ]

    GRUPO_SOCIAL = [
        ('DAMAS', 'Damas'),
        ('VARONES', 'Varones'),
        ('JÓVENES', 'Jóvenes'),
        ('ADOLESCENTES', 'Adolescentes'),
        ('NIÑOS', 'Niños')
    ]

    MOTIVO_DE_ALTA = [
        ('CAPTURA_INICIAL', 'Captura Inicial'),
        ('TRASLADO', 'Traslado'),
        ('INCORPORACION', 'Incorporación'),
        ('OTRO', 'Otro')
    ]

    BAUTISMO_EN_AGUA = [
        ('SI', 'Si'),
        ('NO', 'No')
    ]

    # Datos personales
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(
        max_length=50, null=True, blank=True, default='')
    apellido_materno = models.CharField(
        max_length=50, null=True, blank=True, default='')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.CharField(null=True, blank=True, max_length=200)
    genero = models.CharField(choices=GENEROS, max_length=6)
    direccion = models.CharField(
        max_length=250, null=True, blank=True, default='')
    telefono_movil = models.CharField(
        max_length=10, null=True, blank=True, default='')
    telefono_casa = models.CharField(
        max_length=10, null=True, blank=True, default='')
    email = models.CharField(max_length=100, null=True, blank=True, default='')

    estatus = models.CharField(choices=ESTATUS, max_length=10, default='AMIGO')
    notas = models.TextField(null=True, blank=True)

    # Datos familiares
    # auxiliar = models.ForeignKey(
    #     Persona, null=True, on_delete=models.SET_NULL, related_name='auxiliar', default=None)
    padre = models.ForeignKey(
        'self', null=True, blank=True,  on_delete=models.SET_NULL, related_name='hijo_del_padre', default=None)
    madre = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='hijo_de_la_madre', default=None)
    estado_civil = models.CharField(
        choices=ESTADO_CIVIL, max_length=15, null=True, blank=True)
    conyuge = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='conyuge_del_otro', default=None)
    fecha_matrimonio = models.DateField(null=True, blank=True)

    # Datos de la iglesia
    grupo_social = models.CharField(
        choices=GRUPO_SOCIAL, max_length=20, blank=True, null=True)
    motivo_de_alta = models.CharField(
        choices=MOTIVO_DE_ALTA, max_length=300, blank=True, null=True)
    fecha_conversion = models.DateField(null=True, blank=True)
    bautismo_en_agua = models.CharField(
        choices=BAUTISMO_EN_AGUA, max_length=10, blank=True, null=True)
    fecha_bautismo = models.DateField(null=True, blank=True)
    iglesia_bautismo = models.CharField(max_length=50, blank=True, null=True)
    experiencia_ministerial = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        apell_paterno = self.apellido_paterno
        apell_materno = self.apellido_materno
        if apell_paterno == None:
            apell_paterno = ''
        if apell_materno == None:
            apell_materno = ''
        else:
            apell_materno = self.apellido_materno
        return self.nombre + ' ' + str(apell_paterno) + ' ' + str(apell_materno)
