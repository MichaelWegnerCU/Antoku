;(function(){

			// Menu settings
			$('#menuToggle, .menu-close').on('click', function(){
				$('#menuToggle').toggleClass('active');
				$('body').toggleClass('body-push-toleft');
				$('#theMenu').toggleClass('menu-open');
			});


})
    

    function initMap() {
    
    
    
    
    var locations = '{{content}}';

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,

      center: new google.maps.LatLng(40.03, -105.26)
      
    });

    var infowindow = new google.maps.InfoWindow();

    var marker;
    

    var i= 1;

    {% for c in content %}

        var LAT_in = '{{ c.LNG }}';
        var LNG_in = '{{ c.LAT }}';
        var icon_out= 'https://raw.githubusercontent.com/Concept211/Google-Maps-Markers/master/images/marker_blue'+i+'.png';
        i++;
        LAT_LNG={lat: parseFloat('{{ c.LNG }}'), lng: parseFloat('{{ c.LAT }}') },
        marker = new google.maps.Marker({
          animation: google.maps.Animation.DROP,
          position: new google.maps.LatLng(LAT_LNG),
          map: map,
          title: '{{c.street_address}}',
          icon: icon_out
        });
    {% endfor %}
  }

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}




(jQuery)