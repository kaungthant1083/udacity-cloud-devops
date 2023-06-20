# udacity-cloud-devops
We are deploying High Available Web applicaiton 

Website endpoint : udaci-WebAp-1GKPZNI8FJSRJ-1755838113.us-east-1.elb.amazonaws.com 

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
