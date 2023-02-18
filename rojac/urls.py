from django.urls import path, re_path

from . import views
app_name = 'rojac'

urlpatterns = [
    # access api end point for creating a new user account
    path('create-user-account',
         views.CreateUserAccountApiView.as_view(), name='create-user'),

    # accesses api end point for creating a new client
    path('signup', views.CreateClientApiView.as_view(), name='signup'),

    # accesses an api end point for acquiring an expiring auth token
    path('login', views.CustomAuthToken.as_view(), name='login'),

    # accesses api end point for listing all clients
    path('clients', views.ListClientsApiView.as_view(), name='clients'),

    # accesses api end point for viewing a specific client
    path('clients/<str:pk>/', views.SpecificClientApiView.as_view(),
         name='specific-client'),


    # accesses api end point for updating client profile
    path('clients/<str:pk>/update', views.UpdateClientApiView.as_view(),
         name='update-client-profile'),

    re_path(
        r'^activate-account/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),

    # accesses api end point for adding new sale products
    path('add-commodity', views.AddCommodityApiView.as_view(), name='add-commodity'),

    # accesses api end point for listing all sale products in stock
    path('products', views.ListCommoditiesApiView.as_view(), name='products'),

    # accesses api end point for viewing a specific commodity
    path('products/<str:pk>/', views.SpecificCommodityApiView.as_view(),
         name='specific-product'),


    # accesses api end point for updating sale products
    path('products/<str:pk>/update', views.UpdateCommodityApiView.as_view(),
         name='update-commodity'),

    # c2b transaction initiation url
    path("c2b-initiate/", views.C2BInitiateAPIView.as_view(),
         name="c2b-initiate"),
    # c2b transaction validation url
    path("c2b-validation/", views.C2BValidationAPIView.as_view(),
         name="c2b-validation"),

    # c2b transaction confirmation url
    path("c2b-confirmation/", views.C2BConfirmationAPIView.as_view(),
         name="c2b-confirmation"),
]
