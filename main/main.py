import logging
from flask import Blueprint, render_template, request
from main.functions import search_in_posts

logging.basicConfig(level=logging.INFO)
main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/search')
def search():
    """
    Вьюшка для страницы поиска
    """
    s = request.args.get('s')
    valid_posts = search_in_posts(s)
    logging.info(f'Пользователь осуществил поиск по строке - {s}')
    if len(valid_posts) >= 1:
        return render_template('post_list.html', posts=valid_posts)
    else:
        return 'К сожалению таких постов нет'
