import L from 'leaflet';
import '../../scss/app.scss';

// consts.
const LNG = 0;
const LAT = 1;
const DATETIME = 2;
const DEPTH = 3;
const AREA = 4;
const MAGNITUDE = 5;

const seismList = document.getElementById('seismList');
const data = JSON.parse(seismList.value)['data'];

const geoData = document.getElementById('geoData');
const features = JSON.parse(geoData.value)['features'];

// init.
const center = [36.2048, 138.2529];
const zoom = 8;
const map = L.map('map').setView(center, zoom);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution:
    '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
  maxZoom: 12,
  minZoom: zoom,
}).addTo(map);

// marker.
const icon = L.icon({
  iconUrl: 'static/images/pin.svg',
  iconSize: [20, 20],
  iconAnchor: [22, 94],
  popupAnchor: [-3, -76],
});
for (let i = 0; i < data.length; i++) {
  const d = data[i];
  const pos = [d[LAT], d[LNG]];
  const popup = `<p>datetime: ${d[DATETIME]}</p>
    <p>area: ${d[AREA]}</p>
    <p>depth: ${d[DEPTH]}</p>
    <p>magnitude: ${d[MAGNITUDE]}</p>`;
  L.marker(pos, { icon: icon })
    .addTo(map)
    .bindPopup(popup);
}

// polygon.
for (let i = 0; i < features.length; i++) {
  const p = [];
  for (let j = 0; j < features[i].geometry.coordinates[0].length; j++) {
    const tmp = [
      features[i].geometry.coordinates[0][j][1],
      features[i].geometry.coordinates[0][j][0],
    ];
    p.push(tmp);
  }
  L.polygon(p).addTo(map);
}
