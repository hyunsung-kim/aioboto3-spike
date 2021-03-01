import time

import boto3


def main():
    s3 = boto3.resource("s3")
    start_time = time.perf_counter()
    bucket = s3.Bucket('superbai-test13')
    for s3_object in bucket.objects.all():
        print(s3_object)
    end_time = time.perf_counter()
    print(f"Took: {end_time-start_time}")



if __name__ == "__main__":
    main()
