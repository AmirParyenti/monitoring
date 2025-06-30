# Prometheus & Grafana:

## Commands to activate:
```bash
kubectl create namespace monitoring
```

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

```bash
kubectl create namespace monitoring
```

```bash
helm install kube-prometheus prometheus-community/kube-prometheus-stack \
--namespace monitoring \
--set grafana.adminPassword='admin123' \
cancel nodeExporter too
```


## Expose all the services by using Port-Forward:
- Prometheus
```bash
kubectl port-forward -n monitoring svc/kube-prometheus-kube-prome-prometheus 9090:9090
```

- Grafana
```bash
kubectl port-forward -n monitoring svc/kube-prometheus-grafana 3000:80
```

- Alert Manager
```bash
kubectl port-forward -n monitoring svc/kube-prometheus-kube-prome-alertmanager 9093:9093
```

- Metrics
```bash
kubectl port-forward -n monitoring svc/kube-prometheus-kube-state-metrics 8080:8080
```

## CPU Usage:

```bash
100 *
sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by(pod)
/
sum(kube_pod_container_resource_limits{resource="cpu", unit="core", namespace="default"}) by(pod)
```

## RAM Usage:

```bash
100 *
sum by(pod) (container_memory_usage_bytes{namespace="default"})
/
sum by(pod) (kube_pod_container_resource_limits{resource="memory", unit="byte", namespace="default"})
```
