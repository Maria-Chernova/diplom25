"""netology_pd_diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from backend.views import (
    OrderView,
    ContactView,
    PartnerOrders,
    PartnerUpdate,
    PartnerState,
)

app_name = 'backend'

urlpatterns = [
    # Заказы
    path('orders/', OrderView.as_view(), name='order_list'),  # Получить и разместить заказы
    path('orders/<int:pk>/', OrderView.as_view(), name='order_detail'),  # Получить или изменить конкретный заказ

    # Контакты
    path('contacts/', ContactView.as_view(), name='contact_list'),  # Получить и добавить контакты
    path('contacts/<int:pk>/', ContactView.as_view(), name='contact_detail'),  # Изменить или удалить контакт

    # Заказы поставщиков
    path('partner/orders/', PartnerOrders.as_view(), name='partner_orders'),  # Получить заказы поставщика

    # Обновление прайса от поставщика
    path('partner/update/', PartnerUpdate.as_view(), name='partner_update'),  # Обновление прайса

    # Статус поставщика
    path('partner/state/', PartnerState.as_view(), name='partner_state'),  # Получить и изменить статус поставщика
]