from flask import render_template, request, redirect# type:ignore
from config import db
from models.article import Article

def index():
    articles = Article.query.all()
    return render_template('index.html', title="Home Page", articles=articles)

def add_post():
    return render_template('add-post.html', title="Add Post")


def create():
    form = request.form
    title = form['title']
    author = form['author']
    description = form['description']

    article = Article(title=title, author=author, description=description)
    db.session.add(article)
    db.session.commit()

    return redirect('/')


def view(id):
    articles = Article.query.get(id)
    return render_template('view.html', title="View Page", articles=articles)


def delete(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            articles = Article.query.get(id)
            db.session.delete(articles)
            db.session.commit()
            return redirect('/')
    

def update(id):
    article = Article.query.filter_by(id = id).first()
    if article is None:
        return redirect('/')
    if request.method == "GET":
        return  render_template('update.html', title="Update Page", article=article)
    elif request.method == "POST":
        form = request.form
        title = form['title']
        author = form['author']
        description = form['description']
        article.title = title
        article.author = author
        article.description = description
        db.session.commit()
        return redirect('/')
    return render_template('update.html', title="Update Page", article=article)
