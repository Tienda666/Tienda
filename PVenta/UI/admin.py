from django.contrib import admin
# Register your models here.
from.models import Cliente
admin.site.register(Cliente)

from.models import TipoCliente
admin.site.register(TipoCliente)

from.models import Articulo
admin.site.register(Articulo)

from.models import Categoria
admin.site.register(Categoria)

from.models import Venta
admin.site.register(Venta)

from.models import DetalleVenta
admin.site.register(DetalleVenta)

from.models import Apartar
admin.site.register(Apartar)

from.models import Abono
admin.site.register(Abono)