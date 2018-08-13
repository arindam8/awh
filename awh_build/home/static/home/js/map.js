  // This example creates circles on the map, representing populations in North
  // America.

  // First, create an object containing LatLng and population for each city.
  var citymap = {
    london: {
      center: {lat: 51.509865, lng: -0.118092},
      population: 2714856
    },
    manchester: {
      center: {lat: 53.4808, lng: -2.2426},
      population: 2714856
    }
  };

  function initMap() {
    // Create the map.
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 6.5,
      center: {lat: 51.509865, lng: -0.118092},
      mapTypeId: 'terrain'
    });

    // Construct the circle for each value in citymap.
    // Note: We scale the area of the circle based on the population.
    for (var city in citymap) {
      // Add the circle for this city to the map.
      var cityCircle = new google.maps.Circle({
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#FF0000',
        fillOpacity: 0.35,
        map: map,
        center: citymap[city].center,
        radius: Math.sqrt(citymap[city].population) * 40
      });
    }
  }