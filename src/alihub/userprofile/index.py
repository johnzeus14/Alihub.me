import algoliasearch_django as algoliasearch

from .models import Profile

algoliasearch.register(Profile)