<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Top Level - Guild</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Top</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmreport" name="frmreport" method="POST">
              <div class="form-group col-md-3">
                <select class="form-control" id="idServer" name="idServer">
                    <!--<option value="0">--All--</option>-->
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
                <div class="form-group col-md-3">
                    <input <?php if($fromDate) echo 'value='.date("d-m-Y",strtotime($fromDate));?> class="form-control" id="fromDate" name="fromDate" type="text" placeholder="Select Date">
                </div>
                
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="topreportsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="topreportexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
		  <h2>Top Guild</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="dataTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
                    <th>Rank</th>
                    <th>Guild</th>
                    <th>Guild Master</th>
                    <th>Guild Score</th>
                    
                  </tr>
                </thead>
                <tbody>
                <?php
				
					if($topguild)
					{
						foreach($topguild as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["rank"].'</td>';
							echo '<td>'.$value["name"].'</td>';
							echo '<td>'.$value["master_id"].'</td>';
							echo '<td>'.$value["score"].'</td>';
							
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
			<h2>Top Level</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="paymentTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
                    <th>Rank</th>
                    <th>PlayerID</th>
                    <th>Name</th>
                    <th>Level</th>
                  </tr>
                </thead>
                <tbody>
                <?php
					//print_r($arrSpent);exit;
					if($toplevel)
					{
						foreach($toplevel as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["rank"].'</td>';
							echo '<td>'.$value["PlayerID"].'</td>';
							echo '<td>'.$value["PlayerID"].'</td>';
							echo '<td>'.$value["Level"].'</td>';
							
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
		function topreportsearch()
		{
			$('#frmreport').submit();
		}
		
		
		
		function topreportexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exporttoplevelguild?idServer="+serverID+"&fromDate=" + fromDate;
		}
		
	</script>