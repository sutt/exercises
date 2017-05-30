using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;


namespace PokerApplication
{
            
public class Game
{

    private int kitty;

    //private int min_bet_size;

    //private int button_position;

    //private int bigbet_size;


    public static bool hello = true;

    public static bool RunGame()
    {
        DeckClass deck = new DeckClass();
        //deck.dealHoleCards();
        
        return hello;
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
 