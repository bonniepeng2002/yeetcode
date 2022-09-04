using namespace std;
class Solution {
public:
    // Idea:
    // Create a queue (this is the return response)
    // Iterate through the string, adding chars onto the queue
    // When you encounter a repeated character, determine if the curr queue has size > prev queue
    // Then, pop from queue
    bool isInQ(char c, const deque<char> q) {
        for (auto qc:q) {
            if (c == qc) return true;
        }
        return false;
    }
    int lengthOfLongestSubstring(string s) {
        deque<char> res;
        deque<char> strRes;
        for (int i = 0; i < s.size(); ++i) {
            if (res.size() == 0 || !isInQ(s[i], res)) {
                res.push_back(s[i]);
            } else { // alr in deque
                if (res.size() > strRes.size()) strRes = res;
                while (res.front() != s[i]) {
                    res.pop_front();
                }
                res.pop_front();
                res.push_back(s[i]);
            }
        }
        if (res.size() > strRes.size()) strRes = res;
        return strRes.size();
    }
};
