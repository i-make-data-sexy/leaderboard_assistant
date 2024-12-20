/* ========================================================================
   Initialization and Setup
   ======================================================================== */

// Initialize network object at global scope
var network = null;

// Update canvas size to match container
function resizeCanvas() {
    const container = document.getElementById('network-container');
    if (container) {
        const canvas = container.querySelector('canvas');
        if (canvas) {
            canvas.style.width = '100%';
            canvas.style.height = '100%';                             // Container height set in CSS
        }
    }
}

// Add resize event listener
window.addEventListener('resize', function() {
    resizeCanvas();
    if (network) {
        network.fit(); // This ensures the network fills the available space
    }
});

// Key functionality of network graph
function initializeNetwork() {
    try {
        console.log('Initializing network:', {
            'vis available': typeof vis !== 'undefined',
            'network data exists': !!window.networkData,
            'container exists': !!document.getElementById('network-container')
        });
        
        // Check for vis-network library
        if (typeof vis === 'undefined') {
            throw new Error('vis-network library not available');
        }
        
        // Check for container
        const container = document.getElementById('network-container');
        if (!container) {
            throw new Error('network-container element not found');
        }
        
        // Check for network data
        if (!window.networkData) {
            throw new Error('Network data not available');
        }
        
        // Clear any existing content in the container
        container.innerHTML = '';
        
        // Create a loading indicator
        const loadingDiv = document.createElement('div');
        loadingDiv.textContent = 'Loading network...';
        loadingDiv.style.textAlign = 'center';
        loadingDiv.style.padding = '20px';
        container.appendChild(loadingDiv);
    
        const zoomLevel = $('#node-spacing-slider').val() || 1;
        const networkData = window.networkData || { nodes: [], edges: [] };
        
        console.log('Network data:', {
            nodes: networkData.nodes.length,
            edges: networkData.edges.length,
            data: networkData
        });

        network = new vis.Network(
            container,
            {
                nodes: new vis.DataSet(networkData.nodes),
                edges: new vis.DataSet(networkData.edges)
            },
            {
                layout: {
                    hierarchical: {
                        enabled: true,
                        direction: 'UD',
                        sortMethod: 'directed'
                    }
                },
                autoResize: true,
                // height: '100%',                               // Set container height
                width: '100%',
                physics: {
                    enabled: false
                },
                edges: {
                    smooth: false,
                    arrows: {
                        to: false                                   // Removes arrows from edges
                    }
                },
                interaction: {
                    zoomView: false,                                // Disable mouse zoom
                    zoomSpeed: 0,                                   // Disable mouse wheel zoom
                    dragNodes: true,
                    zoomSpeed: 0
                },
                nodes: {
                    shape: 'dot',
                    font: {
                        face: 'Ek Mukta',
                        size: 14,
                        background: '#ffffffCC',
                        color: '#333333',
                        strokeWidth: 0,
                        multi: true,  // Enable multi-font support
                        bold: {  // Define bold font style
                            color: '#333333',
                            size: 16,
                            face: 'Ek Mukta'
                        }
                    },
                    borderWidth: 1,
                    borderWidthSelected: 2
                }
            }
        );
        console.log('Network creation successful');
        // resizeCanvas();

        // Ensure network fills the space initially
        network.fit();                                      
        setupZoomSlider();
        setupNetworkClickHandler();
    
    } catch (error) {
        console.error('Error initializing network:', error);

        // Re-throw to be caught by initializeNetworkWithRetry
        throw error; 
    }
}


// Setup when document is ready
document.addEventListener('DOMContentLoaded', function() {
    const resultsContainer = document.getElementById('results');
    if (!resultsContainer) {
        console.error('Results container not found');
        return;
    }

    // Initialize if container is already visible
    if (!resultsContainer.classList.contains('hidden')) {
        initializeNetwork();
    }

    // Setup form submission handler
    const form = document.getElementById('modelPickerForm');
    if (form) {
        form.addEventListener('submit', function() {
            // Form submission will naturally update URL
            resultsContainer.classList.remove('hidden');
        setTimeout(initializeNetwork, 100);                         // Give DOM time to update
        });
    }
});

/* ========================================================================
   Slider Configuration and Event Handling
   ======================================================================== */

// Initialize slider controls for zoom
function setupZoomSlider() {
    $('#node-spacing-slider').on('input', function() {
        var zoomValue = parseFloat($(this).val());
        updateSliderTrack(this, zoomValue);
        updateNetworkZoom(zoomValue);
    });

    setSliderTrackValue();
}

// Update the slider's visual filled track
function updateSliderTrack(slider, value) {
    const min = parseFloat(slider.min) || 0;
    const max = parseFloat(slider.max) || 2;
    const percentage = ((value - min) / (max - min)) * 100;
    slider.style.setProperty('--value', `${percentage}%`);
}

// Apply zoom value to network
function updateNetworkZoom(zoomValue) {
    if (network) {
        network.moveTo({
            scale: zoomValue,
            animation: {
                duration: 1000,
                easingFunction: 'easeInOutQuad'
            }
        });
    }
}

// Initialize slider track value on page load
function setSliderTrackValue() {
    const slider = document.getElementById('node-spacing-slider');
    if (slider) {
        const min = slider.min || 0;
        const max = slider.max || 100;
        const value = slider.value;
        const percentage = ((value - min) / (max - min)) * 100;
        slider.style.setProperty('--value', `${percentage}%`);
    }
}

/* ========================================================================
   Network Graph Event Handling
   ======================================================================== */

// Set up click handlers for network nodes
function setupNetworkClickHandler() {
    if (!network) return;

    network.on('click', function(params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            
            if (nodeId.startsWith('leaderboard_')) {
                handleLeaderboardNodeClick(nodeId);
            }
        }
    });
}

console.log('Network click handler setup complete');

// Handle clicks on leaderboard nodes
function handleLeaderboardNodeClick(nodeId) {
    // This will be handled by the React component
    const event = new CustomEvent('leaderboardClick', { 
        detail: { nodeId: nodeId }
    });
    window.dispatchEvent(event);
}

/* ========================================================================
   Window Event Handling and UI Updates
   ======================================================================== */


// Handle window resize events
$(window).on('resize', function() {
    resizeCanvas();
});


/* ========================================================================
   Set Styling for Benchmark Labels
   ======================================================================== */

// For benchmark nodes, apply custom label formatting
function formatBenchmarkLabel(label) {
    // Assuming benchmark labels have a specific format like "Benchmark: Value"
    if (label.includes('Benchmark')) {
        return `<b>${label}</b>`;  // This will use the bold font style we defined
    }
    return label;
}