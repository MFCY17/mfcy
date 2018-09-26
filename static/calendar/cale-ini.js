
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


    /* on drop Evento ya creado */
    CalendarApp.prototype.onDrop = function (eventObj, date) {
        var $this = this;
            // retrieve the dropped element's stored Event Object
            var originalEventObject = eventObj.data('eventObject');
            var $categoryClass = eventObj.attr('data-class');
            var $ideven = eventObj.attr('data-id');
            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);
            // assign it the date that was reported
            copiedEventObject.start = date;

            if ($categoryClass)
                copiedEventObject['color'] = $categoryClass;
                copiedEventObject['id'] = $ideven;

            // render the event on the calendar
            $this.$calendar.fullCalendar('renderEvent', copiedEventObject, true);
            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                eventObj.remove();
            }
    },

    /* on click on event */
    CalendarApp.prototype.onEventClick =  function (calEvent, jsEvent, view) {

          var $this = this;


            var form = $("<form></form>");
            $.ajax({
              url:"/json_consultar_evento/"+calEvent.id,
              type: "GET",
              success: function(data){
                $.each(data, function(i, item) {
                  form.append("<div class='row'></div>");
                  form.find(".row")
                      .append("<div class='col-md-12'><label><strong>Modificar: </strong>" + calEvent.title + "</label></div>")
                      .append("<div class='col-md-5'><img id='output' class='img-responsive img-thumbnail' src='https://i.pinimg.com/736x/ed/3e/66/ed3e660d4d40886cd87f6edcd5a5c7e1.jpg' alt=''><br><input type='file' id='imagen' class='form-control form-white' name='imagen' accept='image/*' onchange='loadFile(event)' placeholder='Sube una Imagen'></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Titulo</label><input class='form-control' id='titulo'  type='text'  value='" + calEvent.title + "' /></div></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Descripcion</label><textarea class='form-control' id='descripcion'>"+item.descripcion+"</textarea></div></div>")
                      .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Valor</label><input class='form-control' id='precio'  type='number' step='0.01'  value='"+item.costo+"' /></div></div>")
                      .append("<div class='col-md-4'><div class='form-group'><label class='control-label'>Tipo Evento</label><div class='input-group'><input class='form-control' id='precio'  type='text'  value='"+item.tipo+"' /><span class='input-group-btn'><button class='btn btn-secondary' type='button'>Cambiar</button></span></div></div></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Lugar del Evento: </label><div class='input-group'><input class='form-control' id='lugar'  type='text'  value='"+item.lugar+"' /><span class='input-group-btn'><button href='#demo' class='btn btn-secondary' data-toggle='collapse'>Cambiar</button></span></div></div></div>")
                      .append("<div class='col-md-7'><div id='map'></div></div>")
                      .append("<div class='col-md-12'><div id='demo' class='collapse form-group'><textarea class='form-control'  type='text' disabled rows='6' style='resize:none;'></textarea></div></div>")
                      .append("<input type='text' name='idEvent' id='idEvent' value='"+calEvent.id+"' />")
                      .append("<input type='hidden' name='latlng' id='latlng' value='"+item.lat+", "+item.log+"' />")
                      .append("<div class='col-md-12'><span class='input-group-btn'><button type='submit' class='btn btn-success waves-effect waves-light'><i class='fa fa-check'></i> Guardar</button></span></div>")

                });
              }
            });

            $this.$modal.modal({
                backdrop: 'static'
            }).on('shown.bs.modal', function () {
              var input = document.getElementById('latlng').value;
              var latlngStr = input.split(',', 2);
              var myLatLng = {
                lat: parseFloat(latlngStr[0]),
                lng: parseFloat(latlngStr[1])
              };
              var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 16,
                center: myLatLng
              });
              var marker = new google.maps.Marker({
                position: myLatLng,
                map: map,
                title: 'Hello World!'
              });
            });


            $this.$modal.find('.delete-event').show().end().find('.save-event').hide().end().find('.modal-body').empty().prepend(form).end().find('.delete-event').unbind('click').click(function () {
                // Eliminar evento
                $this.$calendarObj.fullCalendar('removeEvents', calEvent._id );
                $.ajax({
                  type: "GET",
                  url : '/eliminar_evento/'+calEvent._id,
                  success:function(data){
                    console.log(data);
                    alert("Evento Eliminado");
                  }
                });
                $this.$modal.modal('hide');
            });
            // Actualizar Evento
            $this.$modal.find('form').on('submit', function () {
                var file = form.find("#imgInp").val();
                var titulo = form.find("#titulo").val();
                var descripcion = form.find("#descripcion").val();
                var valor = form.find("#precio").val();
                var lugar = form.find("#lugar").val();
                var idE = form.find("#idEvent").val();
                var postData = $(this).serializeArray();
                calEvent.title = titulo;

                $this.$calendarObj.fullCalendar('updateEvent', calEvent);
                $this.$calendarObj.fullCalendar('rerenderEvents');
                var fecha = new Date(calEvent.start);
                var formatFecha = fecha.toISOString().slice(0,10).replace(/-/g,"-");
                var hstart=new Date(calEvent.start);
                var hstart = hstart.toISOString().slice(11,19).replace(/-/g,"-");
                var hend=new Date(calEvent.end);
                var hend = hend.toISOString().slice(11,19).replace(/-/g,"-");
                var rdata = {
                    'fecha':formatFecha,
                    'hstart':hstart,
                    'hend':hend,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                }
                $.ajax({
                  type: "POST",
                  url : '/json_update_evento/'+idE+'/',
                  data : rdata,
                  success:function(data){
                    console.log(data);
                  }
                });
                $this.$modal.modal('hide');
                return false;
            });
    },
    /* on select */
    CalendarApp.prototype.onSelect = function (start, end, allDay) {
        var $this = this;
            $this.$modal.modal({
                backdrop: 'static'
            });
            var form = $("<form></form>");
            form.append("<div class='row'></div>");
            form.find(".row")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Event Name</label><input class='form-control' placeholder='Insert Event Name' type='text' name='title'/></div></div>")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Category</label><select class='form-control' name='category'></select></div></div>")
                .find("select[name='category']")
                .append("<option value='bg-danger'>pp</option>")
                .append("<option value='bg-success'>Success</option>")
                .append("<option value='bg-purple'>Purple</option>")
                .append("<option value='bg-primary'>Primary</option>")
                .append("<option value='bg-pink'>Pink</option>")
                .append("<option value='bg-info'>Info</option>")
                .append("<option value='bg-warning'>Warning</option></div></div>");
            $this.$modal.find('.delete-event').hide().end().find('.save-event').show().end().find('.modal-body').empty().prepend(form).end().find('.save-event').unbind('click').click(function () {
                form.submit();
            });
            $this.$modal.find('form').on('submit', function () {
                var title = form.find("input[name='title']").val();
                var beginning = form.find("input[name='beginning']").val();
                var ending = form.find("input[name='ending']").val();
                var categoryClass = form.find("select[name='category'] option:checked").val();
                if (title !== null && title.length != 0) {
                    $this.$calendarObj.fullCalendar('renderEvent', {
                        title: title,
                        start:start,
                        end: end,
                        allDay: false,
                        className: categoryClass
                    }, true);
                    $this.$modal.modal('hide');
                }
                else{
                    alert('You have to give a title to your event');
                }
                return false;

            });
            $this.$calendarObj.fullCalendar('unselect');
    },
    CalendarApp.prototype.enableDrag = function() {
        //init events
        $(this.$event).each(function () {
            // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
            // it doesn't need to have a start or end
            var eventObject = {
                title: $.trim($(this).text()) // use the element's text as the event title
            };
            // store the Event Object in the DOM element so we can get to it later
            $(this).data('eventObject', eventObject);
            // make the event draggable using jQuery UI
            $(this).draggable({
                zIndex: 999,
                revert: true,      // will cause the event to go back to its
                revertDuration: 0  //  original position after the drag
            });
        });
    }
    /* Initializing */
    CalendarApp.prototype.init = function() {
        this.enableDrag();
        /*  Initialize the calendar  */
        var date = new Date();
        var d = date.getDate();
        var m = date.getMonth();
        var y = date.getFullYear();
        var form = '';
        var today = new Date($.now());
        console.log(today);
        // var defaultEvents =  [];
        var defaultEvents =  [{
                id:1,
                title: 'Released Ample Admin!',
                start: '2017-09-27 07:00:00',
                end: '2017-09-27 10:00:00',
                className: 'bg-info'
            }];
        $.ajax({
          url: '/json_all_eventos_rl',
          type: 'get',
          success: function(data) {
            $.each(data, function(i, item) {
              console.log(item);
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
            defaultView: 'agendaWeek',
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
            drop: function(date) { $this.onDrop($(this), date); },
            select: function (start, end, allDay) { $this.onSelect(start, end, allDay); },
            eventClick: function(calEvent, jsEvent, view) { $this.onEventClick(calEvent, jsEvent, view); }

        });

        //on new event
        this.$saveCategoryBtn.on('click', function(){
          var form3=$("#myform");
          // form3.submit();
          // var iamgen = $this.$categoryForm.find("input[name='imagen']").val();
          var name = $this.$categoryForm.find("input[name='event-titulo']").val();
          var descripcion = $this.$categoryForm.find("textarea[name='event-descripcion']").val();
          var valor = $this.$categoryForm.find("input[name='event-valor']").val();
          var tipo = $this.$categoryForm.find("select[name='event-tipo']").val();
          var music = $this.$categoryForm.find("select[name='event-music']").val();
          var lugar = $this.$categoryForm.find("select[name='event-lugar']").val();
          var postData = $(this).serializeArray();
          var rdata = {
              // 'imagen': iamgen,
              'name':name,
              'descripcion':descripcion,
              'valor':valor,
              'tipo':tipo,
              'music':music,
              'lugar':lugar
          }
          $.ajax({
                type: "POST",
                url : '/registro_evento',
                data : rdata,
                success:function(data)
                {
                  $.each(data, function(i, item) {
                    $this.$extEvents.append('<div class="calendar-events " data-id="'+item.valor+'" data-class="' +item.color+'" style="position: relative;"><i class="fa fa-circle " style="color:'+item.color+';"></i>' + name + '</div>')
                    $this.enableDrag();
                    alert("Evento Creado");
                  });
                }
              });
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
