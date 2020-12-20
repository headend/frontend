 $(document).ready(function() {
	$('#newDate').datetimepicker({
    format: 'YYYY-MM-DD HH:MM',
    formatTime: 'HH:mm',
    lang: 'en',
  });

  $.datetimepicker.setDateFormatter({
    // parseDate: function(date, format) {
    //   var d = moment(date, format);
    //   return d.isValid();
    // },
    formatDate: function(date, format) {
      return moment(date).format(format);
    },
  });

  $('#loading').hide();
});

function get_timestamp() {
  // body...
  return Math.floor(new Date().getTime()/1000.0)
}
function execute_update_agent(){

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
    "monitor": $('#monitor-'+select_id).prop("checked") ? 1 : 0,
    "alarm": $('#alarm-'+select_id).prop("checked") ? 1 : 0,
    "signal": $('#signal-'+select_id).prop("checked") ? 1 : 0,
    "video": $('#video-'+select_id).prop("checked") ? 1 : 0,
    "audio": $('#audio-'+select_id).prop("checked") ? 1 : 0,
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
      alert(result);
      location.reload();
    });  
  }
  else {
    var txt = "Cancel";
    $('#loading').hide();
    alert(txt);
  }
}

function changeDatetime(sync) {
	var data;
	if (sync == true) {
		data = {
			'sync': 1
		}
	} else {
		newDatetime = document.getElementById("newDate").value;
		console.log(newDatetime);
		var ts = get_timestamp()
	  data = {
	  	'sync': 0,
	    'new_datetime': newDatetime,
	    'ts': ts
	  }
	}
  $('#loading').show();
  $.post("/servers/datetime/", data, function(result){
    $('#loading').hide();
    alert(result);
    location.reload();
  });
}

function uploadCDN(select_obj) {
  var env = select_obj.name;
  var name = select_obj.id;
    var ts = get_timestamp()
    data = {
      'env': env,
      'name': name,
      'ts': ts
    }
    $('#loading').show();
    $.post("/patch/resource/", data, function(result){
      $('#loading').hide();
      alert(result);
      window.open('/', '_blank');
      //location.reload();
    });
}
function resourceApply(select_obj) {
  var env = select_obj.name;
  var name = select_obj.id;
    var ts = get_timestamp()
    data = {
      'env': env,
      'name': name,
      'ts': ts
    }
    if (env == 'real') {
      if (confirm("Đây là môi trường PRODUCTON, có chắc chắn áp dụng update này???</br> Nhớ tạo CHANGE tại https://itsmv2.vng.com.vn/change trước khi thực hiện nhé!")){
        $('#loading').show();
        $.post("/patch/resource/apply/", data, function(result){
          $('#loading').hide();
          alert(result);
          window.open('/', '_blank');
          // location.reload();
        });
      } else {
        txt = "Thao tác đã hủy";
        alert(txt);
      }
    } else {
      $('#loading').show();
      $.post("/patch/resource/apply/", data, function(result){
        $('#loading').hide();
        alert(result);
        window.open('/', '_blank');
        // location.reload();
      });
  }
}

function patchServerApply(select_obj) {
  var env = select_obj.name;
  var name = select_obj.id;
  var ts = get_timestamp()
  data = {
    'env': env,
    'name': name,
    'ts': ts
  }
  if (env == 'real') {
    if (confirm("Đây là môi trường production, thao tác này sẽ restart server game disconnect tất cả user! </br> Nhớ tạo CHANGE tại https://itsmv2.vng.com.vn/change trước khi thực hiện nhé!")) {
      $('#loading').show();
      $.post("/patch/", data, function(result){
        $('#loading').hide();
        alert(result);
        window.open('/', '_blank');
        // location.reload();
      });
    }
    else {
      alert("Yêu cầu update server đã được hủy!")
    }
  } else {
    $('#loading').show();
    $.post("/patch/", data, function(result){
      $('#loading').hide();
      alert(result);
      window.open('/', '_blank');
      // location.reload();
    });
 }
}

function uploadFileSubmitCheck(){
    var errors = "";
    var input_file = $("#files");
    var files = input_file.prop("files")
    var names = $.map(files, function (val) { return val.name; });
    var count=0;
    $.each(names, function (i, name) {
        // Check space
        if (name.indexOf(' ') >= 0){
            errors += "\n" + " Tên file không được chứa khoảng trắng: " + name;
        }
        // check zip, tar.gz file
        if (name.endsWith(".tar.gz") == false && name.endsWith(".zip") == false) {
            errors += "\n" + " Vui lòng upload file ZIP, TAR.GZ ";
        }
        // check unicode
        for (var i = 0; i < name.length; i++) {
            if(name.charCodeAt(i) > 127) {
                errors += "\n" + "Tên file không được chứa ký tự đặc biệt, dấu tiếng Vệt: " + name;
                break;
            }
        }
        count +=1;
    });
    if (count == 0){
        errors += "\n" + "Vui lòng chọn file upload. ";
    }
    if (errors.length > 1) {
        alert(errors);
        return false;
    }
    $('#loading').show();
    document.form.submit();
    $('#loading').hide();
};


function changeState(select_obj) {
  var sid = select_obj.name;
  var status = select_obj.value;
  var ts = get_timestamp()
  if (confirm("Thay đổi trạng thái server " + sid + " thành: " + status + " ?")) {
    location.href="/servers/status/change/?sid=" + sid + "&status=" + status + "&ts=" + ts;
  } else {
    txt = "You pressed cancel!";
  }
}

function serverSearch(){
    var version = document.getElementById("versionServer").value;
    var status = document.getElementById("statusServer").value;
    var ts = get_timestamp()
    window.location.href= "/servers/filter/?version="+version+"&status=" + status + "&ts=" + ts;
}

function execute_action_control_v1(sid, action, host){
  if (confirm("Bạn có chắc " + action + " server khu " + sid + " ?")) {
    var ts = get_timestamp()
    location.href="/servers/control/?sid=" + sid + "&action=" + action + "&host=" + host +  "&ts=" + ts;
  } else {
    txt = "You pressed cancel!";
  }
}

function execute_action_control_v2(sid, action, host){
  if (confirm("Bạn có chắc " + action + " server khu " + sid + " ?")) {
    var ts = get_timestamp()
    data = {
      'sid': sid,
      'action': action,
      'host': host,
      'ts': ts
    }
    $('#loading').show();
    $.post("/servers/control/", data, function(result){
      $('#loading').hide();
      alert(result);
      location.reload();
    });
  } else {
    txt = "You pressed cancel!";
  }
}

function serverControl(select_obj) {
  // console.log(select_obj)
  var selected_sid = select_obj.id;
  var action_host = select_obj.name;
  var action_host_arr = action_host.split("_");
  var selected_action = action_host_arr[0];
  var selected_host = action_host_arr[1];
  return execute_action_control_v2(selected_sid, selected_action, selected_host); 
}

function execute_action_ctl_register_v1(sid, choose) {
  // body...
  if (confirm("Bạn có chắc " + choose + " REGISTER server khu " + sid + " ?")) {
    var ts = get_timestamp()
    location.href="/servers/registerctl/?sid=" + sid + "&choose=" + choose + "&ts=" + ts;
  } else {
    txt = "You pressed cancel!";
  }    
}

function execute_action_ctl_register_v2(sid, choose) {
  // body...
  if (confirm("Bạn có chắc " + choose + " REGISTER server khu " + sid + " ?")) {
    var ts = get_timestamp()
    data = {
      'sid': sid,
      'choose': choose,
      'ts': ts
    }
    $('#loading').show();
    $.post("/servers/registerctl/", data, function(result){
      $('#loading').hide();
      alert(result);
      location.reload();
    });
  } else {
    txt = "You pressed cancel!";
  }    
}


function serverControlRegister(select_obj) {
  var selectted_sid = select_obj.id;
  var selectted_choose = select_obj.name;
  return execute_action_ctl_register_v2(selectted_sid, selectted_choose);
}


function removeIP(select_obj) {
  var oldip = select_obj.name;
  if (confirm("Bạn có chắc xóa ip " + oldip + " khỏi whitelist???")){
    var ts = get_timestamp()
    location.href="/servers/whitelist/remove/" + oldip + "/?ts=" + ts;
  } else {
    txt = "You pressed Cancel!";
  }
  // console.log(select_obj);
}

function ValidateIPaddress(ipaddress) 
{
 if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress))
  {
    return (true)
  }
  alert("Bạn cần nhập vào ip v4!")
  return (false)
}
function addWhitelist(){
  var newip = $('#newip').val();
  var ts = get_timestamp()
  if (ValidateIPaddress(newip)) {
    location.href="/servers/whitelist/add/" + newip + "/?ts=" + ts;
  }
}
