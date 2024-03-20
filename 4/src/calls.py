import helpers
import time 

def intervalTest():
   while 1:
    metrics()
    time.sleep(3600)

def metrics():
  metrics = helpers.buildReport()
  helpers.sendMetrics(metrics)
  return "metrics invoked"