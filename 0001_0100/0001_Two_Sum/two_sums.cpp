class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        for(int i = 0; i < nums.size(); i++){
            for(int j = nums.size()-1; j > i; j--){
                if(nums[i]+nums[j]==target){
                    answer.push_back(i);
                    answer.push_back(j);
                }
            }
        }
        return answer;
    }
};