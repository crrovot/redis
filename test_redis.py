import redis.asyncio as redis

async def main():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    await redis_client.set('my_key', 'todo bien')
    value = await redis_client.get('my_key')
    print(value)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
