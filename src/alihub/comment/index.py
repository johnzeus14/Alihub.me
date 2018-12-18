import algoliasearch_django as algoliasearch

from .models import Comment

algoliasearch.register(Comment)