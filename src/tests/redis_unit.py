import pickle
import redis

# Get the pickled object
r = redis.Redis(host='localhost', port=6379, db=0)
pickled_object = r.get('response:76aff6ae-17b2-419a-95ce-5087618fe7a1')

# Unpickle the object
unpickled_object = pickle.loads(pickled_object)

print(unpickled_object)
