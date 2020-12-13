<main class="app-content">
      <div class="app-title">
        <div>
          <h1><i class="fa fa-th-list"></i> Item</h1>
          
        </div>
        <ul class="app-breadcrumb breadcrumb side">
          <li class="breadcrumb-item"><i class="fa fa-home fa-lg"></i></li>
          <li class="breadcrumb-item">Operation</li>
          <li class="breadcrumb-item active"><a href="#">Item</a></li>
        </ul>
      </div>
      <div class="row">
        <div class="col-md-12">
          
            <div class="tile">
              <form class="row">
              <div class="form-group col-md-2">
                <select class="form-control" id="exampleSelect1">
                    <option value="0">--All--</option>
					<?php
						foreach($server as $value)
						{
							echo '<option value="'.$value["ServerIndex"].'">'.$value["server_name"].'</option>';
						}
					?>
                    </select>
                    </select>
                </div>
                <div class="form-group col-md-3">
                    <input class="form-control" id="fromDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-3">
                    <input class="form-control" id="toDate" type="text" placeholder="Select Date">
                </div>
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button"><i class="fa fa-fw fa-lg fa-check-circle"></i>Search</button>
                </div>
                <div class="form-group col-md-2 align-self-end">
                  <button class="btn btn-primary" type="button"><i class="fa fa-fw fa-lg fa-check-circle"></i>Export</button>
                </div>
              </form>
            </div>
        </div>

        <div class="clearix"></div>
        <div class="col-md-12">
          <div class="tile">
            <div class="tile-body">
              <table class="table table-hover table-bordered" id="sampleTable">
                <thead>
                  <tr>
                    <th>Ngày</th>
					          <th>Server</th>
                    <th>ID Event</th>
                    <th>Tên Item</th>
                    <th>ID Item</th>
                    <th>Số lượng</th>
                    
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                  
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>                   
                  </tr>
				  
				  
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </main>