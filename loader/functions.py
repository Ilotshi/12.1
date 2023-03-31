import json

def json_add(picture_path,content):
    """
    Функция записи данных поста в json файл
    """
    with open('C:\\Users\\popov\\OneDrive\\Рабочий стол\\python projects\\lesson12_project_source_v3\\posts.json',encoding='utf-8')as f:
        data = json.load(f)
        new_data = {'pic':picture_path,'content':content,}
        data.append(new_data)
        with open('C:\\Users\\popov\\OneDrive\\Рабочий стол\\python projects\\lesson12_project_source_v3\\posts.json','w',encoding='utf-8')as outfile:
            json.dump(data,outfile,ensure_ascii=False,indent=2)

