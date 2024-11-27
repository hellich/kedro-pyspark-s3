# setup minio

```
mkdir -p ~/minio/data

docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=ROOTNAME" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   quay.io/minio/minio server /data --console-address ":9001"
```

Download URL for mc client : https://dl.min.io/client/mc/release/windows-amd64/mc.exe
```
mc.exe alias set local http://127.0.0.1:9000 ROOTNAME CHANGEME123
mc.exe admin info local

mc head -n 5 local/mydata/companies.csv
```

# setup kedro project

```
micromamba.exe create -n venv39  python=3.9 -c conda-forge -y

micromamba activate venv39

pip install pyspark

pip install s3fs
```