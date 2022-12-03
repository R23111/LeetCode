class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        for(int i = 0; i < height.size()-1; i++){
            if(height[i] == 0) continue;
            if(max/height[i] > height.size()-i || height[i]==0){
                continue;
            }
            for(int j = i+1; j < height.size(); j++){
                int minh = 0;
                if(height[i]>=height[j])
                    minh = height[j];
                else
                    minh = height[i];
                int curr = minh*(j-i);
                if(curr > max)
                    max = curr;
            }
        }
        return max;
    }
};