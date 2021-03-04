# check stock price
from uncleengineer import thaistock
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

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
def chekproduct(index:int = 0,name: Optional[str] = 'Test name'):
    return [products[index],name]



@app.get('/stock/{stock_name}/')
def stock(stock_name:str):
    price = thaistock(stock_name)
    return price

@app.get('/mystock/')
def mystock(stock_name:str = 'AOT'):
    price = thaistock(stock_name)
    return price

###############POST METHOD############################
class Fruit(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
fruit_stock=[]

@app.post('/addfruit/')
def Addfruit(fruit:Fruit):
    fruit_stock.append(fruit.dict())
    print(fruit_stock)
    return fruit

@app.get('/fruit/')
def Allfruit():
    return fruit_stock

@app.put('/update/{ID}')
def UpdateFruit(ID : int, fruit : Fruit):
    fruit_stock[ID] = fruit.dict()
    return {'ID':ID,'message':'update','data':fruit.dict()}


@app.delete('/delete/{ID}')
def UpdateFruit(ID : int):
    data = fruit_stock[ID]
    del fruit_stock[ID]
    return {'ID':ID,'message':'delete','data':data}