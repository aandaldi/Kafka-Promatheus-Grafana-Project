# Setup Kafka Stream and Monitoring with Promatheus and Grafana

## contain :
<h4> 
    1. Python (Producer and Consumer) </br>
    2. Kafka (Multiple Node) </br>
    3. Provectuslabs (kafka UI) </br>
    4. Promatheus </br>
    5. Grafana
</h1>

<p>
1. Run Docker compose </br>
2. activate virtual env: ~ python3 . venv/bin/activate ~ </br>
3. run python producer and consumer file in virtual environtment </br>
4. Create Grafana Dashboard use template [kafka overview](https://grafana.com/grafana/dashboards/721-kafka/). Then, setup dashboard

</p>

ref:
- https://jaceklaskowski.gitbooks.io/apache-kafka/content/kafka-server-BrokerTopicMetrics.html
- https://dzone.com/articles/kafka-monitoring-via-prometheus-amp-grafana
- [grafana labs](https://grafana.com/)
- https://www.slingacademy.com/article/ways-to-monitor-kafka-cluster-health/
- https://betterdatascience.com/apache-kafka-in-python-how-to-stream-data-with-producers-and-consumers/
- https://github.com/provectus/kafka-ui