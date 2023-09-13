// import the sqlite3 module
const sqlite3 = require('sqlite3').verbose();
var express = require ('express');
var app = express ();

// query data from the users table
let sql = `SELECT name, player_id, gender FROM player_universe LIMIT 10`;

// open the database connection
let db = new sqlite3.Database('./../zelus.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the cricket database.');
  });

app.get('/players', (req, res) => {
    db.all(sql, (err, rows) => {
      if (err) throw err;
      res.sendFile('/index.html', { rows: rows });
    //   res.render('index.html');
    });
  });

app.listen (3000, function () {
    console.log ('Server is listening on port 3000');
 });