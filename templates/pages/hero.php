<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Hero</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Hero</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmhero" name="frmhero" method="POST">
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
                  <button class="btn btn-primary" type="button" onclick="herosearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="hreoexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
		  <h2>Tướng Sinh Ra</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="dataTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
					<th>ID Tướng</th>
                    <th>Tướng</th>
                    <th>Số lượng</th>
                    <th>CmdID</th>                    
                    <th>Nguồn ra</th>                    
                  </tr>
                </thead>
                <tbody>
                  <?php
					//print_r($arrHero);exit;
					if($arrHeroAdd)
					{
						foreach($arrHeroAdd as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["TypeID"].'</td>';
							if(isset($value["vn_name"])){ $name =$value["vn_name"];}else {$name = $value["TypeID"];}
							echo '<td>'.$name.'</td>';
							echo '<td>'.$value["total"].'</td>';
							echo '<td>'.$value["CmdID"].'</td>';
							if(isset($value["name"])){ $item =$value["name"];}else {$item = $value["CmdID"];}
							echo '<td>'.$item.'</td>';
							echo '</tr>';
						}
					}
				?>
				  
				  
                </tbody>
              </table>
            </div>
          </div>
        </div>
		
		
		 <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
		  <h2>Tướng Tiêu Hao</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="payTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
					<th>ID Tướng</th>
                    <th>Tướng</th>
                    <th>Số lượng</th>
                    <th>CmdID</th>                    
                    <th>Nguồn ra</th>                    
                  </tr>
                </thead>
                <tbody>
                  <?php
					//print_r($arrHero);exit;
					if($arrHeroDel)
					{
						foreach($arrHeroDel as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.$value["TypeID"].'</td>';
							if(isset($value["vn_name"])){ $name =$value["vn_name"];}else {$name = $value["TypeID"];}
							echo '<td>'.$name.'</td>';
							echo '<td>'.$value["total"].'</td>';
							echo '<td>'.$value["CmdID"].'</td>';
							if(isset($value["name"])){ $item =$value["name"];}else {$item = $value["CmdID"];}
							echo '<td>'.$item.'</td>';
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
		function herosearch()
		{
			$('#frmhero').submit();
		}
		
		function hreoexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var toDate = document.getElementById("toDate").value;
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exporthero?idServer="+serverID+"&fromDate=" + fromDate + "&toDate=" + toDate;
		}
		
		
		
		
	</script>