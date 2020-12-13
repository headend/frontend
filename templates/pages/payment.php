<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Payment</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Payment</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row" id="frmpayment" name="frmpayment" method="POST" action="payment">
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
                  <button class="btn btn-primary" type="button" onclick="paymentsearch()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-3 align-self-end">
                  <button class="btn btn-primary" type="button" onclick="paymentexport()"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>  
        
        <div class="clearix"></div>
        <div class="col-md-6">
          <div class="tile">
		  <h2>Payment Items</h2>
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="">
                <thead bgcolor="#009688">
                  <tr>
                    <th></th>
					<th>Total lần mua</th>
                    <th>Total Người mua</th>
					<th>Tỉ lệ</th>
					<th>Total doanh thu</th>
					<th>Tỉ lệ</th>
                  </tr>
                </thead>
                <tbody>
                <?php
					//print_r($data);exit;
					$active_user = $data["active"];
					if($data["active"]==0)
						$active_user=1;
					if($arrItems)
					{
						foreach($arrItems as $value)
						{
							if($value["pay_type"]>0){
								echo '<tr>';
								echo '<td>'.$value["pay_name"].'</td>';
								echo '<td>'.$value["num"].'</td>';
								echo '<td>'.$value["pu"].'</td>';
								echo '<td>'.number_format(($value["pu"] / $active_user * 100),2).' %</td>';
								echo '<td>'.number_format($value["total"]).'</td>';
								echo '<td>'.number_format(($value["total"] / $data["total"] * 100),2).' %</td>';
								echo '</tr>';
							}
							
						}
					}
				?>
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>
		<div class="col-md-6">
          <div class="tile">
            <h3 class="tile-title">Tỷ lệ người mua</h3>
            <div class="embed-responsive embed-responsive-16by9">
              <canvas class="embed-responsive-item" id="pieChartHome"></canvas>
            </div>
			<div>
				<span class="badge" style="background-color:#F7464A">Gói nạp thường</span>
				<span class="badge" style="background-color:#46BFBD">Gói nạp ngày</span>
			</div>
			
			<div>
				<span class="badge" style="background-color:#FDB45C">Gói thẻ tháng</span>
				<span class="badge" style="background-color:#17a2b8">Gói chí tôn</span>
			</div>
          </div>
        </div>
		
		<script type="text/javascript">
		 
		  var pdataHome = [
			{
				value: <?php if(isset($arrItems[0]["pu"])) echo $arrItems[0]["pu"]; else echo 0; ?>,
				color:"#F7464A",
				highlight: "#FF5A5E",
				label: "<?php  if(isset($arrItems[0]["pay_name"])) echo $arrItems[0]["pay_name"];?>"
			},
			{
				value: <?php if(isset($arrItems[1]["pu"])) echo $arrItems[1]["pu"]; else echo 0;?>,
				color: "#46BFBD",
				highlight: "#5AD3D1",
				label: "<?php if(isset($arrItems[1]["pay_name"])) echo $arrItems[1]["pay_name"];?>"
			},
			{
				value: <?php if(isset($arrItems[2]["pu"])) echo $arrItems[2]["pu"]; else echo 0;?>,
				color: "#FDB45C",
				highlight: "#FFC870",
				label: "<?php if(isset($arrItems[2]["pay_name"])) echo $arrItems[2]["pay_name"];?>"
			},
			{
				value: <?php if(isset($arrItems[3]["pu"])) echo $arrItems[3]["pu"]; else echo 0;?>,
				color: "#17a2b8",
				highlight: "#FFC870",
				label: "<?php if(isset($arrItems[3]["pay_name"])) echo $arrItems[3]["pay_name"];?>"
			}
		  ]
		</script>
		
		<div class="col-md-12">
          <div class="tile">
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="paymentTable11">
                <thead bgcolor="#FDB45C">
                  <tr>
                    <th>Total Revnue</th>
                    <th><?php echo number_format($data["total"]); ?></th>
                  </tr>
				  <tr>
                    <th>Total PU</th>
                    <th><?php echo $data["pu"]; ?></th>
                  </tr>
				</thead>
                <tbody>
                <?php
					if(isset($dataTemp))
					{
						$i=0;
						foreach($dataTemp as $key=>$value)
						{
							if($i % 2 ==0)
								echo '<thead>';
							else{
								echo '<thead bgcolor="#009688">';
							}
							if($value["pu"]==0)
								$value["sumtotal"] =0;
							echo '<tr>';
							echo '<th>Revnue ('.$dataTempName[$key]["name"].')</th>';
							echo '<th>'.number_format($value["sumtotal"]).'</th>';
							echo '</tr>';
							
							echo '<tr>';
							echo '<th>PU ('.$dataTempName[$key]["name"].')</th>';
							echo '<th>'.$value["pu"].'</th>';
							echo '</tr>';
							
							echo '<tr>';
							echo '<th>Percent Rev ('.$dataTempName[$key]["name"].')</th>';
							echo '<th>'.number_format(($value["sumtotal"] / $data["total"] *100),2).' %</th>';
							
							echo '</tr>';
							echo '</thead>';
							$i++;
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
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="paymentTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					<th>Server</th>
                    <th>Doanh Thu (VNĐ)</th>
                    <th>PU</th>
                    <th>160 vàng</th>
                    <th>400 vàng</th>
                    <th>800 vàng</th>
                    <th>4000 vàng</th>
                    <th>8000 vàng</th>
                    <th>12000 vàng</th>
                    <th>Quà Tài Lộc</th>
                    <th>Quà Hảo hữu</th>
                    <th>Quà Hoạt Lực</th>
                    <th>Thẻ Tháng Thường</th>
                    <th>Thẻ Tháng Trung</th>
                    <th>Thẻ Tháng Cao</th>
                    <th>Thẻ Chí Tôn</th>
                  </tr>
                </thead>
                <tbody>
                <?php
				
					if(isset($report))
					{
						foreach($report as $value)
						{
							echo '<tr>';
							echo '<td>'.date('Y-m-d',strtotime($value["log_ymd"])).'</td>';
							echo '<td>'.$value["server_name"].'</td>';
							echo '<td>'.number_format($value["total"]).'</td>';
							echo '<td>'.$value["pu"].'</td>';
							if(isset($value["item5"])) echo '<td>'.$value["item5"] .'</td>'; else echo '<td>0</td>';
							if(isset($value["item6"]))echo '<td>'.$value["item6"].'</td>';else echo '<td>0</td>';
							if(isset($value["item7"]))echo '<td>'.$value["item7"].'</td>';else echo '<td>0</td>';
							if(isset($value["item8"])) echo '<td>'.$value["item8"].'</td>';else echo '<td>0</td>';
							if(isset($value["item9"])) echo '<td>'.$value["item9"].'</td>';else echo '<td>0</td>';
							if(isset($value["item10"])) echo '<td>'.$value["item10"].'</td>';else echo '<td>0</td>';
							if(isset($value["item11"]))echo '<td>'.$value["item11"].'</td>';else echo '<td>0</td>';
							if(isset($value["item12"]))echo '<td>'.$value["item12"].'</td>';else echo '<td>0</td>';
							if(isset($value["item13"]))echo '<td>'.$value["item13"].'</td>';else echo '<td>0</td>';
							if(isset($value["item1"]))echo '<td>'.$value["item1"].'</td>';else echo '<td>0</td>';
							if(isset($value["item2"]))echo '<td>'.$value["item2"].'</td>';else echo '<td>0</td>';
							if(isset($value["item3"]))echo '<td>'.$value["item3"].'</td>';else echo '<td>0</td>';
							if(isset($value["item4"]))echo '<td>'.$value["item4"].'</td>';else echo '<td>0</td>';
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
		function paymentsearch()
		{
			$('#frmpayment').submit();
		}
		
				
		function paymentexport()
		{
			var serverID = document.getElementById("idServer").value;
			var fromDate = document.getElementById("fromDate").value;
			var toDate = document.getElementById("toDate").value;
			var DOMAIN = "https://po-ptm.mto.zing.vn/";
			window.location.href= DOMAIN + "main/exportpayment?idServer="+serverID+"&fromDate=" + fromDate + "&toDate=" + toDate;
		}
		
	</script>
    