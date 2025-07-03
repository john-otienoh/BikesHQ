from category.models import Category

def menu_links(request):
    # links = Category.objects.filter(parent__isnull=True)
    links=Category.objects.all()
    return dict(links=links)