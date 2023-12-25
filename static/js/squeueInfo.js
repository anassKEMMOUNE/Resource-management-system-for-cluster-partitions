function squeueInfo(){
    const jsonFilePath = "static/json/result3.json";
    jsonObject = {};
    output = [];
    window.squeue = [];
    fetch(jsonFilePath)
                .then(response => response.json())
                .then(data => {
                    selectedPartition = document.getElementById("partitionSelect").value;
                    if (selectedPartition !== 'None'){

                        jsonObject = data;
                        document.getElementById("squeueInfo").innerHTML =  "";
                        var table = document.createElement('table');
                        var thead = table.createTHead();
                        var headerRow = thead.insertRow();
                        ['Username', 'Nodes', 'Time Used'].forEach(function (headerText) {
                        var th = document.createElement('th');
                        th.appendChild(document.createTextNode(headerText));
                        headerRow.appendChild(th);
                        });
                    
                    
                        var tbody = table.createTBody();
                    
                    for ( jobId in jsonObject){
                             jobInfo = jsonObject[jobId];

                             jobPartition = jobInfo.PARTITION;
        
                             nodelist = jobInfo["NODELIST(REASON)"];
                             user = jobInfo.USER;
                             time = jobInfo.TIME;
                            if (jobPartition === selectedPartition){
                                var arr = [user,nodelist,time];
                                var tr = tbody.insertRow();
                                arr.forEach(function (cell) {
                                var td = tr.insertCell();
                                td.appendChild(document.createTextNode(cell));
                                });

                            }
    
                            
                    }
                    document.getElementById("squeueInfo").appendChild(table); 

                    
                    }
                    


                })
                .catch(error => console.error('Error fetching JSON:', error));

}

