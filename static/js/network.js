/* ========================================================================
   Initialization and Setup
   ======================================================================== */

// Initialize network object at global scope
let network;

function initializeNetwork() {
    console.log('Initializing network:', {
        'vis available': typeof vis !== 'undefined',
        'network data exists': !!window.networkData,
        'container exists': !!document.getElementById('network-container')
    });
    
    if (typeof vis === 'undefined') {
        console.error('Error: vis-network library not available');
        return;
    }
    
    const container = document.getElementById('network-container');
    if (!container) {
        console.error('Error: network-container element not found');
        return;
    }
    
    const spacingValue = $('#node-spacing-slider').val() || 200;
    const networkData = window.networkData || { nodes: [], edges: [] };
    
    try {
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
                        levelSeparation: parseInt(spacingValue),
                        nodeSpacing: parseInt(spacingValue),
                        treeSpacing: 200,
                        direction: 'UD',
                        sortMethod: 'directed'
                    }
                },
                physics: {
                    enabled: false
                },
                edges: {
                    smooth: false
                },
                interaction: {
                    zoomView: false,
                    dragNodes: true,
                    zoomSpeed: 0
                },
                nodes: {
                    shape: 'dot',
                    font: {
                        face: 'Ek Mukta',
                        size: 14,
                        background: '#ffffffCC', // white with slight transparency
                        color: '#333333',
                        strokeWidth: 0
                    },
                    borderWidth: 1,
                    borderWidthSelected: 2
                }
            }
        );
        console.log('Network creation successful');
        
        setupSlider();
        setupNetworkClickHandler();
        resizeCanvas();
    } catch (error) {
        console.error('Error initializing network:', error);
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
            setTimeout(initializeNetwork, 100); // Give DOM time to update
        });
    }
});

/* ========================================================================
   Slider Configuration and Event Handling
   ======================================================================== */

// Initialize slider controls and event listeners
function setupSlider() {
    $('#node-spacing-slider').on('input', function() {
        var spacingValue = $(this).val();
        updateSliderTrack(this, spacingValue);
        updateNetworkSpacing(spacingValue);
    });

    setSliderTrackValue();
}

// Update the slider's visual filled track
function updateSliderTrack(slider, spacingValue) {
    const min = slider.min || 0;
    const max = slider.max || 100;
    const percentage = ((spacingValue - min) / (max - min)) * 100;
    slider.style.setProperty('--value', `${percentage}%`);
}

// Apply new spacing values to network layout
function updateNetworkSpacing(spacingValue) {
    if (network) {
        network.setOptions({
            layout: {
                hierarchical: {
                    enabled: true,
                    levelSeparation: parseInt(spacingValue),
                    nodeSpacing: parseInt(spacingValue),
                    treeSpacing: 200,
                    direction: 'UD',
                    sortMethod: 'directed',
                }
            },
            // Disable physics engine to prevent node movement
            physics: {
                enabled: false
            },
            // Disable zoom interactions for better UX
            interaction: {
                zoomView: false,
                zoomSpeed: 0
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

// Update canvas size to match container
function resizeCanvas() {
    $('#network-container canvas').css({
        width: '100%',
        height: '100%'
    });
}

// Handle window resize events
$(window).on('resize', function() {
    resizeCanvas();
});