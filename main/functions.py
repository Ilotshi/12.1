import json

def search_in_posts(key_word):
    """
    Функция поиска постов по строке в описании
    """
    with open('C:\\Users\\popov\\OneDrive\\Рабочий стол\\python projects\\lesson12_project_source_v3\\posts.json',
              encoding='utf-8') as f:
        file = json.load(f)
        valid_posts = []

        for post in file:
            if key_word.lower() in post['content'].lower():
                valid_posts.append(post)
        return valid_posts
