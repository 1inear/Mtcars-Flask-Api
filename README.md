# Mtcars-Flask-Api
model variable:

Outcome Variable: `mpg`

Predictors : `cyl` `disp` `hp` `drat` `wt` `qsec` `gear`

1. To run this API, change your directory to the docker folder and run:

  `docker-compose up`

If it has created the localhost server correctly you will not get your prompt back.

2. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

  `curl http://localhost:5000/`

This should return the following response "Server is up!"

3. To send a request to the API, use a curl command like the example below:
  
  `curl -H "Content-Type: application/json" -X POST -d '{"cyl":"4","disp":"150","hp":"235","drat":"4.2","wt":"2.5","qsec":"12","gear":"2"}' "http://localhost:5000/predict_mpg"`

 This should return the following response:
  `{
  "predict mpg": 16.107773931901843
  }`
  
  
 4. You can change some of the values to see the prediction change. To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through 

  `docker container kill <container-name>`
