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
              <form class="row" id="frmreportnew" name="frmreportnew" method="POST">
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
                  <button class="btn btn-primary" type="button" onclick="reportnewsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportnewexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="dataTable">
                <thead bgcolor="#FDB45C">
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
                    <th>NRU_O</th>
                    <th >NRU_N</th>
                    <th>A1_O</th>
                    <th >A1_N</th>
                    <th>A3_O</th>
                    <th >A3_N</th>
                    <th>A7_O</th>
                    <th >A7_N</th>
                    <th>REV_O</th>
                    <th >REV_N</th>
                    <th>PU_O</th>
                    <th >PU_N</th>
                    <th>PU3_O</th>
                    <th >PU3_N</th>
                    <th>PU7_O</th>
                    <th >PU7_N</th>
                    
                  </tr>
                </thead>
                <tbody>
                <?php
				
					if($reportnew)
					{
						foreach($reportnew as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["nru"].'</td>';
							echo '<td bgcolor="#009688">'.$value["nru_n"].'</td>';
							echo '<td>'.$value["a1"].'</td>';
							echo '<td bgcolor="#009688">'.$value["a1_n"].'</td>';
							echo '<td>'.$value["a3"].'</td>';
							echo '<td bgcolor="#009688">'.$value["a3_n"].'</td>';
							echo '<td>'.$value["a7"].'</td>';
							echo '<td bgcolor="#009688">'.$value["a7_n"].'</td>';
							echo '<td>'.number_format($value["rev"]).'</td>';
							echo '<td bgcolor="#009688">'.number_format($value["rev_n"]).'</td>';
							echo '<td>'.$value["pu"].'</td>';
							echo '<td bgcolor="#009688">'.$value["pu_n"].'</td>';
							echo '<td>'.$value["pu3"].'</td>';
							echo '<td bgcolor="#009688">'.$value["pu3_n"].'</td>';
							echo '<td>'.$value["pu7"].'</td>';
							echo '<td bgcolor="#009688">'.$value["pu7_n"].'</td>';
							
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
		function reportnewsearch()
		{
			$('#frmreportnew').submit();
		}
		
		
		
		function reportnewexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var toDate = document.getElementById("toDate").value;
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exportreportnew?idServer="+serverID+"&fromDate=" + fromDate + "&toDate=" + toDate;
		}
		
	</script>