from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'rojac'

urlpatterns = [

    ######################### API URLS ###############################

    # access home page data
    path('home', views.HomePagedataApiView.as_view(), name='home'),
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

    # accesses api end point for adding new sale products
    path('add-product', views.AddProductApiView.as_view(), name='add-product'),

    # accesses api end point for listing all sale products in stock
    path('products', views.ListProductsApiView.as_view(), name='products'),

    # accesses api end point for viewing a specific commodity
    path('products/<str:pk>/', views.SpecificProductApiView.as_view(),
         name='specific-product'),

    # accesses api end point for updating sale products
    path('products/<str:pk>/update', views.UpdateProductApiView.as_view(),
         name='update-product'),

    # accesses api end point for adding new product category
    path('add-product-category', views.AddProductCategoryApiView.as_view(),
         name='add-product-category'),

    # accesses api end point for listing all products categories
    path('product-categories', views.ListProductCategoriesApiView.as_view(),
         name='product-categories'),

    # accesses api end point for viewing a specific product category
    path('product-categories/<str:pk>/', views.SpecificProductCategoryApiView.as_view(),
         name='specific-product-category'),

    # accesses api end point for updating product categories
    path('product-categories/<str:pk>/update', views.UpdateProductCategoryApiView.as_view(),
         name='update-product-category'),

    # accesses api end point for adding new product image
    path('add-product-image', views.AddProductImageApiView.as_view(),
         name='add-product-image'),

    # accesses api end point for listing all product images
    path('product-images', views.ListProductImagesApiView.as_view(),
         name='product-images'),

    # accesses api end point for viewing a specific product image
    path('product-images/<str:pk>/', views.SpecificProductImageApiView.as_view(),
         name='specific-product-image'),

    # accesses api end point for updating product images
    path('product-images/<str:pk>/update', views.UpdateProductImageApiView.as_view(),
         name='update-product-image'),

    # accesses api end point for adding new product variation image
    path('add-product-variation-image', views.AddProductVariationImageApiView.as_view(),
         name='add-product-variation-image'),

    # accesses api end point for listing all product variation images
    path('product-variation-images', views.ListProductVariationImagesApiView.as_view(),
         name='product-variation-images'),

    # accesses api end point for viewing a specific product variation image
    path('product-variation-images/<str:pk>/', views.SpecificProductVariationImageApiView.as_view(),
         name='specific-product-variation-image'),

    # accesses api end point for updating product variation images
    path('product-variation-images/<str:pk>/update', views.UpdateProductVariationImageApiView.as_view(),
         name='update-product-variation-image'),

    # accesses api end point for adding a new product variation
    path('add-product-variation', views.AddProductVariationApiView.as_view(),
         name='add-product-variation'),

    # accesses api end point for listing all products variations
    path('product-variations', views.ListProductVariationsApiView.as_view(),
         name='product-variations'),

    # accesses api end point for viewing a specific product variation
    path('product-variation/<str:pk>/', views.SpecificProductVariationApiView.as_view(),
         name='specific-product-variation'),

    # accesses api end point for updating product variations
    path('product-variations/<str:pk>/update', views.UpdateProductVariationApiView.as_view(),
         name='update-product-variation'),

    # c2b transaction initiation url
    path("c2b-initiate/", views.C2BInitiateAPIView.as_view(),
         name="c2b-initiate"),
    # c2b transaction validation url
    path("c2b-validation/", views.C2BValidationAPIView.as_view(),
         name="c2b-validation"),

    # c2b transaction confirmation url
    path("c2b-confirmation/", views.C2BConfirmationAPIView.as_view(),
         name="c2b-confirmation"),

    ######################### END OF API URLS ###############################

    ######################### OTHER URLS ###############################
    re_path(
        r'^activate-account/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.user_account_activation, name="activate-account"),
    #     path("account-activated", views.user_account_activated,
    #          name="account-activated"),
    #     path("login", views.login_request, name="login"),
    #     path("logout", views.logout_request, name="logout"),
    #     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #         template_name='password_reset_done.html'), name='password_reset_done'),
    #     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #         template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    #     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
    #         template_name='password_reset_complete.html'), name='password_reset_complete'),
    #     path("password_reset", views.password_reset_request, name="password_reset"),

    ######################### END OF OTHER URLS ###############################
]
