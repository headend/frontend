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
    // console.log(name+id+"-"+val);
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
                 sync_label("id",dicts.id, dicts.id);
                 sync_text('location', dicts.id, dicts.location);
                 sync_text('thread', dicts.id, dicts.thread);
                 sync_label("downtime",dicts.id, dicts.downtime);
                 sync_label("version",dicts.id, dicts.version);
             });
        }
    });
    };
    // setInterval(sync,10000);
    // setTimeout(sync, 2000);
}
function getAgentColumn(select_id) {
  data = {
    "id": select_id,
    "ip_control": $('#ipcontrol-'+select_id).text(),
    "ip_receive_multicast": $('#ipmulticast-'+select_id).text(),
    "cpu": $('#cpu-'+select_id).text(),
    "ram": $('#ram-'+select_id).text(),
    "disk": $('#disk-'+select_id).text(),
    "location": $('#location-'+select_id).val(),
    "monitor": $('#monitor-'+select_id).is(":checked") ? 1 : 0,
    "status": $('#status-'+select_id).is(":checked") ? 1 : 0,
    "alarm": $('#alarm-'+select_id).is(":checked") ? 1 : 0,
    "signal": $('#signal-'+select_id).is(":checked") ? 1 : 0,
    "video": $('#video-'+select_id).is(":checked") ? 1 : 0,
    "audio": $('#audio-'+select_id).is(":checked") ? 1 : 0,
    "thread": $('#thread-'+select_id).val(),
  };
  console.log(data);
  return data;
}

function getAgentColumn(select_id) {
  data = {
    "id": select_id,
    "ip_control": $('#ipcontrol-'+select_id).text(),
    "ip_receive_multicast": $('#ipmulticast-'+select_id).text(),
    "cpu": $('#cpu-'+select_id).text(),
    "ram": $('#ram-'+select_id).text(),
    "disk": $('#disk-'+select_id).text(),
    "location": $('#location-'+select_id).val(),
    "monitor": $('#monitor-'+select_id).is(":checked") ? 1 : 0,
    "status": $('#status-'+select_id).is(":checked") ? 1 : 0,
    "alarm": $('#alarm-'+select_id).is(":checked") ? 1 : 0,
    "signal": $('#signal-'+select_id).is(":checked") ? 1 : 0,
    "video": $('#video-'+select_id).is(":checked") ? 1 : 0,
    "audio": $('#audio-'+select_id).is(":checked") ? 1 : 0,
    "thread": $('#thread-'+select_id).val(),
  };
  console.log(data);
  return data;
}

function onChangeCheckBox(select_obj) {
  var tmp = $('#'+select_obj).is(":checked");
  $('#'+select_obj).prop('checked', tmp);
}

function agentUpdate(select_obj) {
  data = getAgentColumn(select_obj);
  $('#loading').show();
  if (confirm("You update this agent?")){
    $.post("/agents/update/", data, function(result){
      $('#loading').hide();
      msg = "Monitor:\t"+ result.monitor.msg+"\n"+"Signal:\t"+result.signal.msg+"\nVideo:\t"+result.video.msg+"\nAudio:\t"+result.audio.msg;
      alert(msg);
      console.log(result);
      location.reload();
    }).fail(function(){
      $('#loading').hide();
      alert("Not connect to server")
    });
  }
  else {
    var txt = "Cancel";
    $('#loading').hide();
    alert(txt);
  }
}

function agentDete(select_obj) {
  $('#loading').show();
  if (confirm("You delelte this agent: "+select_obj)){
      $.ajax({
        url:"/agents/delete/"+select_obj,
        method: 'DELETE',
        contentType: 'application/json',
        success: function(result,status) {
            // handle success
            console.log(status);
            alert(status);
            $('#loading').hide();
            location.reload();
        },
        error: function(request,msg,error) {
            // handle failure
            alert(msg);
            $('#loading').hide();
        }
    });
  }
}