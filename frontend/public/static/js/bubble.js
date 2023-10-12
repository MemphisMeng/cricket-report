import * as d3 from "d3";
const fs = require('fs')
const sqlite3 = require('sqlite3').verbose();

// open the database connection
let db = new sqlite3.Database('./../zelus.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the cricket database.');
  });

async function drawChart() {
    const sql = fs.readFileSync('../queries/games_per_team.sql').toString()
    const teams  = await db.all(sql);
    const data = teams.map((d) => (
        {
            ...d,
            team: d.team,
            games: d.games
        }
    ))
    .filter(d => d.team)
    .sort((a, b) => d3.descending(a.games, b.games));

    // construct the radius scale
    const radius = d3.scaleSqrt([0, d3.max(data, d => d.population)], [0, 40]);
    
    // construct the path generator
    const path = d3.geoPath();

    // Select the SVG container. Its dimensions correspond to the bounding-box
    const svg = d3.select("svg")
        .attr("width", 975)
        .attr("height", 610)
        .attr("viewBox", [0, 0, 975, 610])
        .attr("style", "width: 100%; height: auto; height: intrinsic;");

    // Create the cartographic background layers.
    svg.append("path")
        .datum(topojson.feature(world, world.objects.land))
        .attr("fill", "#ddd")
        .attr("d", path);

    svg.append("path")
        .datum(topojson.mesh(world, world.objects.countries, (a, b) => a !== b))
        .attr("fill", "none")
        .attr("stroke", "white")
        .attr("stroke-linejoin", "round")
        .attr("d", path);

    // Create the legend.
    const legend = svg.append("g")
        .attr("fill", "#777")
        .attr("transform", "translate(915,608)")
        .attr("text-anchor", "middle")
        .style("font", "10px sans-serif")
        .selectAll()
        .data(radius.ticks(4).slice(1))
        .join("g");

    legend.append("circle")
        .attr("fill", "none")
        .attr("stroke", "#ccc")
        .attr("cy", d => -radius(d))
        .attr("r", radius);

    legend.append("text")
        .attr("y", d => -2 * radius(d))
        .attr("dy", "1.3em")
        .text(radius.tickFormat(4, "s"));

    // Add a circle for each county, with a title (tooltip).
    const format = d3.format(",.0f");
    svg.append("g")
        .attr("fill", "brown")
        .attr("fill-opacity", 0.5)
        .attr("stroke", "#fff")
        .attr("stroke-width", 0.5)
        .selectAll()
        .data(data)
        .join("circle")
        .attr("transform", d => `translate(${centroid(d.team)})`)
        .attr("r", d => radius(d.games))
        .append("title")
        .text(d => `${d.team.properties.name}: ${format(d.games)}`);

}
drawChart();