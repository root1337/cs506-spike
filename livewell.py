from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Vinay Janardhanam',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'September 28, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'September 29, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')



if __name__ =='__main__':
    app.run(debug=True)
