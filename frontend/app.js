// import the sqlite3 module
const sqlite3 = require('sqlite3').verbose();
var express = require ('express');
var app = express ();
app.use(express.static('public'));
// app.engine('ejs', engine());
app.set('view engine', 'ejs');
app.set('views', './views');

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
  });

app.get('/vis', (req, res) => {
  // games played per country
  let sql = `WITH teams AS (
      SELECT 
      json_extract(teams, '$[0]') AS team1, 
      json_extract(teams, '$[1]') AS team2
      FROM match_results),
      games AS(
        SELECT team1 AS team, COUNT(*) AS games
        FROM teams
        GROUP BY 1
        UNION ALL
        SELECT team2 AS team, COUNT(*) AS games
        FROM teams
        GROUP BY 1)
      SELECT team, SUM(games) AS games
      FROM games
      GROUP BY 1`;
  db.all(sql, (err, rows) => {
    if (err) {
      throw err;
    }
    res.json(rows);
  });
});

app.listen (3000, function () {
    console.log ('Server is listening on port 3000');
 });