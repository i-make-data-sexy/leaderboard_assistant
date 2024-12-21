import React, { useState, useEffect } from 'react';

const LeaderboardModal = () => {
  console.log('LeaderboardModal component initialized');
  const [data, setData] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    console.log('Component mounted');
    
    const handleLeaderboardClick = async (event) => {
      console.log('Received leaderboardClick event:', event.detail);
      try {
        const response = await fetch('/filter_data', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ node_id: event.detail.nodeId })
        });
        
        const responseData = await response.json();
        console.log('Received data:', responseData);
        setData(responseData);
        setIsOpen(true);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    window.addEventListener('leaderboardClick', handleLeaderboardClick);
    console.log('Event listener added');

    return () => {
      window.removeEventListener('leaderboardClick', handleLeaderboardClick);
      console.log('Event listener removed');
    };
  }, []);

  if (!isOpen || !data) {
    console.log('Modal not showing. isOpen:', isOpen, 'data:', data);
    return null;
  }

  console.log('Rendering modal with data:', data);

  // Basic modal without shadcn components
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-4xl max-h-[90vh] overflow-y-auto">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold">{data.leaderboard}</h2>
          <button 
            onClick={() => setIsOpen(false)}
            className="p-2 hover:bg-gray-100 rounded-full"
          >
            ×
          </button>
        </div>

        <div className="grid grid-cols-3 gap-6">
          {/* Column 1 */}
          <div>
            <h3 className="font-bold mb-2">Source</h3>
            <a 
              href={data.source}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-800"
            >
              Visit Leaderboard
            </a>

            {data.tooltip && (
              <div className="mt-4">
                <h3 className="font-bold mb-2">Summary</h3>
                <p>{data.tooltip}</p>
              </div>
            )}
          </div>

          {/* Column 2 */}
          <div>
            <h3 className="font-bold mb-2">Tips</h3>
            {data.analysis_tips && (
              <ul className="list-disc pl-4">
                {data.analysis_tips.map((tip, index) => (
                  <li key={index}>{tip}</li>
                ))}
              </ul>
            )}
          </div>

          {/* Column 3 */}
          <div>
            <h3 className="font-bold mb-2">Benchmarks</h3>
            {data.benchmarks && data.benchmarks.map((benchmark, index) => (
              <div key={index} className="mb-2">
                <p className="font-semibold">{benchmark.benchmark_name}</p>
                <p>{benchmark.benchmark_measures}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LeaderboardModal;