$(document).ready(function () {
  
  function addGeneralClass(){
  $(".textinput,.emailinput,.checkboxinput,.dateinput,.textarea,.numberinput").each(function(){
      $(this).addClass("form-control")
    });
    $(".select").each(function(){
      $(this).select2({width:'100%'});
    });
  };
  var MuestraFormulario = function(){
    var btn = $(this);
    $.ajax({
      url : btn.attr('data-url'),
      type: 'get',
      dataType:'json',
      beforeSend: function(){
        $('#modal-generic').modal('show');
      },
      success:function(data){
        $('#modal-generic .modal-content').html(data.html_form)
        addGeneralClass();
        if(data.extra_function){
          funcion_generica(data);
        }
      }
    });
  };
  var GuardaFormulario = function(){
    var form = $(this);
    console.log(form.attr('data-url'))
    $.ajax({
        url: form.attr('data-url'),
        data: form.serialize(),
        type: form.attr('method'),
        dataType: 'json',
        success: function(data){
          if(data.form_is_valid){
            $('#table_generic tbody').html(data.object_list);
            if(data.hide_modal){
              $('#modal-generic').modal('hide');
            }       
            if(data.message){
              $('#notificacion').append('<div class="alert alert-success"><b>'+data.message+' </b></div>');
              setTimeout(function () {
                $('#notificacion').empty();
            }, 3300);
            }
            if(data.extra_function){
              funcion_generica(data);
            }
          }
          else {
            $('#modal-generic .modal-content').html(data.html_form)
            addGeneralClass();
          }
        }
    })
    return false;
  }


  $('#table_generic').DataTable({
    "oLanguage": {
    "sProcessing": "Cargando...",
    "sLengthMenu": "Mostrar _MENU_ registros",
    "sZeroRecords": "No se encontraron resultados",
    "sEmptyTable": "Ningún dato disponible en esta tabla",
    "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
    "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
    "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
    "sInfoPostFix": "",
    "sSearch": "Buscar:",
    "sUrl": "",
    "sInfoThousands": ",",
    "sLoadingRecords": "Cargando...",
    "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
    },
    "oAria": {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
    }
}
}); 
  // crear
  $(".show-form").click(MuestraFormulario);
  $("#modal-generic").on("submit",".create-form",GuardaFormulario)
  // actualizar
  $("#table_generic").on("click",".show-form",MuestraFormulario)
  $("#table_generic").on("click",".show-form-update",MuestraFormulario)
  $("#modal-generic").on("submit",".update-form",GuardaFormulario)

  // eliminar
  $("#table_generic").on("click",".show-form-delete",MuestraFormulario)
  $("#modal-generic").on("submit",".delete-form",GuardaFormulario)
});
