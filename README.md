## Scale
```bash
heroku ps:scale web=1
```

## CRUD
```bash
curl https://powerful-oasis-83494.herokuapp.com/todo1 -d "data=Remember the milk" -X PUT

curl https://powerful-oasis-83494.herokuapp.com/todo1
# >> {"todo1": "Remember the milk"}

$ curl https://powerful-oasis-83494.herokuapp.com/todo2 -d "data=Change my brakepads" -X PUT
# >> {"todo2": "Change my brakepads"}

$ curl https://powerful-oasis-83494.herokuapp.com/todo2
# >> {"todo2": "Change my brakepads"}

curl http://localhost:5000/seyoung-iphone -d "coordinates=33" -X PUT
# >> {"seyoung-iphone": "33"}

curl https://powerful-oasis-83494.herokuapp.com/

curl http://localhost:5000/seyoung-iphone

curl http://localhost:5000/seyoung-iphone -d "longitude=-75.19345" -d "latitude=40.023383" -X PUT

curl https://powerful-oasis-83494.herokuapp.com/seyoung-iphone -d "longitude=-75.19345" -d "latitude=40.023383" -X PUT
```

## Question
Hei guys, I'm working on client-server communication. The client is using Alamofire and the server is using Python Flask.

Flask has a restful api like `api.add_resource(VulcanServer, '/<string:detector_id>')` for a `PUT` request.

I can make a request on bash like:
```
>>> curl http://localhost:5000/seyoung-iphone -d "longitude=-75.19345" -d "latitude=40.023383" -X PUT

## Run a GET request
>>> curl http://localhost:5000/seyoung-iphone
{"seyoung-iphone": {"latitude": "40.023383", "longitude": "-75.19345"}}
```

Now I'm trying to
