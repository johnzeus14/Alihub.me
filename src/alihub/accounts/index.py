import algoliasearch_django as algoliasearch

from .models import User

algoliasearch.register(User)