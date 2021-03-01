# aioboto3-spike


## Benchmark

| Package | Easy to Use | Speed | Error-Handling |
|---|---|---|---|
| Boto3 | :star: :star: :star: | Speed | Error-Handling |



## Issues
- [CERTIFICATION ERROR](https://github.com/aio-libs/aiobotocore/issues/548)
```python
async with aioboto3.resource("s3", verify=False) as s3:
        bucket = await s3.Bucket('superbai-test13')
        async for s3_object in bucket.objects.all():
            print(s3_object)
```


## Reference
- [aioboto3](https://pypi.org/project/aioboto3/)
- [aioboto3 doc](https://aioboto3.readthedocs.io/en/latest/)