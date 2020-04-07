from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import stockForm, \
    portfolioForm, \
    AdvancedAnalysisForm, \
    graphAnalysisForm
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


# class compareStock(View):
#     form = AdvancedAnalysisForm
#
#     def get:(self, request, *args, **kwargs):


def filterstocks(stocks):
    functionStock = stocks['stock_names']
    print(functionStock)
    functionStock = functionStock.replace(" ", "',")
    return functionStock


#  my_stocks = stocks['stock_names'][0].split()   # this gives a list, my_stocks with two text elements, ANF and AIB
# for stock in my_stocks:
#     do_something(stock)    # where do_something is any function or code suite

def comparestock(request):
    form = AdvancedAnalysisForm()

    stocks = request.GET
    if bool(stocks):
        print("you have stocks")
        listofstocks = filterstocks(stocks)
        print(listofstocks)
        args = {
            'form': form,
            'stocks': Stock.objects.filter(stock_ticker__in=['AIB', 'KO']),
            'portfolio': Portfolio.objects.all()[0]
        }

        return render(request, 'portfolio/compare_stocks.html', args)

    else:
        args = {
            'form': form,
            'portfolio': Portfolio.objects.all()[0]
        }

        return render(request, 'portfolio/compare_stocks.html', args)


def stock_options(request):
    stock_list = {
        'stocks': Portfolio.objects.all()
    }
    return render(request, 'portfolio/view_stock_options.html', stock_list)


def view_individual_stock_data(request):
    form = graphAnalysisForm
    stock = request.GET
    if bool(stock):
        print("you have stocks")
        print(stock['stock_name'])
        args = {
            'form': form,
            'stocks': Stock.objects.all(),
            'portfolio': Portfolio.objects.all()[0]
        }

        return render(request, 'portfolio/view_individual_stock_data.html', args)

    else:
        args = {
            'form': form,
            'portfolio': Portfolio.objects.all().last()
        }

        return render(request, 'portfolio/view_individual_stock_data.html', args)


def create_portfolio(request):
    # stock_list = {
    #     'stocks': Portfolio.objects.all()
    # }
    return render(request, 'portfolio/create_portfolio.html')


def advanced_analysis(request):
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
