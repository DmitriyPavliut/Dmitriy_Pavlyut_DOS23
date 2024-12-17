from jinja2 import Template

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Список пользователей</title>
</head>
<body>
    <h1>Список пользователей</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.name }} - {{ user.email }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

users = [
    {"name": "Иван Иванов", "email": "ivan@example.com"},
    {"name": "Сидор Сидоров", "email": "sidor@example.com"},
    {"name": "Петр Петров", "email": "petr@example.com"}
]

template = Template(html_template)
rendered_html = template.render(users=users)

with open("template.html", "w", encoding="utf-8") as file:
    file.write(rendered_html)

print("HTML-шаблон был успешно создан и записан в файл template.html.")
