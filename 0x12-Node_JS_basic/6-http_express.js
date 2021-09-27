// create express version of a simple http server
const express = require('express');
const app = express();

app.get('/', (request, response) => {
  request.send('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
