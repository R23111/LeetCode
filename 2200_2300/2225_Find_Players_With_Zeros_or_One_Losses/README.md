# 2225. Find Players With Zero or One Losses
(28/11 daily challenge)
You are given an integer array matches where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return a list answer of size 2 where:

- `answer[0]` is a list of all players that have **not** lost any matches.
- `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

### **Note**:

- You should only consider the players that have played at least one match.
- The testcases will be generated such that no two matches will have the same outcome.


---

## Submissions Status

|Language|Status|Runtime|Memory|
|---|---|---|---|
|python3|Accepted|3291ms|68.1MB|

