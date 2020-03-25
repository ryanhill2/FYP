from django import forms
from django.utils.safestring import mark_safe
from .models import Stock, Portfolio


class stockForm(forms.ModelForm):
    stock_ticker = forms.CharField(label='Stock Ticker')
    number_of_shares = forms.CharField(label='Number of Shares')

    class Meta:
        model = Stock
        fields = ('stock_ticker', 'number_of_shares',)


class portfolioForm(forms.ModelForm):
    portfolio_name = forms.CharField(label='Portfolio Name')

    class Meta:
        model = Portfolio
        fields = ('portfolio_name',)

class AdvancedAnalysisForm(forms.Form):

    stock_names = forms.CharField(widget=forms.Textarea)

class graphAnalysisForm(forms.Form):
    stock_name = forms.CharField(label='stock_name')
    stock_start_date = forms.CharField(label='stock_start_date')
    stock_end_date = forms.CharField(label='stock_end_date')



