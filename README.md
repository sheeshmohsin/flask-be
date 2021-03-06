# Flask BE

![GitHub issues](https://img.shields.io/github/issues/sheeshmohsin/flask-be)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3)
![GitHub Repo stars](https://img.shields.io/github/stars/sheeshmohsin/flask-be?style=social)

User List API with pagination and filter support. Not just a regular API, wondering why? All data are fetched with uniform time complexity and lowest possible query cost. (Tested with **1M** rows)

## For Live Demo, Click [here](http://40.78.149.220:5000/api/v1/users)

## List Users (Documentation)

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

    ```bash
    $ git clone https://github.com/sheeshmohsin/flask-be/
    ```

2. Make sure docker and docker-compose is installed in your system, and run below commands next

    ```bash
    $ cd flask-be
    ```
    
    ```bash
    $ docker-compose up
    ```

3. And you'll see your server running right there, head over the url and follow above API documentation.

4. If you want to daemonize the server, run below command::

    ```bash
    $ docker-compose up -d
    ```
    
