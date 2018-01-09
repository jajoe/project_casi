const express = require('express')
const fs = require('fs');
var bodyParser = require('body-parser');
var path = require("path");


const app = express();
const pathFile = "/tmp/casi/"

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));


app.use(function(req, res, next) {  
  res.header('Access-Control-Allow-Origin', req.headers.origin);
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// to test : curl -H "Conte-Type: application/json" -X POST -d '{"idProxy":"xxxBOBxxx","result":"2"}' http://localhost:4242/answer

app.post('/answer', function (req, res) {
  if (req.body){
    if (req.body.idProxy && req.body.result) {
      fs.writeFile(pathFile + req.body.idProxy + ".txt", req.body.result, function(err) {
        if(err) {
          res.status(400).send("Error while writing in the file : "+err);
        } else {
          res.send('OK');
        }
      });
    } else {
      res.status(400).send("Field idProxy or/and result missing");
    }
  } else {
    res.status(400).send('Problem with the body of your request : there is no body');
  }
})

app.listen(4242, function () {
  console.log('app listening on port 4242!')
})


