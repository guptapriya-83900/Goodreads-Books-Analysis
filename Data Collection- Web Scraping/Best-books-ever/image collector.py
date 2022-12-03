#Image collection: To collect the book covers. 
#We have already collected the image URLs of the book covers, now all that is required is to simply download them. 
import wget
import os

book_data=pd.read_csv('best-books-ever_data.csv')
PATH="D:\Priya\Masters\Projects\Goodreads Books Analysis\Data Collection\Best-books-ever\images"
files=os.listdir(PATH)
n=0
if len(files)>0:
    n=max([int(f[:-4]) for f in os.listdir(PATH)])+1

for i in range(n, len(book_data)):
    url=book_data.at[i, 'image_url']
    filename=f'{i}.jpg'
    if not pd.isna(url):
        wget.download(url, PATH+filename)
    if i%100==0:
        print(i)