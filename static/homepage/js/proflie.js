$(document).ready(function() {
    loadForeignKey();
});
function loadSelectQuality(lstValuses){
    $.each(lstValuses, function(index,values){
        // console.log(values.id);
        $('#frm-add-quality').prop('selectedIndex',0);
        if($('#frm-add-quality').find("option[value='"+values.id+"']").length){
            $('#frm-add-quality').trigger('change');
         }else{ 
             $('#frm-add-quality').append($('<option>', {
                 value:values.id,
                 text: values.quality,
             }));
             $('#frm-add-quality').trigger('change');
        }
         console.log($('#frm-add-quality').val());
    });
}
function loadSelectChannle(lstValuses){
    $.each(lstValuses, function(index,values){
        // console.log(values.id);
        $('#frm-add-channel').prop('selectedIndex',0);
        if($('#frm-add-channel').find("option[value='"+values.id+"']").length){
            $('#frm-add-channel').trigger('change');
         }else{ 
             $('#frm-add-channel').append($('<option>', {
                 value:values.id,
                 text: values.name,
             }));
             $('#frm-add-channel').trigger('change');
        }
         console.log($('#frm-add-channel').val());
    });
}
function loadSelectVlan(lstValuses){
    $.each(lstValuses, function(index,values){
        // console.log(values.id);
        $('#frm-add-vlan').prop('selectedIndex',0);
        if($('#frm-add-vlan').find("option[value='"+values.id+"']").length){
            $('#frm-add-vlan').trigger('change');
         }else{ 
             $('#frm-add-vlan').append($('<option>', {
                 value:values.id,
                 text: values.vlanid,
             }));
             $('#frm-add-vlan').trigger('change');
        }
         // console.log($('#frm-add-vlan').val());
    });
}
function loadSelectMulticast(lstValuses){
    $.each(lstValuses, function(index,values){
        // console.log(values.id);
        $('#frm-add-mulip').prop('selectedIndex',0);
        if($('#frm-add-mulip').find("option[value='"+values.id+"']").length){
            $('#frm-add-mulip').trigger('change');
         }else{ 
             $('#frm-add-mulip').append($('<option>', {
                 value:values.id,
                 text: values.ip,
             }));
             $('#frm-add-mulip').trigger('change');
        }
         // console.log($('#frm-add-mulip').val());
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
function loadSelectEncoder(lstValuses){
    $.each(lstValuses, function(index,values){
        console.log(values.id);
        $('#frm-add-encoder').prop('selectedIndex',0);
        if($('#frm-add-encoder').find("option[value='"+values.state+"']").length){
            $('#frm-add-encoder').trigger('change');
         }else{
             $('#frm-add-encoder').append($('<option>', {
                 value:values.id,
                 text: values.name,
             }));
             $('#frm-add-encoder').trigger('change');
        }
    });
}
function loadForeignKey(){
    $.get("/profile/get4create/", function(result, status){
        // console.log(status);
      }).done(function(result){
        console.log(result.Encoder);
        loadSelectChannle(result.Channel);
        loadSelectQuality(result.Quality);
        loadSelectMulticast(result.MulCastIp);
        loadSelectVlan(result.Vlan);
        loadSelectStatus(result.State);
        loadSelectEncoder(result.Encoder);
      }).fail(function(result, textStatus, xhr){
        console.log(result.status, textStatus, xhr);
      }); 
    // loadDataSelect("frm-add-vlan");
}

 $('#btnnewprofile-form-submit').on('click',function(e) {
     frmdata= {
         "quality": $('#frm-add-quality').val(),
         'channel': $('#frm-add-channel').val(),
         'mulcast': $('#frm-add-mulip').val(),
         'vlan': $('#frm-add-vlan').val(),
         'status': $('#frm-add-status').val(),
         'encoder': $('#frm-add-encoder').val(),
         'desc': $('#frm-add-desc').val(),
     };
     e.preventDefault();
     $.post('/profile/newprofile/', frmdata, function(reult){
         console.log(reult);
     }).fail(function (resulf,msg,xhr){
         console.log(resulf.responseText, msg, xhr);
     });
    console.log(frmdata);
});