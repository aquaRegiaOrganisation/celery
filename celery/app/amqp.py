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
      - name: temp-name
        image: imgname
        env:
        - name: SPRING_PROFILE
          value: "dev"
        - name: logging.level.root
          value: "ERROR"
        - name: logging.level.org.springframework
          value: "ERROR"
        - name: logging.level.com.blumeglobal
          value: "ERROR"
        - name: logging.level.org.apache.kafka
          value: "ERROR"          
        - name: LOG4J_FORMAT_MSG_NO_LOOKUPS
          value: "true"
