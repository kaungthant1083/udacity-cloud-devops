# udacity-cloud-devops
We are deploying High Available Web applicaiton as per the following Architecture Diagram. 
[https://github.com/kaungthant1083/udacity-cloud-devops/blob/main/project2/udacity-high-availability-architecture.png](url)

**Create VPC Environment for our Web Application**

```

cd project2
./create.sh stack_name network.yml network-parameters.json aws_profile_name 

```

**Updating Network Stack**
```

cd projectr2
./update.sh stack_name network.yml network-parameters.json aws_profile_name

```
**Deploy our Web-Applicaiton Stack**

```

cd project2
./create.sh stack_name server.yml server-parameters.json aws_profile_name 

```

**Updating Web Stack**
```

cd projectr2
./update.sh stack_name server.yml server-parameters.json aws_profile_name

```
