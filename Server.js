var app = require('express')();
var http = require('http').createServer(app);
var express = require('express');
const fs = require('fs');
app.use(express.urlencoded({ extended: true }))
app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/APImap.html');
});


app.post('/sendData', async function(req, res) {
  console.log(req.body);
  fs.writeFileSync(__dirname + '/storage.JSON', JSON.stringify(req.body));
})



http.listen(3000, () => {
  console.log('listening on *:3000');
});
