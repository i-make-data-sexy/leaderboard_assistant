import React from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { useState, useEffect } from 'react';
import { ExternalLink } from 'lucide-react';

const LeaderboardCard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const handleLeaderboardClick = async (event) => {
      try {
        const response = await fetch('/filter_data', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ node_id: event.detail.nodeId })
        });
        const responseData = await response.json();
        setData(responseData);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    };

    window.addEventListener('leaderboardClick', handleLeaderboardClick);
    return () => window.removeEventListener('leaderboardClick', handleLeaderboardClick);
  }, []);

  if (!data) return null;

  const {
    leaderboard,
    leaderboard_link,
    tooltip,
    methodology,
    analysis_tips,
    benchmarks
  } = data;

  return (
    <Card className="w-full max-w-4xl bg-white rounded-lg shadow-lg p-6 mt-4">
      <CardContent className="p-0">
        <div className="grid grid-cols-3 gap-6">
          {/* Column 1 */}
          <div className="space-y-4">
            <div>
              <h3 className="font-bold text-lg mb-2">Leaderboard</h3>
              <p className="mb-2">{leaderboard}</p>
              <a
                href={leaderboard_link?.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 flex items-center gap-1"
              >
                View leaderboard <ExternalLink size={16} />
              </a>
            </div>

            <div>
              <h3 className="font-bold text-lg mb-2">Summary</h3>
              <p className="text-gray-700">{tooltip}</p>
            </div>

            {methodology?.url && (
              <div>
                <h3 className="font-bold text-lg mb-2">Methodology</h3>
                <a
                  href={methodology.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 hover:text-blue-800 flex items-center gap-1"
                >
                  View methodology <ExternalLink size={16} />
                </a>
              </div>
            )}
          </div>

          {/* Column 2 */}
          <div>
            <h3 className="font-bold text-lg mb-2">Tips</h3>
            {analysis_tips && analysis_tips.length > 0 && (
              <ul className="list-disc pl-4 space-y-2">
                {analysis_tips.map((tip, index) => (
                  <li key={index} className="text-gray-700">{tip}</li>
                ))}
              </ul>
            )}
          </div>

          {/* Column 3 */}
          <div>
            <h3 className="font-bold text-lg mb-2">Benchmark(s)</h3>
            {benchmarks && benchmarks.length > 0 && (
              <div className="space-y-4">
                {benchmarks.map((benchmark, index) => (
                  <div key={index} className="border-b border-gray-200 pb-2 last:border-0">
                    <p className="font-semibold">{benchmark.benchmark_name}</p>
                    <p className="text-gray-700">{benchmark.benchmark_measures}</p>
                    {benchmark.score_interpretation && (
                      <p className="text-gray-600 text-sm mt-1">
                        ({benchmark.score_interpretation})
                      </p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default LeaderboardCard;