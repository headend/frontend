<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Report Level</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Report Level</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmreport" name="frmreport" method="POST">
              <div class="form-group col-md-3">
                <select class="form-control" id="idServer" name="idServer">
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
				
				<div class="form-group col-md-1">
                    <input class="form-control" id="ilevel" name="ilevel" type="number" placeholder="Level">
                </div>
                
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportlevelsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportlevelexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
				<div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="reportlevelexportdetail()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export Detail</button>
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
                    <th>Level</th>
                    <th>Count</th>
                    
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
							echo '<td>'.$value["LEVEL"].'</td>';
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
		function reportlevelsearch()
		{
			$('#frmreport').submit();
		}
		
		
		function reportlevelexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exportreportlevel?idServer="+serverID+"&fromDate=" + fromDate ;
		}
		
		function reportlevelexportdetail()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var level = document.getElementById("ilevel").value;
			
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exportreportleveldetail?idServer="+serverID+"&fromDate=" + fromDate +"&ilevel=" + level;
		}
		
	</script>