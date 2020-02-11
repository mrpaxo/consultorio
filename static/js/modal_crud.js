$(document).ready(function () {
  
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
        $(".textinput,.select,.emailinput,.checkboxinput").each(function(){
          console.log(this)
           $(this).addClass("form-control")
         });
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
            console.log('datos guardados con exito')
            if(data.hide_modal){
              $('#modal-generic').modal('hide');
            }       
            if(data.extra_function){
              funcion_generica(data);
            }
          }
          else {
            console.log('entro else')
            $('#modal-generic .modal-content').html(data.html_form)
          }
        }
    })
    return false;
  }
  // crear
  $(".show-form").click(MuestraFormulario);
  $("#modal-generic").on("submit",".create-form",GuardaFormulario)
  // actualizar
  $("#table_generic").on("click",".show-form-update",MuestraFormulario)
  $("#modal-generic").on("submit",".update-form",GuardaFormulario)

  // eliminar
  $("#table_generic").on("click",".show-form-delete",MuestraFormulario)
  $("#modal-generic").on("submit",".delete-form",GuardaFormulario)
});
