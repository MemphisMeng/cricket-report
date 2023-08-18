# README

This ingestion processor is containerized by Docker.

**Prerequisite**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Execution

0. Get in this working directory
```
cd your/parent/path/to/zelus
# claim a variable for the absolute path of the current working directory
work_dir=your/parent/path/to/zelus
```

1. Build docker image:
```
docker build -t zelus .
```

2. Run docker image:
```
docker run --name cricket-database -v /$(pwd):$work_dir zelus --filename $work_dir/zelus.db
```

3. Expected result:
You are supposed to see a file named "zelus.db" created in the current working directory. To verify, please run `sqlite3 $work_dir/zelus.db` and you'll see a dialog waiting for you to type in.

*Note*:
1. you can pick the docker image name as you choose, for the demonstration reason, I selected "zelus";
2. "filename" argument in the docker image running command stands for the SQLite location of data schema, it's also also customizable while a text ending with any one of .sqlite, .sqlite3, .db, .db3, .s3db, .sl3, .sql is recommended.