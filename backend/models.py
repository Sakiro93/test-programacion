from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class DateModel(models.Model):
    state = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class DateCreationModel(models.Model):
    state = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class CategoryClient(DateModel):
    name = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.date_update = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Categoria Cliente'
        verbose_name_plural = 'Categorias Cliente' \

        ordering = ('name',)

class Client(DateModel):
    idcategory = models.ForeignKey(CategoryClient, on_delete=models.PROTECT, verbose_name='CategoryClient')
    name = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        self.date_update = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.dni, self.name)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('name',)


class Sale(DateCreationModel):
    idcliente = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Client')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.idcliente.dni, self.total)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ('date_creation',)

class Category(DateModel):
    name = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.date_update = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('name',)

class Product(models.Model):
    idcategory = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    state_iva = models.BooleanField(default=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ('name',)

class DetailSale(models.Model):
    idsale = models.ForeignKey(Sale, on_delete=models.PROTECT, verbose_name='Sale')
    idproduct = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Product')

    def __str__(self):
        return "{}".format(self.idsale)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles Venta'
        ordering = ('idsale',)

