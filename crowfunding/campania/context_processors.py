from campania.models import Categoria

def get_all_categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias':categorias}