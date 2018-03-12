## Instructions

请安装airflow和所需的dependency:
```
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow
```

在此项目根目录下`maven clean install` 可以看到build到的jar包`target/tisparkexample-1.0-SNAPSHOT-jar-with-dependencies.jar`

在`resources/tisparkdag-example.py`按实际情况修改包括jar包路径在内的属性，并复制到`$AIRFLOW_HOME/dags`，airflow将从这个目录获取DagOperator信息

schedule设置的方式很多，也比较简单，可以仔细阅读[官方文档](https://airflow.apache.org/scheduler.html#)


run
```
# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080
```

此项目仅为示例，可以按自己业务需求来写特定的tispark job