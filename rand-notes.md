Step-by-Step Query in Datadog:
Uptime Calculation: Use Datadog's metric for node readiness or cluster status, depending on the level of granularity you need (e.g., node or cluster level).
Uptime Percentage for Nodes:
The following query will calculate the percentage of time that EKS nodes have been in the "Ready" state:

json
Copy code
100 * avg:kubernetes.node.ready{cluster-name:<your-cluster-name>} by {node}
This query gives you the uptime of each node as a percentage over time. kubernetes.node.ready metric has values of either 1 (node is ready) or 0 (node is not ready).

Uptime Percentage for Cluster:
If you want to calculate the uptime for the entire cluster, you can use:

json
Copy code
100 * avg:aws.eks.cluster.status{cluster-name:<your-cluster-name>} by {cluster}
This query returns the average cluster status over time. aws.eks.cluster.status metric typically reports 1 when the cluster is healthy (up) and 0 when the cluster is down.

Downtime Calculation: You can calculate downtime by subtracting the uptime percentage from 100.
Downtime Percentage for Nodes:
json
Copy code
100 - (100 * avg:kubernetes.node.ready{cluster-name:<your-cluster-name>} by {node})
This query calculates the downtime percentage for each node.

Downtime Percentage for Cluster:
json
Copy code
100 - (100 * avg:aws.eks.cluster.status{cluster-name:<your-cluster-name>} by {cluster})
This query calculates the downtime percentage for the entire EKS cluster.

Step 3: Visualization in Grafana
Once you enter the query into Grafana:

Use a gauge or single stat panel to display uptime and downtime percentages.
If you want to visualize uptime and downtime over time, choose a time series graph for a more granular view.
Example Queries:
Example Query for Node Uptime Percentage:
json
Copy code
100 * avg:kubernetes.node.ready{cluster-name:my-cluster} by {node}
Example Query for Cluster Downtime Percentage:
json
Copy code
100 - (100 * avg:aws.eks.cluster.status{cluster-name:my-cluster} by {cluster})
Setting Time Intervals:
You can set the time window (e.g., last 24 hours, 7 days) in Grafana to calculate uptime/downtime over a specific period.
These queries will help you track your EKS cluster and node uptime/downtime and visualize the percentage of time your cluster or nodes are operational (or not).




If the kubernetes.node.ready and aws.eks.cluster.status metrics are not available, you can still calculate EKS cluster uptime and downtime percentages through Grafana using alternative metrics from Datadog or other data sources. These metrics could be based on other components of the EKS cluster that contribute to the overall system health and availability. Here are several alternative methods you can consider:

Alternative Metrics for EKS Uptime and Downtime Calculation:
1. Kubernetes Pod Metrics (kubernetes.pod.ready)
This metric indicates the readiness of individual pods in your EKS cluster. If you monitor the number of pods that are in a ready state, you can infer the uptime and downtime of services running on the EKS cluster.

Uptime Percentage Query:
json
Copy code
100 * avg:kubernetes.pod.ready{cluster-name:<your-cluster-name>} by {pod}
This query calculates the percentage of time that pods are in a ready state across the cluster.

Downtime Percentage Query:
json
Copy code
100 - (100 * avg:kubernetes.pod.ready{cluster-name:<your-cluster-name>} by {pod})
This query calculates the downtime percentage based on the readiness of pods.

2. Node-Level Metrics (system.uptime)
If your EKS nodes report system-level metrics such as uptime (through Node Exporter or another system monitoring tool), you can use the system.uptime metric to calculate node uptime and downtime.

Uptime Percentage Query (for each node):
json
Copy code
avg:system.uptime{cluster-name:<your-cluster-name>} by {node}
This query monitors the uptime of individual nodes. If system.uptime reports a consistently high value, it indicates that the node has been up for a long time.

3. Datadog Agent Metrics (datadog.agent.running)
If Datadog agents are running on each node in the EKS cluster, the status of these agents can also be used to infer node health and by extension, cluster uptime/downtime.

Uptime Percentage Query:
json
Copy code
100 * avg:datadog.agent.running{cluster-name:<your-cluster-name>} by {node}
This query shows the percentage of time Datadog agents are running on each node. If an agent is running, the node is likely operational.

4. Kubernetes API Server Availability (kubernetes.apiserver.request.latency)
The Kubernetes API server is a critical component of the EKS cluster. If the API server is available and responding with low latency, the cluster is considered "up." You can track the latency of API requests to infer cluster uptime and downtime.

Uptime Percentage Query:
json
Copy code
100 - avg:kubernetes.apiserver.request.latency{cluster-name:<your-cluster-name>}
This query shows the uptime of the API server based on request latency. Lower latency indicates that the server is functioning normally, suggesting uptime.

5. EKS Control Plane Metrics from AWS CloudWatch
If you have set up CloudWatch metrics for your EKS cluster, you can use them in Grafana by configuring AWS CloudWatch as a data source. Some relevant metrics include:

EKSControlPlaneHealthy: Reflects the health of the EKS control plane components.
APIRequestCount: The number of successful API requests can indicate that the control plane is operational.
Uptime Percentage Query:
json
Copy code
100 * avg:aws.eks.cluster.api_request_count{cluster-name:<your-cluster-name>}
This query counts API requests. A healthy API server suggests cluster uptime.

6. Service-Level Metrics (Custom Metrics)
If you have custom application or service-level monitoring enabled for services running on EKS (via Prometheus, Datadog, or CloudWatch), you can use metrics that track the health or availability of critical services as a proxy for cluster uptime.

Uptime Percentage Query (Custom Metric):
json
Copy code
100 * avg:<your-service-metric>.availability{cluster-name:<your-cluster-name>}
This query calculates the availability of a key service or application, which can indirectly reflect cluster uptime.

Steps for Implementing in Grafana:
Identify alternative metrics: Determine which alternative metric best reflects the health of your EKS cluster (e.g., pod readiness, system uptime, API latency).
Write the query: Use the appropriate metric query to calculate uptime or downtime percentages.
Visualize in Grafana: Choose a gauge, single stat, or time series graph to display the uptime or downtime percentages.
General Queries for Uptime and Downtime Calculation:
Uptime Percentage:

Uptime Percentage
=
100
×
avg(metric)
Uptime Percentage=100×avg(metric)
Downtime Percentage:

Downtime Percentage
=
100
−
(
100
×
avg(metric)
)
Downtime Percentage=100−(100×avg(metric))
Conclusion:
If kubernetes.node.ready or aws.eks.cluster.status metrics are not available, you can still calculate uptime and downtime percentages for your EKS cluster using metrics like kubernetes.pod.ready, system.uptime, datadog.agent.running, API server latency, or even custom service metrics. By monitoring critical cluster components, you can approximate uptime and downtime effectively in Grafana.




To monitor and display EKS cluster/platform uptime and downtime in Grafana using Datadog as the data source, even with a load balancer in place, you can focus on a combination of Kubernetes, Datadog, and AWS load balancer metrics. Here’s how you can query Datadog for uptime and downtime in such a setup:

Step-by-Step Approach:
1. Node or Cluster Uptime using Kubernetes Metrics
Datadog collects Kubernetes metrics that help monitor the health of your EKS nodes and pods. These metrics can be used to determine whether nodes or clusters are "up" or "down."

a. Uptime based on Node Readiness:
The kubernetes.node.ready metric reports the readiness of each node in your EKS cluster. If the nodes are in a "Ready" state, the cluster is considered up.

Uptime Query:
json
Copy code
100 * avg:kubernetes.node.ready{cluster-name:<your-cluster-name>} by {node}
This query calculates the percentage of time each node is in a "Ready" state.

Downtime Query:
json
Copy code
100 - (100 * avg:kubernetes.node.ready{cluster-name:<your-cluster-name>} by {node})
This query calculates the percentage of downtime based on node readiness.

b. Cluster-Level Uptime with Pod Readiness:
If you don't have node-level metrics, you can track the readiness of the pods running on the cluster. Use the kubernetes.pod.ready metric for this.

Uptime Query:
json
Copy code
100 * avg:kubernetes.pod.ready{cluster-name:<your-cluster-name>} by {pod}
Downtime Query:
json
Copy code
100 - (100 * avg:kubernetes.pod.ready{cluster-name:<your-cluster-name>} by {pod})
This approach monitors the availability of pods across the cluster. If most pods are in a "Ready" state, the cluster is considered up.

2. AWS Load Balancer Health
If you have a load balancer in front of your EKS cluster, its health can be a strong indicator of overall platform uptime. AWS provides Application Load Balancer (ALB) and Network Load Balancer (NLB) metrics via Datadog.

a. ELB Target Health Metrics (aws.elb.target.healthy_host_count)
The aws.elb.target.healthy_host_count metric tracks the number of healthy targets (EKS nodes or pods) behind your load balancer.

Uptime Query:
json
Copy code
100 * avg:aws.elb.target.healthy_host_count{loadbalancer-name:<your-loadbalancer-name>}
This query shows the percentage of healthy targets behind the load balancer.

Downtime Query:
json
Copy code
100 - (100 * avg:aws.elb.target.healthy_host_count{loadbalancer-name:<your-loadbalancer-name>})
This query calculates the downtime percentage based on the number of healthy targets.

b. ALB/NLB Request Count (aws.elb.request_count)
If your EKS platform is processing traffic through a load balancer, the aws.elb.request_count metric can indicate activity. A sudden drop to 0 might signal downtime, and a healthy request count suggests uptime.

Uptime Query:
json
Copy code
100 * avg:aws.elb.request_count{loadbalancer-name:<your-loadbalancer-name>}
This query monitors the number of requests processed by the load balancer, indicating if it is actively serving traffic.

Downtime Query:
json
Copy code
100 - (100 * avg:aws.elb.request_count{loadbalancer-name:<your-loadbalancer-name>})
A sudden drop in request count could indicate downtime, especially during peak traffic hours.

3. Datadog Agent Metrics for Node-Level Monitoring
Datadog agents running on the EKS nodes can also be a good proxy for uptime/downtime. The datadog.agent.running metric shows whether the Datadog agent is running on each node.

Uptime Query:
json
Copy code
100 * avg:datadog.agent.running{cluster-name:<your-cluster-name>} by {node}
This query calculates the percentage of time Datadog agents are running on the nodes, which is a good indicator of whether the node itself is functioning.

Downtime Query:
json
Copy code
100 - (100 * avg:datadog.agent.running{cluster-name:<your-cluster-name>} by {node})
This query calculates downtime based on Datadog agent availability.

4. Kubernetes API Server Availability
The availability of the Kubernetes API server can indicate overall cluster health. If the API server is slow or down, the cluster may be experiencing downtime.

API Latency Metric (kubernetes.apiserver.request.latency):
If API requests are slow or failing, this could indicate downtime.

Uptime Query:
json
Copy code
100 - avg:kubernetes.apiserver.request.latency{cluster-name:<your-cluster-name>}
This query calculates the uptime based on API server latency. Lower latency means better cluster health.

5. Custom Service-Level Metrics
If you are monitoring specific services running on your EKS cluster (via Prometheus, Datadog, or CloudWatch), you can query service-specific metrics to calculate uptime and downtime.

Uptime Query (Example for a service):
json
Copy code
100 * avg:<your-service-metric>.availability{cluster-name:<your-cluster-name>}
This will track the availability of a particular service, indicating overall platform uptime from the service perspective.

Visualization in Grafana:
Single Stat Panel: Show uptime or downtime percentage as a single number.
Gauge Panel: Display uptime percentage in a gauge.
Time Series Graph: Visualize uptime and downtime over time to track trends.
Conclusion:
By combining Kubernetes metrics, load balancer health, Datadog agent metrics, and Kubernetes API server availability, you can calculate and visualize the uptime and downtime of your EKS cluster with or without a load balancer in place. These metrics can provide a comprehensive view of platform health, ensuring visibility across all layers of your cluster's infrastructure.
