'''An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.'''


def climbingLeaderboard(ranked, player):
    # Write your code here
    sorted_ranked = sorted(set(ranked), reverse = True)
    n= len(sorted_ranked)
    res =[]
    
    for player_score in player:
        left = 0
        right = n-1
        rank = None
        while(left <= right):
            mid = (left + right) // 2
            
            if sorted_ranked[mid] == player_score:
                rank = mid + 1
                break
            elif sorted_ranked[mid] < player_score:
                right = mid - 1
            else:
                left = mid + 1
        if rank == None:
            rank = left + 1
        res.append(rank)
    return res
