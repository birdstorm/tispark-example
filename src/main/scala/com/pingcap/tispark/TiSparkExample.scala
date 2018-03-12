package com.pingcap.tispark

import com.typesafe.scalalogging.slf4j.LazyLogging
import org.apache.spark.sql.{SparkSession, TiContext}

class Job extends LazyLogging {

  private val spark =
    SparkSession
      .builder()
      .appName("tispark-example")
      .getOrCreate()

  private val ti = new TiContext(spark)

  def work(): Unit = {
    ti.tidbMapDatabase("tispark_test")

    val q = spark.sql("select count(*) from full_data_type_table")

    logger.info(q.schema.toString)
    logger.info(q.show.toString)
  }
}

object TiSparkExample {

  def main(args: Array[String]): Unit = {

    val job = new Job()

    job.work()
  }

}