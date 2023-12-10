import pandas as pd

customer=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9],
    'name':['Olivia','Donald','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],
    'age':[20,25,15,10,30,65,35,18,23],
    'Product_ID':[101,0,106,0,103,104,0,0,107],
    'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],
'   City':['Swindon','London','Oxford','Reading','Swindon','Faringdon','Swindon','Faringdon','Manchester']
    })

product=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106,107],
    'Product_name':['watch','bag','shoes','smartphone','books','oil','laptop'],
    'Category':[ 'fashion','fashion','fashion' ,'electronics','stationery','food','electronics'],
    'Price':[14,25,32,400,14,4,450],
    'Seller_City':['London','Swindon','Reading','Swindon','London','Reading','London']
})
# Convert the dictionary into DataFrame
df = pd.DataFrame(customer)

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(product)

print(df1)
print(df)
#res = pd.merge(df1, df, on='Product_ID')
res = pd.merge(customer, product, on='Product_ID')
res

#full join, all products that are not sold and all the customers who didn’t purchase anything from us
res2 = pd.merge(product,customer,on='Product_ID',how='outer',indicator=True)
res2

#left join, only customers who bought from us
res3= pd.merge(product,customer,on='Product_ID',how='left')
res3

#inner join
res4 = pd.merge(product,customer,how='inner',on='Product_ID')
res4
