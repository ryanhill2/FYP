from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import stockForm, portfolioForm
from .models import Stock, Portfolio


# Create your views here.

def portfolio(request):
    stock_list = {
        'stocks': Portfolio.objects.all()
    }
    return render(request, 'portfolio/portfolio.html')

def viewPortfolio(request):
    stock_list = {
        'stocks': Portfolio.objects.all()
    }
    return render(request, 'portfolio/view_portfolio.html', stock_list)

def viewstock(request):
    stocks_list = {
        'stocks': Stock.objects.all()
    }
    return render(request, 'portfolio/view_stocks.html', stocks_list)

def comparestock(request):
    stocks_list = {
        'stocks': Stock.objects.all(),
        'portfolio': Portfolio.objects.all()[0]
    }
    return render(request, 'portfolio/compare_stocks.html', stocks_list)

def stock_options(request):
    stock_list = {
        'stocks': Portfolio.objects.all()
    }
    return render(request, 'portfolio/view_stock_options.html', stock_list)

def view_individual_stock_data(request):
    stock_list = {
        'portfolio': Portfolio.objects.all().last()
    }
    return render(request, 'portfolio/view_individual_stock_data.html', stock_list)


def create_portfolio(request):
    # stock_list = {
    #     'stocks': Portfolio.objects.all()
    # }
    return render(request, 'portfolio/create_portfolio.html')

def advanced_analysis(request):
    # stock_list = {
    #     'stocks': Portfolio.objects.all()
    # }
    return render(request, 'portfolio/advanced_analysis.html')



# class portfolio(TemplateView):
#     template_name = "portfolio/portfolio.html"

class TransactionPageView(TemplateView):
    template_name = "portfolio/transactions_page.html"

    def get(self, request):
        form = stockForm()
        stocks = Stock.objects.all().order_by('-stockCreated')
        args = {'form': form, 'stocks': stocks}
        return render(request, self.template_name, args)

    def post(self, request):
        form = stockForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['stock_ticker']
            form = stockForm()
            return redirect('portfolio-portfolio')
            args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class addstock(TemplateView):
    template_name = "portfolio/add_stock.html"

    def get(self, request):
        form = stockForm()
        stocks = Stock.objects.all().order_by('-stockCreated')
        args = {'form': form, 'stocks': stocks}
        return render(request, self.template_name, args)

    def post(self, request):
        form = stockForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['stock_ticker']
            form = stockForm()
            return redirect('portfolio-addstock')
            args = {'form': form, 'text': text}
        return render(request, self.template_name, args)



class addportfolio(TemplateView):
    template_name = "portfolio/create_portfolio.html"

    def get(self, request):
        form = portfolioForm()
        portfolios = Portfolio.objects.all().order_by('-stockCreated')
        args = {'form': form, 'portfolios': portfolios}
        return render(request, self.template_name, args)

    def post(self, request):
        form = portfolioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['portfolio_name']
            form = portfolioForm
            return redirect('portfolio-create-portfolio')
            args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
