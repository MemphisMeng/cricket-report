WITH teams AS (
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
GROUP BY 1;