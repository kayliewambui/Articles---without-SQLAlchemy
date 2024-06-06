import ipdb
class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception
        self._magazine = magazine
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, '_name'):
            self._name = name
        else:
            raise AttributeError("Name must be a string and is immutable")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        
    def topic_areas(self):
        topic_area = list({article.magazine.category for article in self.articles()})
        return topic_area if topic_area else None
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name =  name
        else:
            raise Exception("Name has to be a string")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category =  category
        else:
            raise Exception("CCategory has to be a string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})
    
    def article_titles(self):
        article_title = list({article.title for article in Article.all if article.magazine == self})
        return article_title if article_title else None

    def contributing_authors(self):
        all_authors = list(article.author for article in Article.all if article.magazine == self)
        contrib_author = list(cont_author for cont_author in all_authors if all_authors.count(cont_author) >= 2)
        return contrib_author if contrib_author else None
