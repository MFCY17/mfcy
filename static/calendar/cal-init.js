!function($) {
    "use strict";

    var CalendarApp = function() {
        this.$body = $("body")
        this.$calendar = $('#calendar'),
        this.$event = ('#calendar-events div.calendar-events'),
        this.$categoryForm = $('#add-new-event form'),
        this.$extEvents = $('#calendar-events'),
        this.$modal = $('#my-event'),
        this.$saveCategoryBtn = $('.save-category'),
        this.$calendarObj = null
    };


    /* on drop */
    CalendarApp.prototype.onDrop = function (eventObj, date) {
        var $this = this;
        alert('');
            // retrieve the dropped element's stored Event Object
            var originalEventObject = eventObj.data('eventObject');
            var $categoryClass = eventObj.attr('data-class');
            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);
            // assign it the date that was reported
            copiedEventObject.start = date;
            if ($categoryClass)
                copiedEventObject['className'] = [$categoryClass];
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
            var date = new Date(calEvent.start);
            var d = date.getDate();
            var m = date.getMonth();
            var y = date.getFullYear();
            var fecha_selecion=(d+1)+'/0'+(m+1)+'/'+y;
            var date1 = new Date(calEvent.end);
            var id=calEvent.id;
            console.log(calEvent)
            var $this = this;
            var form = $("<form></form>");
            var form2 = $("<form id='form2'></form>");

            if (isNaN(id)) {
              var ids=calEvent.allDay;
              $.ajax({
                url:"get_tareas/"+ids,
                type: "GET",
                success: function(data){
                  $.each(data, function(i, item) {
                    form2.append("<div class='row'></div>");
                    form2.find(".row")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Nombre Actividad</label><input class='form-control' id='titulo'  type='text'  value='" + item.titulo_actividad + "' /></div></div>")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Información:</label><textarea class='form-control'  id='descripcion' type='text'  rows='6' style='resize:none;'>"+date1+"</textarea></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>F. Inicio:</label><input class='form-control'  id='finicio' type='text' value='" + date1 + "' disabled /></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>H. Inicio:</label><input class='form-control'  id='hinicio' type='text' value='" + item.horainicio + "'  disabled/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>F. Finalización:</label><input class='form-control' id='ffin'  type='text'  value='" + item.fechafin + "'  disabled/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>H. Finalización:</label><input class='form-control' id='hfin'  type='text'  value='" + item.horafin + "'  disabled/></div></div>")
                  });
                }
              });
              $this.$modal.modal({
                backdrop: 'static'
              });
              $this.$modal.find('.delete-event').show().end().find('.update-event').show().end().find('.save-event').hide().end().find('.modal-body').empty().prepend(form2).end().find('.update-event').unbind('click').click(function () {
                  form2.submit();
              }),
              $this.$modal.find('.delete-event').unbind('click').click(function () {

                $.ajax({
                  url: 'eliminacion_logica_actividades/'+ids,
                  type: 'get',
                  success: function(data) {
                    $.toast().reset('all');
                    $.toast({
                        heading: 'Eliminacion',
                        text: 'La tarea se a eliminado con éxito',
                        showHideTransition: 'fade', // fade, slide or plain
                        allowToastClose: true,
                        position: 'top-right',
                        icon: 'error',
                        hideAfter: 2500,
                        stack: 1,
                        loaderBg: '#fff',
                    });

                  }
                });
                setTimeout(function () {
                   window.location.href = "/buscar_actividades"; //will redirect to your blog page (an ex: blog.html)
                }, 3000);
              });

            }else {
              $.ajax({
                url:"get_actividades/"+id,
                type: "GET",
                success: function(data){
                  $.each(data, function(i, item) {

                    form.append("<div class='row'></div>");
                    form.find(".row")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Nombre Actividad</label><input class='form-control'  type='text'  value='" + item.titulo_actividad + "' disabled/></div></div>")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Informacion:</label><textarea class='form-control'  type='text' disabled rows='3' style='resize:none;'>"+date1+"</textarea></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>F. Entrega:</label><input class='form-control'  type='text'  name='fecha_actividad' id='fechactividad' value='" + date1 + "' disabled /></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>H. Entrega:</label><input class='form-control'  type='text'  value='" + item.horafin + "' disabled /></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Nota:</label><input class='form-control'  type='text'  value='" +item.nota+ "' disabled /></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Tipo:</label><input class='form-control'  type='text'  value='" +item.entregapor+ "' disabled /></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Esq Calificacion:</label><a href='#demo' class='btn btn-info' data-toggle='collapse'>Ver mas</a></div></div>")
                    .append("<div class='col-md-9'><div class='form-group'><label class='control-label'>Medio de Entrega:</label><input class='form-control'  type='text'  value='" +item.metodoentrega+ "' disabled /></div></div>")
                    .append("<div class='col-md-12'><div id='demo' class='collapse form-group'><label class='control-label'>Esquema de Calificación:</label><textarea class='form-control'  type='text' disabled rows='6' style='resize:none;'>"+item.descripcion+"</textarea></div></div>")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Planificar Actividad</label></div></div>")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Actividad</label><input class='form-control' placeholder='Insertar Actividad' id='tituss' type='text' name='title'/></div></div>")
                    .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Descripcion</label><input class='form-control' placeholder='Insertar Actividad' type='text' id='desc' name='descripcion'/></div></div>")
                    .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Fecha Realizacion</label><input class='form-control' type='date' id='fechainicio' name='hora'/></div></div>")
                    .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Fecha Caducidad</label><input class='form-control' placeholder='Insertar Actividad' type='date' id='fechacad' name='hora'/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>H. Inicio</label><input class='form-control' placeholder='Insertar Actividad' type='time' id='horainici' name='hora'/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>H. Finalizacion:</label><input class='form-control' placeholder='Insertar Actividad' id='horafin' type='time' name='hora'/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Una Tarea </label><br><input type='radio' id='estado' value='1' name='estado'/></div></div>")
                    .append("<div class='col-md-3'><div class='form-group'><label class='control-label'>Varias Tareas</label><br><input id='estado' type='radio' value='0' name='estado'/></div></div>")

                  });
                }
              });
              $this.$modal.modal({
                  backdrop: 'static'
              });

              $this.$modal.find('.delete-event').hide().end().find('.update-event').hide().end().find('.save-event').show().end().find('.modal-body').empty().prepend(form).end().find('.save-event').unbind('click').click(function () {
                  form.submit();
              });
            }
            $this.$modal.find('#form2').on('submit', function () {
              var titulo = form2.find("#titulo").val();
              var descripcion = form2.find("#descripcion").val();
              var finicio = form2.find("#finicio").val();
              var hinicio = form2.find("#hinicio").val();
              var ffin = form2.find("#ffin").val();
              var hfin = form2.find("#hfin").val();
              var postData = $(this).serializeArray();

              var rdata = {
                  'titulo': titulo,
                  'descripcion':descripcion,
                  'finicio':finicio,
                  'hinicio':hinicio,
                  'ffin':ffin,
                  'hfin':hfin,
                  csrfmiddlewaretoken: '{{ csrf_token }}'
              }

              $.ajax(
                  {
                      type: "POST",
                      url : 'update_registro_actividades/'+ids,
                      data : rdata,
                      success:function(data)
                      {
                        $.toast().reset('all');
                        $.toast({
                            heading: 'Actualizacion',
                            text: 'La tarea se a actualizado con exito',
                            showHideTransition: 'fade', // fade, slide or plain
                            allowToastClose: true,
                            position: 'top-right',
                            icon: 'success',
                            hideAfter: 2500,
                            stack: 1,
                            loaderBg: '#fff',
                        });
                      }
                  });
                  setTimeout(function () {
                     window.location.href = "/buscar_actividades"; //will redirect to your blog page (an ex: blog.html)
                  }, 3000);

            });


            $this.$modal.find('form').on('submit', function () {
              var fechactividad = form.find("#fechactividad").val();
              var title = form.find("#tituss").val();
              var beginning = form.find("#desc").val();
              var ending = form.find("#fechainicio").val();
              var fechacad = form.find("#fechacad").val();
              var horain = form.find("#horainici").val();
              var horafin = form.find("#horafin").val();
              var estado = form.find("input:radio[name=estado]:checked").val();
              var postData = $(this).serializeArray();
              var fechafor1=new Date(fechacad);
              var df = fechafor1.getDate();
              var mf = fechafor1.getMonth();
              var yf = fechafor1.getFullYear();
              var fechaf=yf+'-'+(mf+1)+'-'+(df+1);

              if (new Date(fechaf).getTime() > new Date(fechactividad).getTime()) {
                $.toast().reset('all');
                $.toast({
                    heading: 'Fecha Superada',
                    text: 'La fecha de inicializacion e finalizacion de la tarea sobrepasa la fecha de entrega.',
                    showHideTransition: 'fade', // fade, slide or plain
                    allowToastClose: true,
                    position: 'top-right',
                    icon: 'warning',
                    hideAfter: 2500,
                    stack: 0,
                    loaderBg: '#000',
                });

              }else{
                if (estado == 1) {
                  $.ajax({
                    url: '/update_estado_actividad/'+id,
                    type: 'get',
                    success: function(data) {
                      $.each(data, function(i, item) {
                        console.log(item)
                      });
                    }
                  });
                }
                var rdata = {
                    'title': title,
                    'beginning':beginning,
                    'fechaincio':ending,
                    'fechacad':fechacad,
                    'horain':horain,
                    'horafin':horafin,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                }

                $.ajax(
                    {
                        type: "POST",
                        url : 'registro_actividades_tareas/'+id,
                        data : rdata,
                        success:function(data)
                        {
                          $.toast().reset('all');
                          $.toast({
                              heading: 'Registro',
                              text: 'La tarea se a planificado con exito',
                              showHideTransition: 'fade', // fade, slide or plain
                              allowToastClose: true,
                              position: 'top-right',
                              icon: 'success',
                              hideAfter: 2500,
                              stack: 1,
                              loaderBg: '#fff',
                          });
                        }
                    });
                    setTimeout(function () {
                       window.location.href = "/buscar_actividades"; //will redirect to your blog page (an ex: blog.html)
                    }, 3000);

              }

                calEvent.title = form.find("input[type=text]").val();
                $this.$calendarObj.fullCalendar('updateEvent', calEvent);
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
                .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Actividad</label><input class='form-control' placeholder='Insertar Actividad' id='tituss' type='text' name='title'/></div></div>")
                .append("<div class='col-md-12'><div class='form-group'><label class='control-label'>Descripcion</label><input class='form-control' placeholder='Insertar Actividad' type='text' id='desc' name='descripcion'/></div></div>")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Fecha Realizacion</label><input class='form-control' placeholder='Insertar Actividad' type='date' id='fechainicio' name='hora'/></div></div>")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Fecha Caducidad</label><input class='form-control' placeholder='Insertar Actividad' type='date' id='fechacad' name='hora'/></div></div>")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Hora Incio</label><input class='form-control' placeholder='Insertar Actividad' type='time' id='horainici' name='hora'/></div></div>")
                .append("<div class='col-md-6'><div class='form-group'><label class='control-label'>Hora Finalizacion:</label><input class='form-control' placeholder='Insertar Actividad' id='horafin' type='time' name='hora'/></div></div>")
            $this.$modal.find('.delete-event').hide().end().find('.update-event').hide().end().find('.save-event').show().end().find('.modal-body').empty().prepend(form).end().find('.save-event').unbind('click').click(function () {
                form.submit();
            });
            $this.$modal.find('form').on('submit', function () {
                var title = form.find("#tituss").val();
                var beginning = form.find("#desc").val();
                var ending = form.find("#fechainicio").val();
                var fechacad = form.find("#fechacad").val();
                var horain = form.find("#horainici").val();
                var horafin = form.find("#horafin").val();
                var postData = $(this).serializeArray();
                var rdata = {
                    'title': title,
                    'beginning':beginning,
                    'fechaincio':ending,
                    'fechacad':fechacad,
                    'horain':horain,
                    'horafin':horafin,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                }

                $.ajax(
                    {
                        type: "POST",
                        url : '/registro_actividades',
                        data : rdata,
                        success:function(data)
                        {
                          $.toast().reset('all');
                          $.toast({
                              heading: 'Registro',
                              text: 'La tarea se a planificado con exito',
                              showHideTransition: 'fade', // fade, slide or plain
                              allowToastClose: true,
                              position: 'top-right',
                              icon: 'success',
                              hideAfter: 2500,
                              stack: 1,
                              loaderBg: '#fff',
                          });
                        }
                    });
                if (title !== null && title.length != 0) {
                    $this.$calendarObj.fullCalendar('renderEvent', {
                        title: title,
                        start:start,
                        end: end,
                        allDay: false,
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
        alert(new Date('09/09/2017 12:12:12'));
        var fecha= '';
        var form = '';

        var $this = this;

        // formato mes/dia/año
        var defaultEvents =  [
          {
              id:1,
              title: 'Long Event',
              start: new Date('2017/9/29 01:30:00'),
              end: new Date('2017/9/29 02:30:00')
          },
          {
              id:2,
              title: 'Long Event',
              start: new Date('2017/9/30 02:00:00'),
              end: new Date('2017/9/30 04:15:00'),
              className: 'bg-danger'
          },
          {
              id:3,
              title: 'Long Event',
              start: new Date('2017/9/31 04:00:00'),
              end: new Date('2017/9/31 06:30:00'),
              className: 'bg-info'
          }

        ];
          // $.ajax({
          //   url: '/json_componentes',
          //   type: 'get',
          //   success: function(data) {
          //     for(var i = 0; i < data.length;i++){
          //        for (var j = 0; j <6; j++) {
          //          switch(data[i].diaclase || data[i].diatutoria) {
          //              case 'Lunes':
          //                  today =new Date(ye,me,di);
          //                  break;
          //              case 'Martes':
          //                  today =new Date(ye,me,di+1);
          //                  break;
          //              case 'Miercoles':
          //                  today =new Date(ye,me,di+2);
          //                  break;
          //              case 'Jueves':
          //                  today =new Date(ye,me,di+3);
          //                  break;
          //              case 'Viernes':
          //                  today =new Date(ye,me,di+4);
          //                  break;
          //              default:
          //                  today =new Date(ye,me,di);
          //          }
          //          $this.$calendarObj.fullCalendar('renderEvent', {
          //              title: data[i].nombre,
          //              start: today,
          //              end: today,
          //              allDay: true,
          //              className: 'bg-success'
          //          }, true);
          //           di=di+7;
          //           if (j == 5) {
          //             di=24;
          //           }
          //        }
          //
          //     }
          //   }
          // });
          // $.ajax({
          //   url: '/json_tareas',
          //   type: 'get',
          //   success: function(data) {
          //     $.each(data, function(i, item) {
          //       $this.$calendarObj.fullCalendar('renderEvent', {
          //           title: item.titulo_actividad,
          //           start: new Date(item.feini),
          //           end: new Date(item.fefin),
          //           allDay: item.id_actividad,
          //           className: 'bg-danger'
          //       }, true);
          //     });
          //
          //   }
          // });




        $this.$calendarObj = $this.$calendar.fullCalendar({
            slotDuration: '00:15:00', /* If we want to split day time each 15minutes */
            minTime: '06:00:00',
            maxTime: '24:00:00',
            locale: 'es',
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
            var categoryName = $this.$categoryForm.find("input[name='category-name']").val();
            var categoryColor = $this.$categoryForm.find("select[name='category-color']").val();
            if (categoryName !== null && categoryName.length != 0) {
                $this.$extEvents.append('<div class="calendar-events bg-' + categoryColor + '" data-class="bg-' + categoryColor + '" style="position: relative;"><i class="fa fa-move"></i>' + categoryName + '</div>')
                $this.enableDrag();
            }

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
