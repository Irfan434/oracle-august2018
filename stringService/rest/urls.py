from django.urls import path

from . import views

urlpatterns = [
    path('stringClean/', views.stringClean, name='stringClean'),
    path('stringClean/<str:iStr>', views.stringClean, name='stringClean'),
    path('maxBlock/', views.maxBlock, name='maxBlock'),
    path('maxBlock/<str:iStr>', views.maxBlock, name='maxBlock'),
    path('reorderBlock/', views.reorderBlock, name='reorderBlock'),
    path('reorderBlock/<str:iStr>', views.reorderBlock, name='reorderBlock'),
]