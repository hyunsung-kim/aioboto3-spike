import time
import asyncio

import aioboto3
import aiobotocore


async def main():
    async with aioboto3.resource("s3", verify=False) as s3:
        start_time = time.perf_counter()
        bucket = await s3.Bucket('superbai-test13')
        async for s3_object in bucket.objects.all():
            print(s3_object)
        end_time = time.perf_counter()
        print(f"Took: {end_time-start_time}")



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()