apiVersion: apps/v1
kind: Deployment
metadata:
  name: maps-event-api
  namespace: dev-iot
spec:
  replicas: 1
  selector:
    matchLabels:
      run: maps-event-api
  template:
    metadata:
      labels:
        run: maps-event-api
    spec:        
      hostNetwork: true
      dnsPolicy: NopPolicy
      containers:
      - name: some parameter
        image: ashfiwehvii
        env:
        - name: some parameter
          value: "dev"
        - name: some parameter
          value: "ERROR"
        - name: some parameter
          value: "ERROR"
        - name: some parameter
          value: "ERROR"
        - name: some parameter
          value: "ERROR"          
        - name: some parameter
          value: "true"
