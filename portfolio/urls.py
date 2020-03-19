from django.urls import path
from .import views

from .views import (
    TransactionPageView,
)


urlpatterns = [
    path('', views.portfolio, name='portfolio-portfolio'),
    # path('', views.portfolio.as_view(), name='portfolio-portfolio'),
    path('addstock/', views.addstock.as_view(), name='portfolio-addstock'),
    path('viewstock/', views.viewstock, name='portfolio-viewstock'),
    path('view_individual_stock_data/', views.view_individual_stock_data, name='portfolio-view_individual_stock_data'),
    path('comparestock/', views.comparestock, name='portfolio-compare-stock'),
    path('stock_options/', views.stock_options, name='portfolio-stock-options'),
    path('transaction_page/', TransactionPageView.as_view(), name='portfolio-transaction-page'),
    path('view_portfolio/', views.viewPortfolio, name='portfolio-view-portfolio'),
    path('create_portfolio/', views.addportfolio.as_view(), name='portfolio-create-portfolio'),
    path('advanced_analysis/', views.advanced_analysis, name='portfolio-advanced-analysis'),
]

