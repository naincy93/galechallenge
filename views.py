import random
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from models import ARTICLES
# Create your views here.


def handle_home(request):
    t = get_template('/home/milind/gale/templates/article_list.html')
    articles = []
    dbarticles = ARTICLES.objects.all()
    for article in dbarticles:
        articles.append({"id": article.id, "title": article.title, "author": article.author, "category": article.category,"hero": article.hero, "body": article.body, "pubdate": article.pubdate})
    # html = t.render(Context({"articles": articles}))
    random.shuffle(articles)
    html = t.render(Context({"articles": articles}))
    print html
    return HttpResponse(html)


def handle_detail(request, article_id):
    t = get_template('/home/milind/gale/templates/article_detail.html')
    articles = []
    dbarticles = ARTICLES.objects.all()
    for article in dbarticles:
        articles.append({"id": article.id, "title": article.title, "author": article.author, "category": article.category,"hero": article.hero, "body": article.body, "pubdate": article.pubdate})
    # html = t.render(Context({"articles": articles}))
    random.shuffle(articles)
    html = t.render(Context({"articles": articles, "article_id": int(article_id)}))
    print html
    return HttpResponse(html)
