const LON = 0;
const LAT = 1;
const DATETIME = 2;
const DEPTH = 3;
const AREA = 4;
const MAGNITUDE = 5;

function init() {
  const seismList = document.getElementById('seismList');
  const data = JSON.parse(seismList.value)['data'];

  const map = new OpenLayers.Map('basicMap');
  const mapnik = new OpenLayers.Layer.OSM();
  const fromProjection = new OpenLayers.Projection('EPSG:4326');
  const toProjection = new OpenLayers.Projection('EPSG:900913');
  // japan center position.
  const position = new OpenLayers.LonLat(138.2529, 36.2048).transform(
    fromProjection,
    toProjection
  );
  // all view japan.
  const zoom = 6;
  map.addLayer(mapnik);
  map.setCenter(position, zoom);

  // add marker.
  const markers = new OpenLayers.Layer.Markers('Markers');
  map.addLayer(markers);
  // // size.
  // const size = new OpenLayers.Size(16, 16);
  // const offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);
  // const icon = new OpenLayers.Icon(
  //   'static/js/OpenLayers-2.13.1/img/marker.png',
  //   size,
  //   offset
  // );

  for (let i = 0; i < data.length; i++) {
    const d = data[i];
    const pos = new OpenLayers.LonLat(d[LON], d[LAT]).transform(
      fromProjection,
      toProjection
    );
    // const marker = new OpenLayers.Marker(pos, icon);
    const marker = new OpenLayers.Marker(pos);
    // add enevt.
    let popup = null;
    marker.events.register('click', marker, function() {
      popup = new OpenLayers.Popup.FramedCloud(
        'Popup',
        pos,
        null,
        `<p>area: ${d[AREA]}</p>
        <p>depth: ${d[DEPTH]}</p>
        <p>magnitude: ${d[MAGNITUDE]}</p>`,
        null,
        false
      );
      map.addPopup(popup);
    });
    marker.events.register('mouseout', marker, function() {
      setTimeout(function() {
        popup.hide();
      }, 200);
    });
    markers.addMarker(marker);
  }
}
