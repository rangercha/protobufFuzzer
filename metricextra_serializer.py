import metricextra_pb2

my_metric = metricextra_pb2.MetricReverse()
my_metric.name = 'sys.cpu'
my_metric.type = 'gauge'
my_metric.value = -12.5
my_metric.tags.extend(['my_tag', 'foo:bar'])
my_metric.herp = 300
with open('out.bin', 'wb') as f:
    f.write(my_metric.SerializeToString())

