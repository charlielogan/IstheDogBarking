from flask import Flask
import datetime
import random
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():

    today = datetime.date.today()
    date_seed = int(str(today.month) + str(today.day) + str(today.year))
    random.seed(date_seed)
    bark_likelihood = random.random()

    is_bark = np.random.uniform(0, 1) < bark_likelihood

    if is_bark:
        return('The Dog is Currently Barking')

    return "The Dog is Not Currently Barking"
    
if __name__ == "__main__":
    app.run(debug=True)