const express = require('express');
const app = express();
app.use(express.static(__dirname + '/static'));

app.get('/', (req, res) => {
  res.send({
    message: 'Hello World!'
  });
})

app.listen(5005, (err) => {
  if (!err) {
    console.log('Example app listening on port 5005!');
  } 
});