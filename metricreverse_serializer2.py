import metricreverse_pb2

my_metric = metricreverse_pb2.MetricReverse()
my_metric.value = 99.9
my_metric.tags.extend(['my_tag', 'foo:bar'])
my_metric.name = 'sys.cpu'
my_metric.type = 'gauge'



with open('out.bin', 'wb') as f:
    f.write(my_metric.SerializeToString())

