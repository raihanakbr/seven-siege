from django.urls import path
from main.views import show_main, create_item, show_html, show_xml, show_json, show_xml_by_id, show_json_by_id, \
register, login_user, logout_user, add_amount, subtract_amount, remove_item, get_item_json, create_ajax

app_name = 'main'

urlpatterns = [
    path('create-item', create_item, name='create_item'),
    path('add/<int:item_id>/', add_amount, name='add_amount'),
    path('subtract/<int:item_id>/', subtract_amount, name='subtract_amount'),
    path('remove/<int:item_id>/', remove_item, name='remove_item'),
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('html/', show_html, name='show_html'), 
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
]