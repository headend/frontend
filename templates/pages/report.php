<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Report</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Report</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmreport" name="frmreport" method="POST">
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
                    <input <?php if($fromDate) echo 'value='.date("d-m-Y",strtotime($fromDate));?> class="form-control" id="fromDate" name="fromDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-2">
                    <input <?php if($toDate) echo 'value='.date("d-m-Y",strtotime($toDate));?> class="form-control" id="toDate" name="toDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="dataTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
                    <th>NRU</th>
                    <th>A1</th>
                    <th>A3</th>
                    <th>A7</th>
                    <th>REV</th>
                    <th>PU</th>
                    <th>PU3</th>
                    <th>PU7</th>
                    <th>ACU</th>
                    <th>PCU</th>
                  </tr>
                </thead>
                <tbody>
                <?php
				
					if($report)
					{
						foreach($report as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["nru"].'</td>';
							echo '<td>'.$value["a1"].'</td>';
							echo '<td>'.$value["a3"].'</td>';
							echo '<td>'.$value["a7"].'</td>';
							echo '<td>'.number_format($value["rev"]).'</td>';
							echo '<td>'.$value["pu"].'</td>';
							echo '<td>'.$value["pu3"].'</td>';
							echo '<td>'.$value["pu7"].'</td>';
							echo '<td>'.$value["acu"].'</td>';
							echo '<td>'.$value["pcu"].'</td>';
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
		function reportsearch()
		{
			$('#frmreport').submit();
		}
		
		
		
		function reportexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var toDate = document.getElementById("toDate").value;
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exportreport?idServer="+serverID+"&fromDate=" + fromDate + "&toDate=" + toDate;
		}
		
	</script>