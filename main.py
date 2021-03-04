# check stock price
from uncleengineer import thaistock
from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
def HomePage():
    return {"message": "Hello World"}

products= [{'id':101,'name':'แปรงสีฟัน','price':20},
        {'id':102,'name':'ยาสีฟัน','price':30},
        {'id':103,'name':'ยาสระผม','price':50}

]
@app.get('/product/')
def Allproduct():
    return products

@app.get('/product/{index}/')
def chekproduct(index:int=0,name: Optional[str] = 'Test name'):
    return products[index]



@app.get('/stock/{stock_name}/')
def stock(stock_name:str):
    price = thaistock(stock_name)
    return price

@app.get('/mystock/')
def mystock(stock_name:str = 'AOT'):
    price = thaistock(stock_name)
    return price





