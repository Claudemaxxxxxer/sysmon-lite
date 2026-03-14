# sysmon-lite

Tiny system monitor. Prints CPU / memory / disk usage and can push a
snapshot to a webhook.

```
pip install .
sysmon            # print a snapshot
sysmon --watch 5  # refresh every 5 seconds
```
