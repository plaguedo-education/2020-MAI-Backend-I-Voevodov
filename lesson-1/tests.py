from cache_utils import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')

def test_Jesse():
    assert cache.get('Jesse') == 'James'
    
def test_Walter(): 
    cache.rem('Walter')
    assert cache.get('Walter') == ''