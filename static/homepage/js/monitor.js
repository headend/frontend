$(document).ready(function() {
    update_status();
    loadForeignKey();
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
        // $('#loading').show();
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

function loadSelectProfile(lstValuses){
    $.each(lstValuses, function(index,values){
        $('#frm-add-profile').prop('selectedIndex',0);
        if($('#frm-add-profile').find("option[value='"+values.state+"']").length){
            $('#frm-add-profile').trigger('change');
         }else{
             $('#frm-add-profile').append($('<option>', {
                 value:values.id,
                 text: values.channelname+'-'+values.quality,
             }));
             $('#frm-add-profile').trigger('change');
        }
         // console.log($('#frm-add-status').val());
    });
}
function loadSelectAgent(lstValuses){
    $.each(lstValuses, function(index,values){
        $('#frm-add-agent').prop('selectedIndex',0);
        if($('#frm-add-agent').find("option[value='"+values.state+"']").length){
            $('#frm-add-agent').trigger('change');
         }else{
             $('#frm-add-agent').append($('<option>', {
                 value:values.id,
                 text: values.location+'-'+values.ip,
             }));
             $('#frm-add-agent').trigger('change');
        }
         // console.log($('#frm-add-status').val());
    });
}
function loadSelectStatus(lstValuses){
    $.each(lstValuses, function(index,values){
        $('#frm-add-status').prop('selectedIndex',0);
        if($('#frm-add-status').find("option[value='"+values.state+"']").length){
            $('#frm-add-status').trigger('change');
         }else{
             $('#frm-add-status').append($('<option>', {
                 value:values.state,
                 text: values.name,
             }));
             $('#frm-add-status').trigger('change');
        }
         // console.log($('#frm-add-status').val());
    });
}
function loadForeignKey(){
    $.get("/monitor/get4create/", function(result, status){
        // console.log(status);
      }).done(function(result){
          loadSelectProfile(result.Profile);
          loadSelectAgent(result.Agent);
          loadSelectStatus(result.Status);
      }).fail(function(result, textStatus, xhr){
        console.log(result.status, textStatus, xhr);
      });
    // loadDataSelect("frm-add-vlan");
}
function showModalMsg(msg, cls){
    $('#lbl-message').removeAttr('class');
    $('#lbl-message').addClass(cls);
    $('#lbl-message').text(msg);
    $('#msgModal').modal('toggle');
}
$("#btnnewmontior-form-submit").click(function (e){
    frmdata = {
        "profile": $('#frm-add-profile').val(),
        "agent": $('#frm-add-agent').val(),
        "status": $('#frm-add-status').val(),
        "enable": $('#chkEnable').prop("checked")?1:0,
        "video": $('#chkVideo').prop("checked")?1:0,
        "audio": $('#chkAudio').prop("checked")?1:0,
        "signal": $('#chkSignal').prop("checked")?1:0,
    };
    e.preventDefault();
    console.log(frmdata);
    $.post('/monitor/newmonitor/', frmdata, function(reult){
         console.log(reult);
         showModalMsg("Success!", "text-success");
         $('#msgModal .closed').click(function (e){
             e.preventDefault();
             location.reload();
         });
     }).fail(function (resulf,msg,xhr){
         console.log(resulf.responseText);
         showModalMsg(resulf.responseText, "text-danger");
         // $('#msgModal').modal('toggle');
     });
});
function deleteMonitor(select_obj) {
  $('#loading').show();
  if (confirm("You delelte this profile: "+select_obj)){
      $.ajax({
        url:"/monitor/delete/"+select_obj,
        method: 'DELETE',
        contentType: 'application/json',
        success: function(result,status) {
            // handle success
            console.log(status);
            // alert(status);
            showModalMsg(msg=result.responseText,'text-success')
            $('#msgModal .closed').click(function (e){
             e.preventDefault();
             location.reload();
             });
            $('#loading').hide();
        },
        error: function(request,status,error) {
            // handle failure
            // alert(msg);
            showModalMsg(msg=request.responseText,'text-danger')
            $('#loading').hide();
        }
    });
      $('#msgModal .close').click(function (e){
          e.preventDefault();
          location.reload();
      });
  }else{
      $('#loading').hide();
  }
}