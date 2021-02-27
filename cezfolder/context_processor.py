from nav_menu.models import NavMenu
from textpages.models import TextPages


def global_processor(request):
    menu_items = NavMenu.objects.filter(is_first_level=True).order_by("order")
    about_us_page = TextPages.objects.filter(active=True, page_type='aboutus').first()
    terms_page = TextPages.objects.filter(active=True, page_type='terms').first()
    context = {
        "menu_items": menu_items,
        'about_us_page': about_us_page,
        'terms_page': terms_page,
    }

    return context
