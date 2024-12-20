import React, { useState, useEffect } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { ExternalLink } from 'lucide-react';

const LeaderboardCard = () => {
  const [leaderboardData, setLeaderboardData] = useState(null);
  
  useEffect(() => {
    const handleLeaderboardClick = async (event) => {
      try {
        const response = await fetch('/filter_data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ node_id: event.detail.nodeId })
        });
        const data = await response.json();
        setLeaderboardData(data);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    };

    window.addEventListener('leaderboardClick', handleLeaderboardClick);
    return () => window.removeEventListener('leaderboardClick', handleLeaderboardClick);
  }, []);

  if (!leaderboardData) return null;

  return (
    <Card className="w-full bg-white shadow-sm mt-4">
      <CardContent className="p-6">
        <div className="grid grid-cols-2 gap-6">
          {/* Left Column */}
          <div className="space-y-4">
            <div>
              <a 
                href={leaderboardData.source}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 flex items-center gap-2"
              >
                {leaderboardData.leaderboard}
                <ExternalLink className="w-4 h-4" />
              </a>
            </div>
            
            <div className="text-gray-700">
              {leaderboardData.tooltip}
            </div>
            
            {leaderboardData.methodology && (
              <div>
                <a 
                  href={leaderboardData.methodology}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 hover:text-blue-800 flex items-center gap-2"
                >
                  View Methodology
                  <ExternalLink className="w-4 h-4" />
                </a>
              </div>
            )}
          </div>
          
          {/* Right Column */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Tips for using this leaderboard</h3>
            <ul className="list-disc pl-5 space-y-2">
              {leaderboardData.analysis_tips?.map((tip, index) => (
                <li key={index} className="text-gray-700">{tip}</li>
              ))}
            </ul>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default LeaderboardCard;