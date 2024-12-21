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
            // I commented this out as part of the refactoring effort
            // canvas.style.width = '100%';
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
                // CHANGED: Remove hierarchical layout or set enabled: false to rely on physics only.
                // If you want a physics-based layout with repulsion:
                layout: {
                    improvedLayout: false // CHANGED: Disables improvedLayout for a raw physics approach
                },
        
                // Use physics-based repulsion 
                physics: {
                    enabled: true,
                    solver: 'barnesHut',
                    barnesHut: {
                        gravitationalConstant: -30000,
                        centralGravity: 0.3,
                        springLength: 95,
                        springConstant: 0.04,
                        damping: 0.09,
                        avoidOverlap: 1
                    },
                    minVelocity: 0.75
                },
                autoResize: true,
                edges: {
                    smooth: false,
                    arrows: {
                        to: false,
                    }
                },
                interaction: {
                    zoomView: false,
                    zoomSpeed: 0,
                    dragNodes: true,
                    hover: true, 
                    tooltipDelay: 0,
                    hoverConnectedEdges: true,
                    keyboard: false,                        // Disable keyboard navigation
                    hideEdgesOnDrag: true,                  // Improve performance
                },
                nodes: {
                    shape: 'dot',
                    font: {
                        face: 'Ek Mukta',
                        size: 14,
                        background: '#ffffffCC',
                        color: '#333333',
                        strokeWidth: 0,
                        multi: true,
                        bold: {
                            color: '#333333',
                            size: 16,
                            face: 'Ek Mukta'
                        }
                    },
                    borderWidth: 1,
                    borderWidthSelected: 2,
                    chosen: {
                        node: function(values, id, selected, hovering) {
                            if (hovering) {
                                document.body.style.cursor = 'pointer';
                            }
                        }
                    }
                }
            }
        );

        // Add event listeners after initialization
        network.once('stabilized', function () {
            network.on('hoverNode', function (params) {
                console.log('Hovered node:', params.node);
            });
            console.log('Event listeners are now attached.');
        });

        console.log(networkData.nodes);
        // console.log(networkData.edges);

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

/* ========================================================================
    Resize Visualization Container
    ======================================================================== */

document.addEventListener('DOMContentLoaded', function () {
    const networkContainerWrapper = document.querySelector('.network-container');
    const resizer = document.querySelector('#resizer');

    let isDragging = false;

    resizer.addEventListener('mousedown', () => {
        isDragging = true;
        document.body.style.cursor = 'row-resize';
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;

        // Measure from the top of .network-container
        const containerRect = networkContainerWrapper.getBoundingClientRect();
        const newHeight = e.clientY - containerRect.top;

        // Ensure minimum and maximum heights
        if (newHeight > 300 && newHeight < window.innerHeight * 0.9) {
            networkContainerWrapper.style.height = `${newHeight}px`;
            if (window.network) {
                network.fit({
                    animation: {
                        duration: 500,
                        easingFunction: 'easeInOutQuad'
                    }
                });
            }
        }
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            document.body.style.cursor = 'default';
        }
    });
});


/* ========================================================================
    Tooltip Interactivity
    ======================================================================== */

// Create and append tooltip element if it doesn't exist
let tooltip = document.querySelector('.vis-tooltip');
if (!tooltip) {
    tooltip = document.createElement('div');
    tooltip.className = 'vis-tooltip';
    document.body.appendChild(tooltip);
}

// Handle node hover events
network.on('hoverNode', function(params) {
    const nodeId = params.node;
    const node = network.body.nodes[nodeId];
    if (!node) return;

    const position = network.getPositions([nodeId])[nodeId];
    const canvasPos = network.canvasToDOM(position);
    
    // Get container bounds
    const container = document.getElementById('network-container');
    const containerRect = container.getBoundingClientRect();
    
    // Calculate tooltip position
    let left = canvasPos.x + containerRect.left;
    let top = canvasPos.y + containerRect.top;
    
    // Adjust position to prevent tooltip from going off-screen
    const tooltipRect = tooltip.getBoundingClientRect();
    if (left + tooltipRect.width > window.innerWidth) {
        left = window.innerWidth - tooltipRect.width - 10;
    }
    if (top + tooltipRect.height > window.innerHeight) {
        top = window.innerHeight - tooltipRect.height - 10;
    }
    
    // Update tooltip content and position
    tooltip.textContent = node.options.title || '';
    tooltip.style.left = `${left + 10}px`;
    tooltip.style.top = `${top + 10}px`;
    tooltip.style.visibility = 'visible';
    tooltip.style.opacity = '1';
    
    // Update cursor
    document.body.style.cursor = 'pointer';
});

// Handle mouse leave events
network.on('blurNode', function() {
    tooltip.style.visibility = 'hidden';
    tooltip.style.opacity = '0';
    document.body.style.cursor = 'default';
});