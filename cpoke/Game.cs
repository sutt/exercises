using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;


namespace PokerApplication
{
            
public class GameAtom
{   

    /*GameAtom:
        GameAtom  <---> Tournament
            : players_chips in/out
                (: eligible_players)
            : button_position ++
            : big_blind_size  func(total_gameatoms)
            [for strategy "known behavior"]
    
        GameAtom  <--->  Deck
            reset after each game

        GameAtom  <----> Hand
            River, post-bet
                winners <- evalWinner <- cards
            [strategy would use this ]

        GameAtom  <----> Betting
            : button_position

        Init
            starting_players
            players_chips

        Turns
            [Blinds]
            DealCards
            Betting
                -> FoldedPlayers
                    -> (Winner)
            [EvalHands]
                -> Winner(s)
        Resoltuion
            DivvyKitty
    */



    private int kitty;

    //private int min_bet_size;

    //private int button_position;

    //private int bigbet_size;

    private List<int> players_chips;
    private TurnName current_turn;

    private DeckClass gameDeck = new DeckClass();
    
    private List<List<string>> player_hole_cards = new List<List<string>>();
    private List<string> common_cards = new List<string>();

    private int num_players;
    
    private Logging L = new Logging();
    public enum TurnName
    {
        PreFlop,
        Flop,
        Turn,
        River
    }

    public void DoATurn()
    {
        //Cards
        switch(current_turn)
        {
            case TurnName.PreFlop:
                player_hole_cards.AddRange( gameDeck.dealHoleCards(num_players) );
                break;
            case TurnName.Flop:
                common_cards.AddRange( gameDeck.dealCommonCards(3) );
                break;
            case TurnName.River:
            case TurnName.Turn:
                common_cards.AddRange( gameDeck.dealCommonCards(1) );
                break;
        }

        if (current_turn == TurnName.PreFlop) {
            //DoBlinds(); 
        }
        
        //Betting.Betting( current_turn )   
            //note: betting starts pre-flop on follower of BB, but on LB afterwards

        if (current_turn == TurnName.River) {
            DivvyKitty(
                evalWinner(player_hole_cards,common_cards)
                ,ref players_chips); 
            }

    }

    public void setKitty(int inp)
    {
        kitty = inp;
    }
    
    public int getKitty()
    {
        return kitty;
    }

    public void DivvyKitty( List<int> inp_winners_ind,
                            ref List<int> players_chips )
    {
        int winning_chips = kitty / inp_winners_ind.Count;
        foreach (int ind in inp_winners_ind)
        {
            players_chips[ind] += winning_chips;
        }
        
    }

    public List<int> evalWinner(List<List<string>> playerHoleCards, List<string> commonCards)
    {

        /*returns: List of player(s) who are top hand in the game */

        HandClass hc = new HandClass();
        int playerLen = playerHoleCards.Count;
        List<int> ret = new List<int>() {};

        List<Tuple<int,int,List<int>>> eval_ret2 = new List<Tuple<int,int,List<int>>>()  ;
        List<int> evalHand = new List<int>() {};
        List<int> evalRank = new List<int>() {};
        List<List<int>> evalKickers = new List<List<int>>() {};
        
        foreach (List<string> _holeCards in playerHoleCards) 
        {
            eval_ret2.Add( hc.evaluateHands( _holeCards, commonCards) );
            evalHand.Add( hc.evaluateHands( _holeCards, commonCards).Item1);
            evalRank.Add( hc.evaluateHands( _holeCards, commonCards).Item2);
            evalKickers.Add( hc.evaluateHands( _holeCards, commonCards).Item3);
        }

        int maxHand = evalHand.Max();
        List<int> topHands = Enumerable.Range(0 ,evalHand.Count)
                            .Where(i => evalHand[i] == maxHand)
                            .ToList();

        if (topHands.Count == 1)
        {
            return topHands;            
        } else {
            int maxRank =evalRank.Max();
            List<int> topRanks = Enumerable.Range(0 ,topHands.Count)
                            .Where(i => (evalRank[i] == maxRank) & 
                                        (evalHand[i] == maxHand))
                            .ToList();
            if (topRanks.Count == 1)
            {
                return topRanks;            
            } else {
                
                List<List<int>> kickersLeft = new List<List<int>>();
                for (int h=0; h < topRanks.Count; h++) {
                    kickersLeft.Add(evalKickers[ topRanks[h] ] );
                }
                
                List<int> maxKickers = maxKicker( kickersLeft );
                
                List<int> topKickers = Enumerable.Range(0, evalHand.Count)
                                        .Where(i => (evalRank[i] == maxRank) &
                                            (evalHand[i] == maxHand) &
                                            (Enumerable.SequenceEqual(
                                                evalKickers[i], maxKickers)) )
                                        .ToList();
            
                if (topKickers.Count == 1)
                {
                    return topKickers;            
                } else {
                    
                    //Split Pot, not even kickers break the tie
                    return topKickers;
                }
            }
        }
    }


    public List<int> maxKicker(List<List<int>> inp)
    {
        
        //all kicker lists in inp should have same len
        int len = inp[0].Count;

        int indBest = 0;
        List<int> kickersBest = inp[0];
        
        for (int i= 1; i < inp.Count; i++)
        {
            if (betterKicker2(kickersBest,inp[i])) {
                indBest = i;
                kickersBest = inp[i];
            }    
        }    
        return kickersBest;
    }
        
     

    public bool betterKicker2(List<int> kick0, List<int> kick1)
    {
        int len = Math.Max( kick0.Count, kick1.Count );
        
        if (len == 0) return  true;  //no kicker yet
        
        for (int i = 0; i < len; i++) 
        {
            try { if (kick1[i] > kick0[i]) return true;}
            catch { return false; }   //if they're unequal lengths
            
        }
        return false;
    }


}
}
 