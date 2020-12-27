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

function sync_vidstatus(id, val){
    // console.log(val)
    if (val == 1){
        $('#vidstatus-'+id).removeClass("bi-check-circle-fill");
        $('#vidstatus-'+id).removeClass("bi-x-circle-fill");
        $('#vidstatus-'+id).addClass("bi-check-circle-fill");
        // console.log(id)
    }
    else {
        $('#vidstatus-'+id).removeClass("bi-check-circle-fill");
        $('#vidstatus-'+id).removeClass("bi-x-circle-fill"); 
        $('#vidstatus-'+id).addClass("bi-x-circle-fill");
    }
}

function sync_audstatus(id, val){
    // console.log(val)
    if (val == 1){
        $('#audstatus-'+id).removeClass("bi-check-circle-fill");
        $('#audstatus-'+id).removeClass("bi-x-circle-fill");
        $('#audstatus-'+id).addClass("bi-check-circle-fill");
        // console.log(id)
    }
    else {
        $('#audstatus-'+id).removeClass("bi-check-circle-fill");
        $('#audstatus-'+id).removeClass("bi-x-circle-fill"); 
        $('#audstatus-'+id).addClass("bi-x-circle-fill");
    }
}

function sync_isenable(id, val){
    // console.log(val)
    if (val == 1){
        $('#isenable-'+id).removeClass("bi-check-circle-fill");
        $('#isenable-'+id).removeClass("bi-x-circle-fill");
        $('#isenable-'+id).addClass("bi-check-circle-fill");
        // console.log(id)
    }
    else {
        $('#isenable-'+id).removeClass("bi-check-circle-fill");
        $('#isenable-'+id).removeClass("bi-x-circle-fill"); 
        $('#isenable-'+id).addClass("bi-x-circle-fill");
    }
}

function sync_sigmonitor(id, val){
    // console.log(val)
    if (val == 1){
        $('#sigmonitor-'+id).removeClass("bi-toggle-off");
        $('#sigmonitor-'+id).removeClass("bi-toggle-on");
        $('#sigmonitor-'+id).addClass("bi-toggle-on");
        // console.log(id)
    }
    else {
        $('#sigmonitor-'+id).removeClass("bi-toggle-off");
        $('#sigmonitor-'+id).removeClass("bi-toggle-on"); 
        $('#sigmonitor-'+id).addClass("bi-toggle-off");
    }
}

function sync_vidmonitor(id, val){
    // console.log(val)
    if (val == 1){
        $('#vidmonitor-'+id).removeClass("bi-toggle-off");
        $('#vidmonitor-'+id).removeClass("bi-toggle-on");
        $('#vidmonitor-'+id).addClass("bi-toggle-on");
        // console.log(id)
    }
    else {
        $('#vidmonitor-'+id).removeClass("bi-toggle-off");
        $('#vidmonitor-'+id).removeClass("bi-toggle-on"); 
        $('#vidmonitor-'+id).addClass("bi-toggle-off");
    }
}

function sync_audmonitor(id, val){
    // console.log(val)
    if (val == 1){
        $('#audmonitor-'+id).removeClass("bi-toggle-off");
        $('#audmonitor-'+id).removeClass("bi-toggle-on");
        $('#audmonitor-'+id).addClass("bi-toggle-on");
        // console.log(id)
    }
    else {
        $('#audmonitor-'+id).removeClass("bi-toggle-off");
        $('#audmonitor-'+id).removeClass("bi-toggle-on"); 
        $('#audmonitor-'+id).addClass("bi-toggle-off");
    }
}

function sycn_label(name,id,val){
    $('#'+name+'-'+id).empty();
    $('#'+name+'-'+id).append(val);
}

function update_status(){
    var sync = function(){
        $.get('/monitor/upstatus/',function(result,status){
        console.log(result);
        if (status == 'success'){
             $.each(result,function(index,dicts){
                 sync_status(dicts.id,dicts.status);
                 sync_vidstatus(dicts.id, dicts.vidstatus);
                 sync_vidmonitor(dicts.id,dicts.vidmonitor);
                 sync_audmonitor(dicts.id, dicts.audmonitor);
                 sync_audstatus(dicts.id, dicts.audstatus);
                 sync_sigmonitor(dicts.id, dicts.sigmonitor);
                 sync_isenable(dicts.id, dicts.isenable);
                 sycn_label("location",dicts.id, dicts.location);
                 sycn_label("ipmulticast",dicts.id, dicts.mulip);
                 sycn_label("channle",dicts.id, dicts.channel);
                 sycn_label("profle",dicts.id, dicts.quality);
             });
        }
    });
    };
    setInterval(sync,10000);
    // setTimeout(sync, 2000);
}