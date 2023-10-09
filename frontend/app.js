// import the sqlite3 module
const sqlite3 = require('sqlite3').verbose();
var express = require ('express');
var app = express ();
app.set('view engine', 'ejs');
app.set('views', '.views');

// open the database connection
let db = new sqlite3.Database('./../zelus.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the cricket database.');
  });

app.get('/players', (req, res) => {
    // query data from the users table
    let sql = `SELECT name, player_id, gender FROM player_universe LIMIT 10`;
    db.all(sql, (err, rows) => {
      if (err) throw err;
    //   res.sendFile('/index.html');
      res.render('index', { rows: rows });
    });

    db.close((err) => {
      if (err) {
        console.error(err.message);
      }
    });
  });

app.get('/vis', (req, res) => {
  let sql = ``;
  db.all(sql, (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });

  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
  });
});

app.listen (3000, function () {
    console.log ('Server is listening on port 3000');
 });