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
        //          int type-rank: highest, high card for straight,ca code for n,m  n-of-a-kind, 100*trip-in-fullhouse+pair-in-fullhouse
        //          List<int> kickers: remaining cards not used, ordered highest ton lowest,                       
        
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
            
            myHand = highNMSetRank(_hand,2,2);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.TwoPair, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = highNSet(_hand, 3);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Trips, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = runOfN(_hand,5);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Straight, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = runOfN(aceLow(_hand),5);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Straight, myHand,ref _hs, ref _hsKicker); 
            }

            myHand = matchSuit(_hand, 5);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.Flush, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = highNMSetRank(_hand,3,2);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.FullHouse, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = highNSet(_hand, 4);
            if (myHand.Item1 > -1) 
            {
                TrackRankAndKicker( (int)HandStrength.FourOfAKind, myHand,ref _hs, ref _hsKicker); 
            }
            
            myHand = matchSuitRunOfN(_hand, 5);
            {
                TrackRankAndKicker( (int)HandStrength.StraightFlush, myHand,ref _hs, ref _hsKicker); 
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

    public List<int> getCardSuits(List<string> inp_cards)
    {
        List<int> ret = new List<int>();
        foreach (string c in inp_cards) {
            ret.Add( Convert.ToInt32( c.Split('|')[1]));
        }
        return ret;
    }

    public List<string> aceLow(List<string> inp_cards)
    {
        List<string> ret = new List<string>();
        foreach (string s in inp_cards) {
            string num = s.Split('|')[0];
            string suit = s.Split('|')[1];
            if (num == "12") {
                ret.Add("-1"+"|"+suit );
            } else {
                ret.Add(num+"|"+suit );
            }
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
    
    public Tuple<int,List<int>> highNMSetRank(List<string> _cards, int N, int M)
    {
        //Returns Tuple( house-rank, List-of-kickers)
        //      highest card-rank where _cards have an N-set and an M-set
        //      kickers only if if N+M < cards
        //      for two pair, tripofhouse will be higher of the pairs, thus being the 100x in the code

        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());

        List<int> num_cards = getCardNums(_cards);
        
        Tuple<int,List<int>> myHand = highNSet(_cards, N);
            if (myHand.Item1 > -1)
            {
                int tripOfHouse = myHand.Item1;
                
                List<string> remainingCards = new List<string>();
                foreach (int i_card in myHand.Item2)
                {
                    remainingCards.Add(  Convert.ToString(i_card) );
                }
                
                Tuple<int,List<int>> myHand2 = highNSet(remainingCards, 2);
                if (myHand2.Item1 > -1)
                {
                    int pairOfHouse = myHand2.Item1;
                    int houseRank = 100*tripOfHouse + pairOfHouse;

                    List<int> kickers = myHand2.Item2.FindAll( s => s != pairOfHouse );
                    List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                    ret = Tuple.Create(houseRank , descKickers);
                }
            }
        return ret;
    }

    public Tuple<int,List<int>> matchSuit(List<string> _cards, int N)
    {
        //Returns Tuple( 0, List-of-kickers)
        //      any flush returns a rank of zero, all suits have equal worth
        //      flush-high is simply all five kickers to compare to another flush
        //      this will cause kickers to be reassesed each time a flush is found in combos
        // edge case: board flush beats player1 but player to beats the 5th high card from board

        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        List<int> suit_cards = getCardSuits(_cards);

        for (int i = 0; i <= 3; i++)
        {   
            if (suit_cards.FindAll( s => s == i ).Count() == N) 
            {
                List<int> kickers = getCardNums(_cards); 
                List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                ret = Tuple.Create( 0 , descKickers  );
            }
        }
        return ret;
    }

    public Tuple<int,List<int>> runOfN(List<string> _cards, int N)
    {
        //Returns Tuple( card-rank, List-of-kickers)
        //      highest card-rank where highest of straight is returned as rank
        //      full list of kickers, but they are irrelevant 

        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        List<int> num_cards = getCardNums(_cards);

        for (int i = -1; i <= 12+1-N; i++)
        {   
            bool[] running = new bool[N];
            for (int j = 0; j < N; j++)
            {
                if (num_cards.FindAll( s => s == i + j ).Count() == 1) running[j] = true;
            }
            if (running.All(e => e == true))
            {
                List<int> kickers = num_cards;
                List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                ret = Tuple.Create( i + N -1 , descKickers  );
            }
        }
        return ret;
    }



    public Tuple<int,List<int>> matchSuitRunOfN(List<string> _cards, int N)
    {
    
        if (matchSuit(_cards,N).Item1 > -1) 
        {
            if (runOfN(_cards, N).Item1 > -1) return runOfN(_cards, N);
            if (runOfN(aceLow(_cards), N).Item1 > -1) return runOfN(aceLow(_cards), N);
        }
        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        return ret;
    }

}
}