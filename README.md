# Goodreads-Books-Analysis
A data science project to scrape Goodreads data and run a classifier to categorize books as fiction or nonfiction based on the description.

### Data Collection:
The Goodreads books data are used as the source of my dataset, as the amount of information they had on their book pages was very comprehensive and in a mostly standard format. I decided to ‘scrape’ the following pieces of information:

**Title**

**Description**

**Authors**

**Edition**

**Format**

**ISBN**

**No. of pages**

**Rating**

**No. of ratings**

**No. of reviews**

**Genres**

**Book cover image**

One of the most popular and easy-to-use packages in Python to collect static data from web pages is BeautifulSoup, which is used in this. 
The training data was collected from Goodreads' best books ever list found here: https://www.goodreads.com/list/show/1.Best_Books_Ever.
The test data used to validate the model was collected from the list of best books of 2018, found here: https://www.goodreads.com/list/best_of_year/2018?id=119307.Best_books_of_2018

Scripts used to scrape data from Goodreads. They should be run in this order:

1. URL collector

2. Data collector

3. Image collector

In case if you don't want to do web scraping for data and want data directly for your model. Then you can download data from kaggle:

Best-books-ever: https://www.kaggle.com/datasets/meetnaren/goodreads-best-books?select=book_data.csv

Best-books-of-2018: https://www.kaggle.com/datasets/meetnaren/goodreads-best-books-of-2018?select=book_data.csv

### Data Exploration:

Data Exploration of books genres, covers, authors etc is performed for better understanding of the data and understanding the trends in data which can help us in classification.


### Models:

Two Recurrent neural network classifiers are used, one is Keras RNN classifier which gives accuracy of around 94% and the other is Pytorch RNN classifier which gives accuracy of around 95%. Both the models are good, but Pytorch RNN classifier is slightly better than Keras RNN classifier.

### Book Recommender System:
A simple content based Book recommender system based on author names and genres.

