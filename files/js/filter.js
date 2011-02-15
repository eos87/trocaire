var url = window.location.href.split('/');

$(document).ready(function(){
    clean();
    $('#id_pais').change(function(){
        cleanAll();
        checkDep();
    });
    $('#id_departamento').change(function(){
        checkMuni();
    });
});

function checkDep(){    
    var selected = $('#id_pais').val();
    $.getJSON('/ajax/depa/?id='+selected, function(data){               
        if(data){
            $('#id_departamento').html('');
            $('#id_departamento').append($('<option></option>').html('Seleccione...'));
            $.each(data, function(i, item){
                $('#id_departamento').append($('<option></option>').val(item.id).html(item.nombre));
            });
        }

    });
}

function checkMuni(){    
    var selected = $('#id_departamento').val();
    $.getJSON('/ajax/muni/?id='+selected, function(data){
        $('#id_municipio').html('');
        if(data){
            $('#id_municipio').append($('<option></option>').html('Seleccione...'));
            $.each(data, function(i, item){
                $('#id_municipio').append($('<option></option>').val(item.id).html(item.nombre));
            });
        }
    });
}

function cleanAll(){    
    $('#id_municipio').html('');
    $('#id_municipio').append($('<option></option>').html('---------'));
}

function clean(){
    if (url[url.length-2]=="add"){
        $('#id_departamento').html('');
        $('#id_departamento').append($('<option></option>').html('---------'));
        $('#id_municipio').html('');
        $('#id_municipio').append($('<option></option>').html('---------'));
    }else{
        checkDep();
        checkMuni();
        $.getJSON('/ajax/data/?id='+url[url.length-2], function(data){
            if(data){
                $("#id_departamento option[value='"+data[0]+"']").attr('selected', 'selected');
                $("#id_municipio option[value='"+data[1]+"']").attr('selected', 'selected');
            }
        });
    }
}