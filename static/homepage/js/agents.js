$(document).ready(function() {
    update_status();
});

function sync_status(id, val){
    // console.log(val)
    if (val == 1){
        $('#status-'+id).removeClass("bi-check-circle-fill");
        $('#status-'+id).removeClass("bi-x-circle-fill");
        $('#status-'+id).addClass("bi-check-circle-fill");
    }
    else {
        $('#status-'+id).removeClass("bi-check-circle-fill");
        $('#status-'+id).removeClass("bi-x-circle-fill"); 
        $('#status-'+id).addClass("bi-x-circle-fill");
    }
}

function sync_button(name, id, val){
    // console.log(val)
    if (val == 1){
        $('#'+name+'-'+id).prop('checked', true);
        $('#'+name+'-'+id).parent().removeClass('btn-danger off');
        $('#'+name+'-'+id).parent().addClass('btn-success')
        // console.log(id)
    }
    else {
        $('#'+name+'-'+id).prop('checked', false);
        $('#'+name+'-'+id).parent().removeClass('btn-success');
        $('#'+name+'-'+id).parent().addClass('btn-danger off');
    }
}


function sync_label(name,id,val){
    $('#'+name+'-'+id).empty();
    $('#'+name+'-'+id).append(val);
}

function sync_text(name, id, val){
    // console.log(val)
    $('#'+name+'-'+id).empty();
    $('#'+name+'-'+id).text(val);
    $('#'+name+'-'+id).val(val);
    // console.log(id)
}

function update_status(){
    var sync = function(){
        $.get('/agents/upstatus/',function(result,status){
        // console.log(result);
        // $('#loading').show();
        if (status == 'success'){
             $.each(result,function(index,dicts){
                 sync_status(dicts.id,dicts.status);
                 sync_button('monitor',dicts.id, dicts.ismonitor);
                 sync_button('video',dicts.id, dicts.vidmonitor);
                 sync_button('audio',dicts.id, dicts.audmonitor);
                 sync_button('signal',dicts.id, dicts.sigmonitor);
                 sync_label("ipcontrol",dicts.id, dicts.ip);
                 sync_text('location', dicts.id, dicts.location);
                 sync_text('thread', dicts.id, dicts.thread);
             });
        }
    });
    };
    setInterval(sync,10000);
    // setTimeout(sync, 2000);
}