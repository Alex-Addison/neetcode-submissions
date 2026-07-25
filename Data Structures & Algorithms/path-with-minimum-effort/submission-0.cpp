class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();
        
        // Min-heap stores: {current_max_effort, {x, y}}
        priority_queue<pair<int, pair<int, int>>, 
                       vector<pair<int, pair<int, int>>>, 
                       greater<pair<int, pair<int, int>>>> pq;
        
        // Distance table to track the minimum effort to reach each cell
        vector<vector<int>> dist(rows, vector<int>(cols, INT_MAX));
        
        pq.push({0, {0, 0}});
        dist[0][0] = 0;
        
        // Up, Down, Right, Left
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        
        while (!pq.empty()) {
            auto [effort, pos] = pq.top();
            int x = pos.first;
            int y = pos.second;
            pq.pop();
            
            // If we reached the bottom-right, we are done
            if (x == rows - 1 && y == cols - 1) {
                return effort;
            }
            
            // Skip if we already found a better path to this specific cell
            if (effort > dist[x][y]) {
                continue;
            }
            
            // Explore neighbors
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                
                // Check bounds
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                    // The effort to the neighbor is the max of the current path's effort 
                    // and the absolute difference in height to the neighbor
                    int next_effort = max(effort, abs(heights[nx][ny] - heights[x][y]));
                    
                    // If this new path is better, update and push to queue
                    if (next_effort < dist[nx][ny]) {
                        dist[nx][ny] = next_effort;
                        pq.push({next_effort, {nx, ny}});
                    }
                }
            }
        }
        return 0; // Fallback (shouldn't be reached if grid is valid)
    }
};