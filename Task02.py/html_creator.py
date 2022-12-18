from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    style = 'style="font-size:22px;"' # описываем стиль, 22 шрифт
    html = '<html>\n <head></head>\n <body>\n' # загатовка для html представления
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device)) # обычная строка вывода
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </body>\n</html>'

    with open('index.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return html

def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"' # описываем стиль, 22 шрифт
    html = '<html>\n <head></head>\n <body>\n' # загатовка для html представления
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t) # обычная строка вывода
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   </body>\n</html>'

    with open('new_index.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return data