import redis
import random

def adjust_keys_in_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    keys = list(r.keys('*'))
    while len(keys) > 1000:
        r.delete(random.choice(keys))
        keys = list(r.keys('*'))

def main():
    adjust_keys_in_redis()
    print("Redis cache adjusted to 1000 keys.")

if __name__ == "__main__":
    main()
