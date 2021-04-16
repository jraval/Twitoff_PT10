"""Main app routing file for Twitoff"""

from flask import Flask, render_template, request
import json
from twitter import upsert_user
from twitoff.data_model import DB, User, Tweet
from twitoff.Users import user_list, tweet_list
from ml import predict_most_likely_author
from os import path

# from os import getenv
# from dotenv import load_dotenv
# from twitoff.heroku_user import get_user_and_tweets


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    # TODO - Make rest of application
    @app.route('/')
    def landing():
        if not path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
            # DB.drop_all()
            # DB.create_all()
            # DB.session.add_all(user_list)
            # DB.session.commit()
            # DB.session.add(app_user)
            # DB.session.commit()
            pass
        with open('landing.json') as f:
            args = json.load(f)
        return render_template('base.html', **args)

    @app.route('/user', methods=['GET'])
    def add_user():
        twitter_handle = request.args['twitter_handle']
        upsert_user(twitter_handle)
        return 'User added'

    @app.route('/products')
    def products():
        new_tweet = Tweet(id=3, text='tweet issues', user_id=4)
        DB.session.add(new_tweet)
        DB.session.commit()
        DB.session.add_all(tweet_list)
        DB.session.commit()
        return render_template('base.html', title="Products", body="This is the products page.")

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!', body="Reset database!")

    @app.route('/predict_author', methods=['GET'])
    def predict_author():
        tweet_to_classify = request.args['tweet_to_classify']
        return predict_most_likely_author(tweet_to_classify, ['cher', 'elonmusk', 'barackobama', 'johncena'])

    return app


if __name__ == "__main__":
    create_app().run(host='127.0.0.1', port=8000)
