import L from 'leaflet';
import '../../scss/app.scss';

const volcanoesData = document.getElementById('volcanoesData');
const data = JSON.parse(volcanoesData.value)['features'];

// init.
const center = [36.2048, 138.2529];
const zoom = 6;
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
  const name = data[i].properties.Name;
  const geo = data[i].geometry.coordinates;
  const pos = [geo[1], geo[0]];
  const popup = `<p>name: ${name}</p>`;
  L.marker(pos, { icon: icon })
    .addTo(map)
    .bindPopup(popup);
}
