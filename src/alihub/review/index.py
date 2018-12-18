import algoliasearch_django as algoliasearch

from .models import Review

algoliasearch.register(Review)