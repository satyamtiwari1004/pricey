from django.shortcuts import render,HttpResponse,redirect
from crawler import views as crawlerView
from storage import views as storageView
def viewHomePage(request):
    return render(request,"home.html")

def extractProductUrl(request):
    URL=request.POST["product_url"]
    productDict=crawlerView.getProductDetails(URL)
    storageView.saveData(productDict)
    return redirect("/home/")

def fetchAllProducts(request):
    return storageView.fetchAllProducts()