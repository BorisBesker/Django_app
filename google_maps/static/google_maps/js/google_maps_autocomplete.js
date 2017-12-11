// Autocomplete function for google search

function init() {
     var input = document.getElementById('locationTextField');
     var autocomplete = new google.maps.places.Autocomplete(input);
 }

 google.maps.event.addDomListener(window, 'load', init);
