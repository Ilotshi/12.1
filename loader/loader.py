import logging

from flask import Blueprint, render_template, request
from loader.functions import json_add

ALLOWED_EXTENSIONS = {'png', 'jpg'}

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
loader = Blueprint('loader', __name__)


@loader.route('/post', methods=['GET', 'POST'])
def post():
    """
    Вьюшка для отображения и загрузки новых постов
    """
    if request.method == 'POST':
        picture = request.files.get('picture')
        if picture != None:
            extension = picture.filename.split(".")[-1]
            post_text = request.form.get('content')
            picture_path = f'./uploads/images/{picture.filename}'
            if extension in ALLOWED_EXTENSIONS:
                picture.save(picture_path)
                json_add(picture_path, post_text)
                return render_template('post_uploaded.html', path=picture_path, content=post_text)
            else:
                logging.info('Пользователь попытался загрузить файл с другим расширением')
                return f'Тип файлов {extension} не поддерживается'
        else:
            logging.error('Произошла ошибка при загрузке файла')
            return 'Произошла ошибка при загурзке картинки'
    else:
        return render_template('post_form.html')
