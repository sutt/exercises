using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//using System.Math;


namespace PokerApplication
{

public class HandClass
{

    public List<List<int>> combos = allCombos();
    public List<List<int>> getCombos() {return combos;}
    
    public static List<List<int>> allCombos()
    {
        var ret = new List<List<int>>();
        int N = 7;
        
        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                
                    if (j == i) continue;

                    List<int> allcards = Enumerable.Range(0,N).ToList();
                
                    allcards.Remove(i);
                    allcards.Remove(j);

                    ret.Add(allcards);
            }
            
        }
        return ret;
    }

    public List<List<string>> allHands(List<string> _hole, 
                                        List<string> _common)
    {
        List<List<string>> ret = new List<List<string>>();

        List<string> c = new List<string>();
        c.AddRange(_hole);
        c.AddRange(_common);
        
        foreach (List<int> combo in combos)
        {
            List<string> this_hand = new List<string>();
            foreach (int ind in combo)
            {
                this_hand.Add( c.ElementAt(ind) );
            }
            ret.Add(this_hand);
        }
        return ret;
    }

    public enum HandStrength 
    {
        Pair,
        TwoPair,
        Trips,
        Straight,
        Flush,
        FullHouse,
        FourOfAKind,
        StraightFlush
    }            

    
    public void TrackRankAndKicker( int hsIndex,
                                    Tuple<int,List<int>> inputHand,
                                    ref int[] globalHS, 
                                    ref List<int>[] globalKickers )
    {
        int _rank = inputHand.Item1;
        int currentRank = globalHS[hsIndex];
        if (_rank > currentRank) 
        {
            globalHS[hsIndex] = _rank;
            globalKickers = CompareKickers2(true,globalKickers, inputHand.Item2, hsIndex);
        }
        if (_rank == currentRank) 
        {
            globalKickers = CompareKickers2(false,globalKickers, inputHand.Item2, hsIndex);
        }
        
    }

    public List<int>[] CompareKickers2( bool higherRank,
                                       List<int>[] kickers,
                                       List<int> inputKickers,
                                       int indexHs )
    {
        if ( (kickers[indexHs] == (null)) | higherRank)
        {
            kickers[indexHs] = inputKickers;
        }
        if (betterKicker(kickers[indexHs], inputKickers))
        {
            kickers[indexHs] = inputKickers;
        }
        return kickers;
    }
     


    public bool betterKicker(List<int> kick0, List<int> kick1)
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

    public Tuple<int,int,List<int>> evaluateHands( List<string> holeCards, 
                                                    List<string> commonCards)
    {
        //returns: int best-hand-type, the int of highest HandStrength of all possible hands
        //          int type-rank: highest , high card for flush and straight, card-of for n-of-a-kind
        //          List<int> kickers: remaining cards not used, ordered highest ton lowest                      
        
        List<List<string>> _hands = allHands(holeCards, commonCards);

        int _hsLen = System.Enum.GetValues(typeof(HandStrength)).Length;

        int[] _hs = new int[_hsLen] ;
        for (int i = 0; i < _hsLen; i++) { _hs[i] = -1;  }

        List<int>[] _hsKicker = new List<int>[_hsLen];

        
        Tuple<int,List<int>> myHand;

        foreach (List<string> _hand in _hands)
        {
            
            myHand = highNSet(_hand, 2);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Pair, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = highNSet(_hand, 3);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Trips, myHand,ref _hs, ref _hsKicker); 
            }

            //TODO: does populating the arguments take time?, worth exiting the function on -1 item1?
            //TODO: twopair
            //TODO: highNMSetRank(_hand, N, M); need kick for twopair
            //Tuple<int,List<int>> houseHand = highHouse(_hand);
            myHand = highHouse(_hand);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.FullHouse, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = highNSet(_hand, 4);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.FourOfAKind, myHand,ref _hs, ref _hsKicker); 
            }
            
        }

        int _topHand = -1;
        for (int i = 0; i < _hsLen; i++)
        {
            if (_hs[i] > -1) _topHand = i;
        }
        
        int _topHandNum = -1;
        if (_topHand > -1) _topHandNum = _hs[_topHand];

        //TODO: make high-card handclass index =0
        List<int> _topKickers;
        if (_topHand > -1) {
             _topKickers= _hsKicker[_topHand];
        } else {
            _topKickers = new List<int>();
        }

        Tuple<int,int,List<int>> bestHand = 
            Tuple.Create(_topHand,_topHandNum,_topKickers);

        return bestHand;
        
    }


    public List<int> getCardNums(List<string> inp_cards)
    {
        List<int> ret = new List<int>();
        foreach (string c in inp_cards) {
            ret.Add( Convert.ToInt32( c.Split('|')[0] ));
        }
        return ret;
    }


    public Tuple<int,List<int>> highNSet(List<string> _cards, int N)
    {
        //Returns Tuple( card-rank, List-of-kickers)
        //      highest card-rank where _cards have an N-set, e.g N=2 is pair
        //      List of kickers as integers in descending order

        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        List<int> num_cards = getCardNums(_cards);

        for (int i = 0; i <= 12; i++)
        {   
            if (num_cards.FindAll( s => s == i ).Count() == N) 
            {
                List<int> kickers = num_cards.FindAll( s => s != i );
                List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                ret = Tuple.Create( i , descKickers  );
            }
        }
        return ret;
    }
    
    public Tuple<int,List<int>> highHouse(List<string> _cards)
    {
        //Returns Tuple( house-rank, List-of-kickers)
        //      highest card-rank where _cards have an N-set, e.g N=2 is pair
        //      empty List<int>, full house has no kickers

        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        Tuple<int,List<int>> houseHand = highNSet(_cards, 3);
            if (houseHand.Item1 > -1)
            {
                int tripOfHouse = houseHand.Item1;
                
                List<string> remainingCards = new List<string>();
                foreach (int i_card in houseHand.Item2)
                {
                    remainingCards.Add(  Convert.ToString(i_card) );
                }
                
                Tuple<int,List<int>> houseHand2 = highNSet(remainingCards, 2);
                if (houseHand2.Item1 > -1)
                {
                    int pairOfHouse = houseHand2.Item1;
                    int houseRank = 100*tripOfHouse + pairOfHouse;
                    ret = Tuple.Create(houseRank, new List<int>());
                }
            }
        return ret;
    }


}
}