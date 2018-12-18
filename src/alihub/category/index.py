import algoliasearch_django as algoliasearch

from .models import Category

algoliasearch.register(Category)