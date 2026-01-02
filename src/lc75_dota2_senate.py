from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        kill_r_vote = 0
        kill_d_vote = 0

        senate_state = list(senate)

        while True:
            # One round
            count_r = 0
            count_d = 0
            for i in range(len(senate_state)):
                if senate_state[i] == 'R':
                    if kill_r_vote > 0:
                        kill_r_vote -= 1
                        senate_state[i] = 'X'
                    else:
                        kill_d_vote += 1
                        count_r += 1
                elif senate_state[i] == 'D':
                    if kill_d_vote > 0:
                        kill_d_vote -= 1
                        senate_state[i] = 'X'
                    else:
                        kill_r_vote += 1
                        count_d += 1
            if count_r == 0:
                return 'Dire'
            elif count_d == 0:
                return 'Radiant'

            
                                
        

