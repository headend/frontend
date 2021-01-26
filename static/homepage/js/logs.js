$(document).ready(function (){

});

function logSearch(){
    channle=$('#channels').val();
    agent = $('#agents').val();
    multiip = $('#mips').val();
    console.log("channel: "+ channle+"agent: "+agent+"muips: "+multiip);
    loadDataLogs()
}


function addNewRow(id, agent, channel, multicast, before_status, after_status, desc, date_create, distance){
  $('#tblogs').append($('<tr>')
     .append($('<td>')
         .append($('<label>').attr('id','agentid-'+id).attr('name','agentid-'+id).text(agent)))
     .append($('<td>')
         .append($('<label>').attr('id', 'channelname-'+id).attr('name', 'channelname-'+id).text(channel)))
     .append($('<td>')
         .append($('<label>').attr('id', 'multicastip-'+id).attr('name', 'multicastip-'+id).text(multicast)))
     .append($('<td>')
         .append($('<label>').attr('id', 'beforestatus-'+id).attr('name', 'beforestatus-'+id).text(before_status)))
     .append($('<td>')
         .append($('<div>').attr('class', 'content_center')
             .append($('<i>').attr('id','status-'+id))))
     .append($('<td>')
         .append($('<label>').attr('id', 'desc-'+id).attr('name', 'desc-'+id).text(desc)))
     .append($('<td>')
         .append($('<label>').attr('id', 'datecreate-'+id).attr('name', 'datecreate-'+id).text(date_create)))
     .append($('<td>')
         .append($('<label>').attr('id', 'distance-'+id).attr('name', 'distance-'+id).text(distance)))
  );
  if (after_status == 1){
      $('status-'+id).removeAttr('class');
      $('#status-'+id).addClass('bi-check-circle-fill');
  }else {
      $('status-'+id).removeAttr('class');
      $('#status-'+id).addClass('bi-x-circle-fill');
  }

}
function loadDataLogs(){
    $("#tblogs").empty();
    console.log("loaddata...");
    addNewRow(1,'HCM','VTV3HD','255.255.1.1','ok',1,'123','','');
    addNewRow(2,'HCM','VTV3HD','255.255.1.1','ok',0,'123','','');
}