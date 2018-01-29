import sys, random, time

from basic import *
from utils import *
from GameLog import GameLog
from TurnStage import get_available_moves, check_moves, apply_move

# b_player_control = [True,False]
# b_instruction_control = [False,False]

class Game():
    
    def __init__(self
                ,manual_control = () 
                ,instruction_control = (0,1) 
                ,s_instructions = ""
                ):

        self.outcome = None
        self.board = None
        self.manual_control = manual_control
        self.instructions = parse_instructions(s_instructions)
        if len(self.instructions) > 0:
            self.instruction_control = instruction_control 
        else:
            self.instruction_control = ()
        


    def select_move(self, moves, player,board, i_turn): 
    
        if int(player) in self.instruction_control:
            
            the_move, the_move_code = instruction_input(board
                                                        ,moves
                                                        ,self.instructions
                                                        ,i_turn
                                                        )
        elif int(player) in self.manual_control:
            
            the_move, the_move_code = player_control_input(board, moves)

        else:
            
            move_i = random.sample(range(0,len(moves)),1)[0]
            the_move = moves[move_i][0:2]
            the_move_code = moves[move_i][2] 

        return the_move, the_move_code



    def play(self, s_instructions = "", **kwargs):

        #INIT Board and pieces
        board = Board()
        board, pieces = place_pieces(board)
        dead_pieces = []

        log = GameLog()

        game_going = True
        i_turn = 0

        print_board_letters(board, pieces, True)

        #Turn Loop
        while(game_going):
            
            #TODO this is a counter-mod, not a for-loop
            for player in (True,False):
                
                i_turn += 1
                
                moves = get_available_moves(pieces, board, player)

                #TODO - Filter moves for king in check
                #NOTE - how to get out of check? all moves filtered by king_in_check
                #   but how to handle killing the checking piece?

                check_code = check_moves(moves, board, player)
                if check_code < 0:
                    #It's a loss or a stalemate
                    game_going = False
                    continue

                #TODO - this should be self.select_move
                the_move, the_move_code = self.select_move(
                                            moves
                                            ,player
                                            ,board
                                            ,i_turn
                                            )

                if the_move == -1: return i_turn

                #Apply the Move
                board, pieces, dead_pieces, kill_flag, pos0, pos1 = apply_move(the_move,the_move_code,board, pieces, dead_pieces, player)
                
                #Log / Record the Move
                log.moves_log.append(the_move)

                log.print_turn(  board = board
                                ,pieces = pieces
                                ,dead_pieces = dead_pieces
                                ,kill_flag = kill_flag
                                ,pos0 = pos0
                                ,pos1 = pos1
                                )

                #Exit from main for predefined instructions
                if int(player) in self.instruction_control:
                    if i_turn == len(self.instructions):
                        game_going = False
                        return board

        log.log_game()


if __name__ == "__main__":
    game = Game(manual_control = (1,), instruction_control = ())
    game.play()

b_instruction_control = [True,True]

def test_castling_allowed():
    
    ss = "1. h7 f8 2. b1 c1 3. g5 e5 4. b2 c2 5. h6 f4 6. b3 c3 7. h5 h7"
    game = Game(s_instructions = ss)
    board = game.play()
    assert board.data_by_player[7][5] == 1
    assert board.data_by_player[7][6] == 3

def test_castling_disallowed_rook():
    
    ss = "1. h7 f8 2. b1 c1 3. g5 e5 4. b2 c2 5. h6 f4 6. b3 c3 7. h8 h7 8. b4 c4 9. h7 h8 10. b5 c5 11. h5 h7"
    game = Game(s_instructions = ss)
    break_turn = game.play()
    assert break_turn == 11

def test_castling_disallowed_king():
    
    ss = "1. h7 f8 2. b1 c1 3. g5 e5 4. b2 c2 5. h6 f4 6. b3 c3 7. h5 h6 8. b4 c4 9. h6 h5 10. b5 c5 11. h5 h7"
    game = Game(s_instructions = ss)
    break_turn = game.play()
    assert break_turn == 11

def test_enpassant_take():
    
    ss = "1. g2 e2 2. b8 c8 3. e2 d2 4. b3 d3 5. d2 c3"
    game = Game(s_instructions = ss)
    board = game.play()
    board.print_board(b_player_data=True)
    assert board.data_by_player[2][2] == 1
    assert board.data_by_player[3][2] == 0
    

def test_enpassant_disallowed():
    
    ss = "1. g2 e2 2. b8 c8 3. e2 d2 4. b3 d3 5. g8 e8 6. b1 c1 7. d2 c3"
    game = Game(s_instructions = ss)
    break_turn = game.play()
    assert break_turn == 7

# if __name__ == "__main__":
#     test_castling_disallowed_king()
