from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

#setup the flask session

app = Flask(__name__)

#Use flask mongo to setup mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

#Define the routes for the html pages

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    print('starting scrape')
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    print('ending scrape')
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

#telling the flask object to run when called 
if __name__ == '__main__':
    app.run()