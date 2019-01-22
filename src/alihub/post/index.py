import algoliasearch_django as algoliasearch

from .models import Post

algoliasearch.register(Post)