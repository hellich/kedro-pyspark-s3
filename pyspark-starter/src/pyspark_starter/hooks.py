from kedro.framework.hooks import hook_impl
from pyspark import SparkConf
from pyspark.sql import SparkSession


class SparkHooks:
    @hook_impl
    def after_context_created(self, context) -> None:
        """Initialises a SparkSession using the config
        defined in project's conf folder.
        """

        # Load the spark configuration in spark.yaml using the config loader
        parameters = context.config_loader["spark"]
        spark_conf = SparkConf().setAll(parameters.items())

        # Initialise the spark session
        spark_session_conf = (
            SparkSession.builder.appName(context.project_path.name)
            .enableHiveSupport()
            .config(conf=spark_conf)
        )
        _spark_session = spark_session_conf.getOrCreate()
        _spark_session.sparkContext.setLogLevel("WARN")

        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "ROOTNAME")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "CHANGEME123")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://127.0.0.1:9000")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        _spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
