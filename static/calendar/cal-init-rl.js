
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

            var form = $("<form method='POST' enctype='multipart/form-data'></form>");
            $.ajax({
              url:"/json_consultar_evento_cl/"+calEvent.id,
              type: "GET",
              success: function(data){
                $.each(data, function(i, item) {
                  form.append("<div class='row'></div>");
                  form.find(".row")
                      .append("<div class='col-md-12'><label><strong>Modificar: </strong>" + calEvent.title + "</label></div>")
                      .append("<div class='col-md-5'><img id='output' class='img-responsive img-thumbnail' src='/static/media/"+item.image+"' alt=''><br><input type='file' id='imagen' class='form-control form-white' name='imagen' accept='image/*' onchange='loadFile(event)' placeholder='Sube una Imagen'></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Titulo</label><input class='form-control' id='titulo' name='titulo'  type='text'  value='" + calEvent.title + "' /></div></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Descripcion</label><textarea class='form-control' id='descripcion3' name='descripcion'>"+item.descripcion+"</textarea></div></div>")
                      .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Valor</label><input class='form-control' id='precio' name='precio'  type='number' step='0.01'  value='"+item.costo+"' /></div></div>")
                      .append("<div class='col-md-4'>"+
                        "<label class='control-label'>Tipo de Evento</label>"+
                        "<select class='form-control form-white' data-placeholder='Choose a color...'' name='tipo' id='tipo'>"+
                          "<option value='0'>Seleccionar</option>"+
                          "<option value='1'>Formal</option>"+
                          "<option value='2'>SemiFomal</option>"+
                          "<option value='3'>Informal</option>"+
                        "</select></div>")
                      .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Lugar del Evento: </label><div>"+item.lugar+"</div></div>")
                      .append("<div class='col-md-12'><div id='map'></div></div>")
                      .append("<input type='hidden' name='idtipo' id='idtipo' value='"+item.id_tipo+"' />")
                      .append("<input type='hidden' name='idEvent' id='idEvent' value='"+calEvent.id+"' />")
                      .append("<input type='hidden' name='latlng' id='latlng' value='"+item.lat+", "+item.log+"' />")
                      .append("<div class='col-md-12'><span class='input-group-btn'><input type='submit' class='btn btn-success waves-effect waves-light' name='Guardar' value='Guardar'></span></div>")
                });
              }
            });

            $this.$modal.modal({
                backdrop: 'static'
            }).on('shown.bs.modal', function () {
              var id = document.getElementById('idtipo').value;
              $('#tipo option').each(function() {
                  if($(this).val() == id) {
                      $(this).prop("selected", true);
                  }
              });
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
              CKEDITOR.replace('descripcion3',{
                height : 190,
              });
            });


            $this.$modal.find('.delete-event').show().end().find('.save-event').hide().end().find('.modal-body').empty().prepend(form).end().find('.delete-event').unbind('click').click(function () {
                // Eliminar evento
                $this.$calendarObj.fullCalendar('removeEvents', calEvent._id );
                $.ajax({
                  type: "GET",
                  url : '/eliminar_evento_rl/'+calEvent._id,
                  success:function(data){
                    console.log(data);
                    $.toast({
                        heading: 'Artes Vivas Unesco',
                        text: 'El evento se a eliminado con exito',
                        position: 'top-right',
                        loaderBg: '#ff6849',
                        icon: 'error',
                        hideAfter: 3500

                    });
                  }
                });
                $this.$modal.modal('hide');
            });
            // Actualizar Evento
            $this.$modal.find('form').on('submit', function () {
                var data = new FormData(this);
                var titulo = form.find("#titulo").val();
                var idE = form.find("#idEvent").val();
                calEvent.title = titulo;
                $this.$calendarObj.fullCalendar('updateEvent', calEvent);
                // Rendirezacion de metodos
                $this.$calendarObj.fullCalendar('rerenderEvents');
                var fecha = new Date(calEvent.start);
                var formatFecha = fecha.toISOString().slice(0,10).replace(/-/g,"-");
                var hstart=new Date(calEvent.start);
                var hstart = hstart.toISOString().slice(11,19).replace(/-/g,"-");
                var hend=new Date(calEvent.end);
                var hend = hend.toISOString().slice(11,19).replace(/-/g,"-");
                // Agregar valores a Data
                data.append('descripcion', CKEDITOR.instances['descripcion3'].getData());
                data.append('fecha', formatFecha);
                data.append('hstart', hstart);
                data.append('hend', hend);

                $.ajax({
                  type: "POST",
                  url : '/json_update_evento_rl/'+idE+'/',
                  data : data,
                  contentType: false,
                  cache: false,
                  processData:false,
                  success:function(data){
                    console.log(data);
                    $.toast({
                        heading: 'Artes Vivas Unesco ',
                        text: 'El evento a sido actualizado ',
                        position: 'top-right',
                        loaderBg: '#ff6849',
                        icon: 'warning',
                        hideAfter: 3500,
                        stack: 6
                    });
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
            }).on('shown.bs.modal', function () {
              $.ajax({
                type: "GET",
                url: "/web_service_gn",
                success: function(response){
                  $('#select-music').html(response.generos);
                }
              });
              CKEDITOR.replace('descripcion2',{height : 150,});
             });
            var form = $("<form method='POST' enctype='multipart/form-data'></form>");
            form.append("<div class='row'></div>");
            form.find(".row")
                .append("<div class='col-md-5'><label class='control-label'>Imagen</label><img id='output' class='img-responsive img-thumbnail' src='https://i.pinimg.com/736x/ed/3e/66/ed3e660d4d40886cd87f6edcd5a5c7e1.jpg' alt=''><br><br><input type='file' id='portada' class='form-control form-white' name='portada' accept='image/*' onchange='loadFile(event)' placeholder='Sube una Imagen'></div>")
                .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Titulo</label><input class='form-control' id='titulo' name='event-titulo'  type='text'  value='' placeholder='Titulo'/></div></div>")
                .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Descripcion</label><textarea class='form-control' id='descripcion2' name='event-descripcion'></textarea></div></div>")
                .append("<div class='col-md-7'><div class='form-group'><label class='control-label'>Valor</label><input class='form-control' id='precio' name='event-valor'  type='number' step='0.01'  value='' placeholder='$ 0.00' /></div></div>")
                .append("<div class='col-md-3'>"+
                  "<label class='control-label'>Tipo de Evento</label>"+
                  "<select class='form-control form-white' data-placeholder='Choose a color...'' name='event-tipo' id='tipo'>"+
                    "<option value='0'>Seleccionar</option>"+
                    "<option value='1'>Formal</option>"+
                    "<option value='2'>SemiFomal</option>"+
                    "<option value='3'>Informal</option>"+
                  "</select></div>")
                .append("<div class='col-md-4'>"+
                  "<label class='control-label'>Tipo de musica</label>"+
                  "<select id='select-music' class='form-control form-white' data-placeholder='Choose a cr...' name='event-music'></select></div>")
                .append("<input type='hidden' name='event-estado' value='1' />")
                .append("<input type='hidden' name='idtipo' id='idtipo' value='' />")
                .append("<input type='hidden' name='idEvent' id='idEvent' value='' />");

            $this.$modal.find('.delete-event').hide().end().find('.save-event').show().end().find('.modal-body').empty().prepend(form).end().find('.save-event').unbind('click').click(function () {
                form.submit();
            });
            $this.$modal.find('form').on('submit', function () {
                var data = new FormData(this);
                data.append('event-descripcion', CKEDITOR.instances['descripcion2'].getData());
                var title = form.find("input[name='event-titulo']").val();
                var categoryClass = form.find("select[name='category'] option:checked").val();
                if (title !== null && title.length != 0) {

                    // $this.$calendarObj.fullCalendar('rerenderEvents');
                    var fecha = new Date(start);
                    var formatFecha = fecha.toISOString().slice(0,10).replace(/-/g,"-");
                    var hstart=new Date(start);
                    var hstart = hstart.toISOString().slice(11,19).replace(/-/g,"-");
                    var hend=new Date(end);
                    var hend = hend.toISOString().slice(11,19).replace(/-/g,"-");
                    data.append('event-fecha', formatFecha);
                    data.append('event-start', hstart);
                    data.append('event-end', hend);
                    $.ajax({
                      url: "/insert_evento_rl",
                      type: "POST",
                      data:  data,
                      contentType: false,
                      cache: false,
                      processData:false,
                      success: function(data){
                        console.log(data);
                        $.each(data, function(i, item) {
                          $this.$calendarObj.fullCalendar('renderEvent', {
                            id: item.valor,
                            title: title,
                            start: start,
                            end: end,
                            allDay: false,
                            color: item.color
                          }, true);
                        });
                      }
                    });
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
        $this.$categoryForm.on('submit',function(e) {
          e.preventDefault(); //prevent the form from submitting
          var data = new FormData(this);
          data.append('event-descripcion', CKEDITOR.instances['event-descripcion'].getData());
          $.ajax({
            url: "/insert_evento_rl",
            type: "POST",
            data:  data,
            contentType: false,
            cache: false,
            processData:false,
            success: function(data){
              $.each(data, function(i, item) {
                $this.$extEvents.append('<div class="calendar-events " data-id="'+item.valor+'" data-class="' +item.color+'" style="position: relative;"><i class="fa fa-circle " style="color:'+item.color+';"></i>'+item.title+'</div>')
                $this.enableDrag();
                $.toast({
                    heading: 'Artes Vivas Unesco',
                    text: 'El evento se ah creado con exito ',
                    position: 'top-right',
                    loaderBg: '#ff6849',
                    icon: 'success',
                    hideAfter: 3500,
                    stack: 6
                });
              });
            }
          });

        });

        this.$saveCategoryBtn.on('click', function(){
          var form3=$("#myform");
          form3.submit();

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
