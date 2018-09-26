
!function($) {
    "use strict";

    var CalendarApp = function() {
        this.$body = $("body")
        this.$calendar = $('#calendar'),
        this.$event = ('#calendar-events div.calendar-events'),
        this.$categoryForm = $('#add-new-event form'),
        this.$extEvents = $('#calendar-events'),
        this.$modal = $('#my-event'),
        this.$modal2 = $('#add-new-event'),
        this.$saveCategoryBtn = $('.save-category'),
        this.$calendarObj = null
    };


    /* on click on event */
    CalendarApp.prototype.onEventClick =  function (calEvent, jsEvent, view) {
          var $this = this;
            var form = $("<form></form>");
            $.ajax({
              url:"/json_consultar_evento_cl/"+calEvent.id,
              type: "GET",
              success: function(data){
                $.each(data, function(i, item) {
                  console.log(item);
                  form.append("<div class='row'></div>");
                  form.find(".row")
                      .append("<div class='col-md-5'><img id='output' class='img-responsive img-thumbnail' src='static/media/"+item.image+"' alt=''></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Titulo</label><div>" + calEvent.title + "</div></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Descripcion</label><div style='text-align:justify'>"+item.descripcion+"</div></div></div>")
                      .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Valor</label><div>"+item.costo+"</div></div>")
                      .append("<div class='col-md-4'><div class='form-group'><label class='control-label'>Tipo Evento</label><div>"+item.tipo+"</div></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Lugar del Evento: </label><div>"+item.lugar+"</div></div>")
                      .append("<input type='hidden' name='latlng' id='latlng' value='"+item.lat+", "+item.log+"' />")
                      .append("<div class='col-md-12'><br><h5><i class='fa fa-hand-o-right' aria-hidden='true'></i> COMÓ LLEGAR?</h5><br></div>")
                      .append("<div class='col-md-8'><div id='map'></div></div>")
                      .append("<div class='col-md-4'><div id='right-panel'><br><p>Total Distance: <span id='total'></span></p></div></div>")
                });
              }
            });
            $this.$modal.find('.modal-body').empty().prepend(form).end();
            $this.$modal.modal({
                backdrop: 'static'
            }).on('shown.bs.modal', function () {
              google.maps.event.trigger(map, 'resize');


              var input = document.getElementById('latlng').value;
              var latlngStr = input.split(',', 2);
              var myLatLng = {lat: parseFloat(latlngStr[0]),lng: parseFloat(latlngStr[1])};
              if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                  var pos = {lat: position.coords.latitude,lng: position.coords.longitude};
                  displayRoute(position.coords.latitude + ',' + position.coords.longitude, myLatLng, directionsService,directionsDisplay);
                  map.setCenter(pos);
                }, function() {
                  handleLocationError(true, infoWindow, map.getCenter());
                });
              }else {
                handleLocationError(false, infoWindow, map.getCenter());
              }
              var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: myLatLng
              });
              var directionsService = new google.maps.DirectionsService;
              var directionsDisplay = new google.maps.DirectionsRenderer({
                draggable: true,
                map: map,
                panel: document.getElementById('right-panel')
              });
              directionsDisplay.addListener('directions_changed', function() {
                computeTotalDistance(directionsDisplay.getDirections());
              });
              function displayRoute(origin, destination, service, display) {
                service.route({
                  origin: origin,
                  destination: destination,
                  travelMode: 'DRIVING',
                  avoidTolls: true
                },function(response, status) {
                  if (status === 'OK') {
                    display.setDirections(response);
                  } else {
                    alert('Could not display directions due to: ' + status);
                  }
                });
              }
              function computeTotalDistance(result) {
                var total = 0;
                var myroute = result.routes[0];
                for (var i = 0; i < myroute.legs.length; i++) {
                  total += myroute.legs[i].distance.value;
                }
                total = total / 1000;
                document.getElementById('total').innerHTML = total + ' km';
              }
            });







    },
    /* Initializing */
    CalendarApp.prototype.init = function() {
        // this.enableDrag();
        /*  Initialize the calendar  */
        var date = new Date();
        var d = date.getDate();
        var m = date.getMonth();
        var y = date.getFullYear();
        var form = '';
        var today = new Date($.now());
        console.log(today);
        var defaultEvents =  [];

        $.ajax({
          url: '/json_all_eventos_cl',
          type: 'get',
          success: function(data) {
            $.each(data, function(i, item) {
              $this.$calendarObj.fullCalendar('renderEvent', {
                  id: item.id,
                  title: item.nombre,
                  start: item.hstart,
                  end: item.hend,
                  allDay: false,
                  color: item.tipo
              }, true);
            });

          }
        });

        var $this = this;
        $this.$calendarObj = $this.$calendar.fullCalendar({
            slotDuration: '00:15:00', /* If we want to split day time each 15minutes */
            minTime: '06:00:00',
            maxTime: '24:00:00',
            defaultView: 'month',
            handleWindowResize: true,

            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay,listDay'
            },
            events: defaultEvents,
            editable: true,
            droppable: true, // this allows things to be dropped onto the calendar !!!
            eventLimit: true, // allow "more" link when too many events
            selectable: true,
            eventClick: function(calEvent, jsEvent, view) { $this.onEventClick(calEvent, jsEvent, view); }

        });


    },

   //init CalendarApp
    $.CalendarApp = new CalendarApp, $.CalendarApp.Constructor = CalendarApp

}(window.jQuery),

//initializing CalendarApp
function($) {
    "use strict";
    $.CalendarApp.init()
}(window.jQuery);
