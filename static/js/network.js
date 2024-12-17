/* ========================================================================
   Initialization and Setup
   ======================================================================== */

// Wait for DOM to be fully loaded before initializing any components
$(document).ready(function() {
    // console.log("Initializing network with hierarchical layout.");
    
    // Get initial spacing value from slider or fallback to default
    const spacingValue = $('#node-spacing-slider').val() || 200;

    // Configure the network visualization with comprehensive layout options
    network.setOptions({
        layout: {
            // Enable hierarchical layout for tree structures
            hierarchical: {
                enabled: true,

                // Set vertical distance between hierarchy levels
                levelSeparation: parseInt(spacingValue),

                // Set horizontal distance between nodes at same level
                nodeSpacing: parseInt(spacingValue),

                // Set spacing between different tree structures
                treeSpacing: 200,

                // Configure top-to-bottom hierarchy layout
                direction: 'UD',

                // Use directed graph method for node sorting
                sortMethod: 'directed'
            }
        },

        // Disable physics engine to prevent node movement
        physics: {
            enabled: false
        },

        // Configure edges to be straight lines
        edges: {
            smooth: false
        },

        // Disable zoom interactions for better UX
        interaction: {
            zoomView: false,
            zoomSpeed: 0
        }
    });

    // Initialize slider controls with event handlers
    setupSlider();

    // Verify data element exists before proceeding
    if (!checkInitialDataElement()) {
        return;
    }

    // Initialize DataTable with full configuration
    var table = initializeDataTable();

    // Set up network click handlers if network is available
    if (typeof network !== 'undefined' && network) {
        setupNetworkClickHandler(table);
    }

    // Ensure canvas is properly sized on initial load
    resizeCanvas();
});

/* ========================================================================
   Slider Configuration and Event Handling
   ======================================================================== */

// Initialize slider controls and event listeners
function setupSlider() {
    // console.log("Setting up slider for node spacing adjustment.");

    // Handle slider value changes
    $('#node-spacing-slider').on('input', function() {
        var spacingValue = $(this).val();
        // Update visual track display
        updateSliderTrack(this, spacingValue);
        // Apply new spacing to network
        updateNetworkSpacing(spacingValue);
    });

    // Initialize slider visual state
    setSliderTrackValue();
}

// Update the slider's visual filled track
function updateSliderTrack(slider, spacingValue) {

    // Get min and max values for slider
    const min = slider.min || 0;
    const max = slider.max || 100;

    // Calculate percentage for visual fill
    const percentage = ((spacingValue - min) / (max - min)) * 100;

    // Update CSS custom property for track fill
    slider.style.setProperty('--value', `${percentage}%`);
}

// Apply new spacing values to network layout
function updateNetworkSpacing(spacingValue) {

    // Update hierarchical layout options with new spacing
    network.setOptions({
        layout: {
            hierarchical: {
                // Enable hierarchical layout with updated spacing
                enabled: true,

                // Set vertical distance between hierarchy levels
                levelSeparation: parseInt(spacingValue),

                // Set horizontal distance between nodes at same level
                nodeSpacing: parseInt(spacingValue),

                // Set spacing between different tree structures
                treeSpacing: 200,

                // Configure top-to-bottom hierarchy layout
                direction: 'UD',

                // Use directed graph method for node sorting
                sortMethod: 'directed'
            }
        }
    });
}

// Initialize slider track value on page load
function setSliderTrackValue() {

    // Get slider element and min/max values
    const slider = document.getElementById('node-spacing-slider');

    // Get min and max values for slider
    const min = slider.min || 0;
    const max = slider.max || 100;

    // Get current value from slider
    const value = slider.value;

    // Calculate initial percentage for track fill
    const percentage = ((value - min) / (max - min)) * 100;

    // Update CSS custom property for track fill
    slider.style.setProperty('--value', `${percentage}%`);
}

/* ========================================================================
   Data Validation and Setup
   ======================================================================== */

// Verify required data element exists in DOM
function checkInitialDataElement() {

    // Check if initialData element exists in DOM
    const initialDataElem = document.getElementById('initialData');

    // Log error if element is missing and return false
    if (!initialDataElem) {
        console.error('initialData element not found. Please check if it is defined in the HTML.');
        return false;
    }

    // Return true if element is found
    return true;
}

/* ========================================================================
   DataTable Initialization and Configuration
   ======================================================================== */

// Initialize DataTable with all required configurations
function initializeDataTable() {
    // console.log("Initializing DataTable.");

    // Initialize DataTable with full configuration
    var table = $('#model-table').DataTable({

        // Enable horizontal scrolling for wide tables
        scrollX: true,

        // Prevent automatic width calculations
        autoWidth: false,

        // Configure columns with specific settings
        columnDefs: defineColumnSettings(),

        // Load initial data from DOM element
        data: JSON.parse(document.getElementById('initialData').textContent),

        // Style table header
        headerCallback: styleTableHeader,

        // Handle row rendering and formatting
        drawCallback: handleDrawCallback
    });

    // Set up window-related event handlers
    setupWindowEvents(table);

    // Return initialized DataTable instance
    return table;
}

// Define column widths and configurations for DataTable
function defineColumnSettings() {
    return [
        // Leaderboard column settings
        { width: '5%', targets: 0, data: 'Leaderboard' },

        // Goal column settings
        { width: '8%', targets: 1, data: 'Goal' },

        // Leaderboard column with line break formatting
        { width: '8%', targets: 2, data: 'Leaderboard', render: addLineBreaks },

        // Tips column with line break formatting
        { width: '69%', targets: 3, data: 'Tips', render: addLineBreaks },

        // Source column with line break formatting
        { width: '5%', targets: 4, data: 'Source', render: addLineBreaks },

        // Method column with line break formatting
        { width: '5%', targets: 5, data: 'Method', render: addLineBreaks },
    ];
}

// Apply styling to table header
function styleTableHeader(thead) {
    // Set background color and text color for header cells
    $(thead).find('th').css({
        'background-color': 'rgba(0, 34, 55, 0.9)',
        'color': 'white'
    });
}

// Handle table drawing and row formatting
function handleDrawCallback(settings) {
    // Apply custom formatting to rows based on task and search terms
    var api = this.api();

    // Get current visible rows considering filters and pagination
    var rows = api.rows({ page: 'current', order: 'applied', search: 'applied' }).indexes();

    // Get search keyword for highlighting
    var searchKeyword = api.search().trim();

    // Track last task and goal for formatting
    var lastTask = null;

    // Track last goal for formatting
    var lastGoal = null;

    // Iterate over each row and apply formatting
    rows.each(function(rowIndex) {

        // Get row data and node for current row
        var rowData = api.row(rowIndex).data();

        // Get row node for current row
        var rowNode = api.row(rowIndex).node();

        // Get task and goal values for current row
        var task = rowData['Task'] ? rowData['Task'].trim() : '';

        // Get goal value for current row
        var goal = rowData['Goal'] ? rowData['Goal'].trim() : '';

        // Reset row classes and cell content
        $(rowNode).removeClass('task-row goal-row');

        // Reset cell content to original state
        resetCellContent(api, rowIndex, rowNode);

        // Apply task-based formatting
        handleTaskFormatting(api, rowIndex, rowNode, task, goal, lastTask, lastGoal);

        // Update task tracking
        if (task !== lastTask) {
            lastTask = task;
            lastGoal = goal;
        } else if (goal !== lastGoal) {
            lastGoal = goal;
        }

        // Apply search highlighting if needed
        if (searchKeyword) {
            highlightSearchTerms(api, rowIndex, rowNode, searchKeyword);
        }
    });
}

/* ========================================================================
   Table Formatting and Display Helpers
   ======================================================================== */

// Reset cell content to original state
function resetCellContent(api, rowIndex, rowNode) {

    // Iterate over each cell in the row and reset content
    $(rowNode).find('td').each(function(index, cell) {

        // Get cell data and render display content
        var cellData = api.cell(rowIndex, index).render('display');

        // Reset cell content to original state
        $(cell).html(cellData);
    });
}

// Handle task-based formatting for rows
function handleTaskFormatting(api, rowIndex, rowNode, task, goal, lastTask, lastGoal) {
    var taskCell = api.cell(rowIndex, 0).node();
    var goalCell = api.cell(rowIndex, 1).node();

    // New task row
    if (rowIndex === 0 || task !== lastTask) {

        // Add task row class and set cell content
        $(rowNode).addClass('task-row');

        // Apply line breaks to task and goal
        $(taskCell).html(addLineBreaks(task));

        // Check if goal is different
        $(goalCell).html(addLineBreaks(goal));
    } 

    // New goal within same task
    else if (goal !== lastGoal) {
        // Add goal row class and set cell content
        $(rowNode).addClass('goal-row');

        // Reset task cell content
        $(taskCell).html('');

        // Apply line breaks to goal
        $(goalCell).html(addLineBreaks(goal));
    } 

    // Same goal row
    else {
        // Reset task and goal cell content
        $(taskCell).html('');

        // Reset goal cell content
        $(goalCell).html('');
    }
}

// Add line breaks to text content based on numbered list format
function addLineBreaks(data, type) {
    // Check if data is empty or not a string
    if (type === 'display' && data) {

        // Check if content starts with numbered list
        const startsWithNumberedList = /^\d+\)/.test(data.trim());

        // Add breaks before all numbered items except the first
        if (startsWithNumberedList) {

            // Handle first item differently
            return data.replace(/(\d+\))/g, (match, p1, offset) => {

                // Add breaks before all numbered items except the first
                return offset === 0 ? match : `<br><br>${match}`;
            });
        } else {
            // Add breaks before all numbered items
            return data.replace(/(\d+\))/g, '<br><br>$1');
        }
    }
    return data;
}

/* ========================================================================
   Search and Highlighting
   ======================================================================== */

// Apply search term highlighting to matching content
function highlightSearchTerms(api, rowIndex, rowNode, searchKeyword) {

    // Iterate over each cell in the row and highlight matching content
    $(rowNode).find('td').each(function(index, cell) {

        // Get cell data and render display content
        var cellData = api.cell(rowIndex, index).render('display');

        // Highlight matching content in cell
        if (cellData.toLowerCase().includes(searchKeyword.toLowerCase())) {

            // Update cell content with highlighted keyword
            $(cell).html(highlightKeywordInHtml(cellData, searchKeyword, 'highlighted-keyword'));
        }
    });
}

// Highlight specific keywords within HTML content
function highlightKeywordInHtml(htmlContent, keyword, highlightClass) {
    // Create a temporary div element to parse HTML content
    var div = document.createElement('div');

    // Set HTML content to div element
    div.innerHTML = htmlContent;

    // Create tree walker to traverse text nodes
    var walk = document.createTreeWalker(div, NodeFilter.SHOW_TEXT, null, false);

    // Initialize regex pattern for keyword matching
    var regex = new RegExp('(' + keyword.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&') + ')', 'gi');

    // Initialize text node for processing
    var textNode;

    // Walk through text nodes and apply highlighting
    while ((textNode = walk.nextNode())) {
        if (textNode.nodeValue.toLowerCase().includes(keyword.toLowerCase())) {
            var parent = textNode.parentNode;
            var newHtml = textNode.nodeValue.replace(regex, `<span class="${highlightClass}">$1</span>`);
            var tempSpan = document.createElement('span');
            tempSpan.innerHTML = newHtml;
            parent.replaceChild(tempSpan, textNode);
        }
    }

    // Return updated HTML content with highlighted keywords
    return div.innerHTML;
}

/* ========================================================================
   Network Graph Event Handling
   ======================================================================== */

// Set up click handlers for network nodes
function setupNetworkClickHandler(table) {

    // Handle click events on network nodes
    network.on('click', function(params) {

        // Check if any nodes were clicked
        if (params.nodes.length > 0) {

            // Get node ID from clicked node
            var nodeId = params.nodes[0];
            
            // Handle different node types
            if (nodeId.startsWith('project_')) {

                // Handle project-level nodes
                handleProjectNodeClick(table);
            } else {

                // Handle regular nodes
                handleRegularNodeClick(nodeId, table);
            }
        }
    });
}

// Handle clicks on project-level nodes
function handleProjectNodeClick(table) {

    // Reset table data to initial state
    network.unselectAll();

    // Reset table data to initial state
    resetTableData(table);
}

// Handle clicks on regular nodes
function handleRegularNodeClick(nodeId, table) {

    // Fetch filtered data based on node ID
    $.ajax({
        // Send POST request to filter data based on node ID
        url: '/filter_data',                                    // URL to send request to   
        type: 'POST',                                           // Request type
        contentType: 'application/json',                        // Data type
        data: JSON.stringify({ 'node_id': nodeId }),            // Data to send
        success: function(filteredData) {                       // Function to run if request is successful
            updateTableWithFilteredData(table, filteredData);   // Update table with filtered data
        },
        error: function(xhr, status, error) {                   // Function to run if request fails
            console.error('Error fetching filtered data:', error);
        }
    });
}

/* ========================================================================
   Window Event Handling and UI Updates
   ======================================================================== */

// Set up window-related event handlers
function setupWindowEvents(table) {
    // Adjust table on window load
    $(window).on('load', function() {

        // Adjust table columns and redraw
        table.columns.adjust().draw();
    });

    // Handle window resize events
    $(window).on('resize', function() {

        // Adjust table columns and redraw        
        table.columns.adjust();

        // Resize canvas to match container
        resizeCanvas();
    });
}

// Update canvas size to match container
function resizeCanvas() {
    // Set canvas size to match container
    $('#network-container canvas').css({
        width: '100%',
        height: '100%'
    });
}

/* ========================================================================
   Data Management
   ======================================================================== */

// Reset table data to initial state
function resetTableData(table) {

    // Clear table data and reload initial data
    table.clear();

    // Fetch initial data from DOM and add to table
    try {
        // Parse initial data from DOM
        const initialData = JSON.parse(document.getElementById('initialData').textContent);

        // Add initial data to table and redraw
        table.rows.add(initialData).draw();
    
    // Log error if parsing fails
    } catch (error) {
        console.error('Error parsing initialData:', error);
    }
}

// Update table with filtered data
function updateTableWithFilteredData(table, filteredData) {

    // Clear existing table data and add filtered data
    table.clear();

    // Add filtered data to table and redraw
    if (filteredData.length > 0) {
        table.rows.add(filteredData).draw();
    }
}