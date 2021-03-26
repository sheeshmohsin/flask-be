# Flask BE

## List Users

### Request method and URL

```
`GET` /api/v1/users
```
### Parameters (Filter and Pagination)

| Name    | Type  | In  | Description |
|:-------:|:-----:|:---:|:-----------:|
|user_type|integer|query|Type of user, input should be between 1-4|
|before   |integer|query|first and smallest id of current page for pagination|
|after    |integer|query|last and greatest id of current page for pagination|

## Setting up project using docker-compose

1. Clone the project first using below command.

    ```$ git clone https://github.com/sheeshmohsin/flask-be/```

2. Make sure docker and docker-compose is installed in your system, and run below commands next

    ```$ cd flask-be```
    
    ```$ docker-compose up```

3. And you'll see your server running right there, head over the url and follow above API documentation.

4. If you want to daemonize the server, run below command::

    ```$ docker-compose up -d```
    
