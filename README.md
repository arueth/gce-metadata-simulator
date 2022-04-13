# Build image

```
docker build --tag gce-metadata-simulator:latest .
```

# Run image

```
docker run -it --rm \
--publish 8080:5000 \
gce-metadata-simulator:latest
```

# Test

```
curl localhost:8080/computeMetadata/v1/instance/attributes
```

```output
cluster-name
```

```
curl localhost:8080/computeMetadata/v1/instance/attributes/cluster-name
```

```output
default-cluster-name
```

# Deploy to Kubernetes

## Default Settings

```
kubectl --namespace simulators apply -f kubernetes-manifests
```

**--OR--**

```
kubectl --namespace simulators apply -k kustomize/base
```

## Custom Settings

```
kubectl --namespace simulators apply -k kustomize/overlays/config-from-configmap
```
