// import the sqlite3 module
const sqlite3 = require('sqlite3').verbose();
var express = require ('express');
var app = express ();
app.use(express.static('public'));
// app.engine('ejs', engine());
app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/vis', (req, res) => {
  res.render('vis');
});

app.listen (3000, function () {
    console.log ('Server is listening on port 3000');
 });