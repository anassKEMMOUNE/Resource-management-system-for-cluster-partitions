function transformNodeFormat(initial){
    
    var tst = initial.replace("node","").replace("[","").replace("]","");
    var middle = tst.split(",");
    var output = [];
    middle.forEach(function(element){
        if (element.includes("-")){
            var a = element.split("-");
            var start = parseInt(a[0]);
            var end = parseInt(a[1]);
            for (var i = start;i<=end;i++){
                var s = i.toString();
                if (i < 10){
                    s = "node0" + s;
                    output.push(s);
                }
                else {
                    output.push("node" +s);
                }
               
            }
        }
        else {
            if (!element.includes("visu")){
                output.push("node"+element);
            }
            else {
                output.push("visu01")
            }
            
            
        }
    
    }
    );
    return output;
}

function numberOfGpus() {
    const jsonFilePath = "static/json/result01.json";
    const jsonFilePath2 = "static/json/result4.json";
    var jsonObject = {};
    var output = {};

    const fetchJsonFile = (filePath) => {
        return fetch(filePath)
            .then(response => response.json())
            .catch(error => {
                console.error('Error fetching JSON:', error);
                throw error; // Re-throw the error to propagate it to the next catch
            });
    };

    // Use Promise.all to wait for both fetch operations to complete
    return Promise.all([fetchJsonFile(jsonFilePath2), fetchJsonFile(jsonFilePath)])
        .then(([data2, data]) => {
            jsonObject = data;
            window.jsonObject2 = data2;

            for (partition in jsonObject) {
                output[partition] = {};
                jobInfo = jsonObject[partition];
                // numberOfCpu = jobInfo.TotalCPUs;
                nodelist = transformNodeFormat(jobInfo.Nodes);
                output[partition].Nodes = nodelist;
                output[partition].TotalGPUs = 0;
                output[partition].GPUAlloc = 0;

                nodelist.forEach(function (node) {
                    if (node in window.jsonObject2){
                        output[partition].GPUAlloc += parseInt(window.jsonObject2[node]);
                        output[partition].TotalGPUs += 1;
                    }
                    
                });
            }

            return output;
        });
}