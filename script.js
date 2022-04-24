
var basemap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

L.mapbox.accessToken = 'pk.eyJ1IjoidGFyZW5hcnRvIiwiYSI6ImNremw3YzIyNjUzODUyeHA0OXczOTA1azkifQ.LkcKPPxan4rvW-x3zxZVuA';

var CarAccidents=L.tileLayer('https://api.mapbox.com/styles/v1/tarenarto/ckzsu3bzn007x16kdwibqfrns/tiles/{z}/{x}/{y}?access_token=' + L.mapbox.accessToken, {
  tileSize: 512,
  zoomOffset: -1,
  attribution: '© <a href="https://apps.mapbox.com/feedback/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});

var map = L.map('map', {
  center: [51.0447, -114.0719],
  zoom: 12,
  layers: [basemap, CarAccidents]
});

var layers = {
  "Basemap": basemap,
  "Car Accidents": CarAccidents
};

L.control.layers(layers).addTo(map);

// var markers = L.layerGroup();

// var oms = new OverlappingMarkerSpiderfier(map);

// var points = L.geoJSON(geojsonFeature, {
//   pointToLayer: function (feature, latlng) {
//     return new L.Marker(latlng);
//   },
//   onEachFeature: function (feature, latlng) {
//     markers.addLayer(latlng), oms.addMarker(latlng)
//   }
// });

// L.markerClusterGroup.layerSupport().addTo(map).checkIn(markers)

// var popup = new L.Popup();

// oms.addListener('click', function (marker) {
//   popup.setContent('<h3>Issued Date:' + marker.feature.properties.issueddate + '</h3><p>Work Class Group: ' + marker.feature.properties.workclassgroup + '</p><p>Contractor Name:' + marker.feature.properties.contractorname + '</p><p>Community Name:' + marker.feature.properties.communityname + '</p><p>Original Address:' + marker.feature.properties.originaladdress + '</p>');
//   popup.setLatLng(marker.getLatLng());
//   map.openPopup(popup);
// });


// var sliderControl = L.control.sliderControl({
//   position: "topright",
//   layer: markers,
//   range: true
// });

// map.addControl(sliderControl);
// sliderControl.startSlider();

// function toggleLayer() {
//   if(map.hasLayer(CarAccidents)) {
//     map.removeLayer(CarAccidents);
//   } else {
//     map.addLayer(CarAccidents);
//   }
// }

