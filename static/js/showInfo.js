// Initialize an object to store data for different dropdowns
window.dataStore = {};

// Fetch data from JSON file
function fetchData(jsonFile, dropdownId, containerId) {
    fetch(jsonFile)
        .then(response => response.json())
        .then(data => {
            // Call a function to populate the dropdown with data
            populateDropdown(data, dropdownId);

            // Store the data in the dataStore object using dropdownId as the key
            window.dataStore[dropdownId] = data;
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Populate dropdown with data
function populateDropdown(data, dropdownId) {
    var select = document.getElementById(dropdownId);

    // Clear previous options
    select.innerHTML = '';

    // Add options to the dropdown based on data
    Object.keys(data).forEach(dataName => {
        var option = document.createElement('option');
        option.value = dataName;
        option.textContent = dataName;
        select.appendChild(option);
    });
}

function showInfo(dropdownId, containerId) {
    var select = document.getElementById(dropdownId);
    var dataName = select.value;
    var dataDetails = window.dataStore[dropdownId] && window.dataStore[dropdownId][dataName];
    console.log(dataDetails);
    console.log(window.dataStore[dropdownId]);

    var container = document.getElementById(containerId);
    var detailsElement = document.getElementById(containerId + 'Details');

    // Clear previous content
    detailsElement.innerHTML = '';

    if (dataDetails) {
        // Create a table
        var table = document.createElement('table');
        table.style.width = '450px';
        var tbody = document.createElement('tbody');

        // Iterate through each key-value pair and create a row
        Object.keys(dataDetails).forEach(function (key) {
            var tr = document.createElement('tr');

            // Create the key cell
            var th = document.createElement('th');
            th.textContent = key;
            tr.appendChild(th);

            // Create the value cell
            var td = document.createElement('td');
            td.textContent = dataDetails[key];
            tr.appendChild(td);

            // Append the row to the table body
            tbody.appendChild(tr);
        });

        // Append the tbody to the table and the table to the detailsElement
        table.appendChild(tbody);
        detailsElement.appendChild(table);

        // Display the table
        container.style.display = 'block';
    } else {
        console.error('Data details not available for:', dataName);
    }
}

// Example usage:
fetchData('static/json/result01.json', 'partitionSelect', 'partitionInfo');
// Example usage:
fetchData('static/json/result2.json', 'nodeSelect', 'nodeInfo');
