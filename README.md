# 🦉 Welcome to the Bounty Board Oracle - Venom!

In order to conjure up the Oracle magic, here's your trusty guide!

## 🛠️ Prerequisites:

Ensure you have the following:

- Docker compose ⛵
- yarn 🪄

## 🚀 Getting Started:

1. To wake up the Oracle, simply run:
    shell
    sudo ./initoracle.sh
   ![Alt text](https://i.postimg.cc/9fYWjxY9/oracle.png)


2. To let the Oracle rest, use:
    shell
    ./stoporacle.sh
    

## 🔮 Interacting with the Oracle:

### - Initiating the Oracle:

Send this request to get the Oracle started:

```shell
curl -X POST -H "access_token: 3e9bd24a88d140c29926d8c96453a39b" -H "Content-Type: application/json" -d '{
  "user_id": "your_user_id",
  "url_input": "https://example.com",
  "task_index": 1
}' http://localhost:8000/start

```
## 🔮 Querying the Oracle's task status:

Use the following request to inquire about the status of your bounty:

```shell
curl -X GET -H "access_token: 3e9bd24a88d140c29926d8c96453a39b" -G http://localhost:8000/status --data-urlencode "user_id=your_user_id" --data-urlencode "url_input=https://example.com"
```
## 🎁 Upon Completion:

Once the issue is resolved, the Oracle will change the status of the bounty to 'closed', enabling the payment to be liberated. ✨
