import L from 'leaflet';
import '../../scss/app.scss';


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
