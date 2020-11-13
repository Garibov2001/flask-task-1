from flask import *

data = [
    {
        'id': 1,
        'title':'How to Start programming',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '13.11.2020'
    },
    {
        'id': 2,
        'title':'How to to learn Java',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '07.01.2020'
    },
    {
        'id': 3,
        'title':'List, Tuples, Dictionary',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '05.12.2019'
    },
    {
        'id': 4,
        'title':'Listen To good music',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '05.06.2018'
    },
    {
        'id': 5,
        'title':'How to read Kuran',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '13.11.2020'
    },
    {
        'id': 6,
        'title':'How to begin Namaz',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '13.11.2020'
    },
    {
        'id': 7,
        'title':'Azan times',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '13.11.2020'
    },
    {
        'id': 8,
        'title':'Qarabagh captured by Azeri forces.',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '09.11.2020'
    },
    {
        'id': 9,
        'title':'Armenia losed',
        'content':'when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'date': '09.11.2020'
    },
]



app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = data)


@app.route('/news/<int:id>')
def news(id):
    for eachNews in data:
        if(eachNews['id'] == id):
            return render_template('news.html', news = eachNews)
    return render_template('home.html', posts = data)








if __name__ == '__main__':
    app.run(debug=True)