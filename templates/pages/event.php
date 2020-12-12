<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Event</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Event</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmevent" name="frmevent" method="POST">
              <div class="form-group col-md-2">
                <select class="form-control" id="idServer" name="idServer">
                    <option value="0">--All--</option>
					<?php
						
						foreach($server as $value)
						{
							if($value["ServerIndex"]==$serverID)
								echo '<option selected value="'.$value["ServerIndex"].'">'.$value["server_name"].'</option>';
							else
								echo '<option value="'.$value["ServerIndex"].'">'.$value["server_name"].'</option>';
						}
					?>
                </select>
                </div>
				<div class="form-group col-md-2">
                <select class="form-control" id="event_id" name="event_id">
                    <option value="0">--All--</option>
					<?php
						
						foreach($events as $event)
						{
							if($event["Misc1"]==$event_id)
								echo '<option selected value="'.$event["Misc1"].'">'.$event["event_name"].'</option>';
							else
								echo '<option value="'.$event["Misc1"].'">'.$event["event_name"].'</option>';
						}
					?>
                </select>
                </div>
                <div class="form-group col-md-2">
                    <input <?php if($fromDate) echo 'value='.date("d-m-Y",strtotime($fromDate));?> class="form-control" id="fromDate" name="fromDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-2">
                    <input <?php if($toDate) echo 'value='.date("d-m-Y",strtotime($toDate));?> class="form-control" id="toDate" name="toDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="eventsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="eventexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
		
		<div class="col-md-5">
          <div class="tile">
		  <h2>TOP SERVER</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="payTable">
                <thead bgcolor="#009688">
                  <tr>
					<th>Server</th>
					<th>Total Users</th>
					<th>Total Gold</th>
                  </tr>
                </thead>
                <tbody>
                <?php
					
					if($topServer)
					{
						foreach($topServer as $value)
						{
							echo '<tr>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["total_user"].'</td>';
							echo '<td>'.$value["total"].'</td>';
							echo '</tr>';
						}
					}
				?>
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>
		
		<div class="col-md-7">
          <div class="tile">
		  <h2>TOP USER</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="userTable">
                <thead bgcolor="#009688">
                  <tr>
					<th>Server</th>
					<th>User</th>
					<th>PlayerName</th>
					<th>Level</th>
					<th>Total Gold</th>
                  </tr>
                </thead>
                <tbody>
                <?php
					
					if($topUser)
					{
						foreach($topUser as $value)
						{
							echo '<tr>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["PlayerID"].'</td>';
							echo '<td>'.$value["PlayerName"].'</td>';
							echo '<td>'.$value["level"].'</td>';
							echo '<td>'.$value["total"].'</td>';
							echo '</tr>';
							
						}
					}
				?>
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>
		
        <div class="col-md-12">
          <div class="tile">
		  <h2>ITEMS</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="dataTable">
                <thead bgcolor="#009688">
                  <tr>
					<th>ItemID</th>
					<th>ItemName</th>
					<th>ItemName(VN)</th>
					<th>Total Users</th>
					<th>Total</th>
                  </tr>
                </thead>
                <tbody>
                <?php
					
					if($items)
					{
						foreach($items as $value)
						{
							echo '<tr>';
							echo '<td>'.$value["TypeID"].'</td>';
							if(isset($value["item_name"])) $item_name = $value["item_name"]; else $item_name="";
							echo '<td>'.$item_name.'</td>';
							if(isset($value["name"])) $name = $value["name"]; else $name="";
							echo '<td>'.$name.'</td>';
							echo '<td>'.$value["total_user"].'</td>';
							echo '<td>'.$value["total"].'</td>';
							echo '</tr>';
						}
					}
				?>
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </main>
	
	
	<script>
		function eventsearch()
		{
			$('#frmevent').submit();
		}
		
		
		function eventexport()
		{
			alert("Update later, haha");
			//var serverID = document.getElementById("idServer").value;
			//var fromDate = document.getElementById("fromDate").value;
			
			//var DOMAIN = "https://po-ptm.mto.zing.vn/";
			//window.location.href= DOMAIN + "main/exporteventlevel?idServer="+serverID+"&fromDate=" + fromDate ;
		}
		
		
	</script>