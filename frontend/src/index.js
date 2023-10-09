// import the sqlite3 module
const sqlite3 = require('sqlite3').verbose();
var express = require ('express');
var app = express ();

// open the database connection
let db = new sqlite3.Database('zelus.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the cricket database.');
});

// query data from the users table
let sql = `SELECT name, player_id, gender FROM player_universe LIMIT 10`;

app.set ('view engine', 'ejs');
app.set ('views', './public');

const router = express.Router();

router.get('/user-list', (req, res) => {
  db.query(sql, (err, data) => {
    if (err) throw err;
    res.render('user-list', { title: 'Players', playerData: data });
  });
});

module.exports = router;

app.get ('/', function (req, res) {
  db.all (sql, function (err, rows) {
    if (err) throw err;
    res.render ('page.js', {rows: rows});
  });
});

app.listen (3000, function () {
  console.log ('Server is listening on port 3000');
});
