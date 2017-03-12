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

    public bool betterKicker(List<int> kick0, List<int> kick1)
    {
        int len = Math.Max( kick0.Count, kick1.Count );
        
        if (len == 0) return  true;  //no kicker yet
        
        for (int i = 0; i < len; i++) 
        {
            try {
            if (kick1[i] > kick0[i]) return true;
            }
            catch {
                return false;   //if they're unequal lengths
            }
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
        List<int>[] _hsKicker = new List<int>[_hsLen];
        for (int i = 0; i < _hsLen; i++) { _hs[i] = -1;  }
        
        List<int> _kickers = new List<int>();

        //TODO: these should proceed backwards, ignore processing lower hands
        //TODO: individual hand types can be abstracted further
        //TODO: only 5 cards in hand, so cutoff kickers after 3 cards for pair, etc.
        //TODO: add kicker evaluation
        //TODO: this could all be a hash lookup with preprocessing?
        foreach (List<string> _hand in _hands)
        {
            
            Tuple<int,List<int>> pairHand = allPairs(_hand);
            if (pairHand.Item1 > -1)
                {

                    _hs[(int)HandStrength.Pair] = Math.Max(pairHand.Item1,
                                                            _hs[(int)HandStrength.Pair]);
                    List<int> _qq = NewMethod(_hsKicker);
                    if (_qq == (null))
                    {
                        _hsKicker[(int)HandClass.HandStrength.Pair] = pairHand.Item2;
                    }

                    if (betterKicker(_hsKicker[(int)HandStrength.Pair], pairHand.Item2))
                    {
                        _hsKicker[(int)HandClass.HandStrength.Pair] = pairHand.Item2;
                    }

                }



                Tuple<int,List<int>> tripHand = allTrips(_hand);
            if (tripHand.Item1 > -1) {
                
                _hs[(int)HandStrength.Trips] = Math.Max(tripHand.Item1, 
                                                        _hs[(int)HandStrength.Trips]);
                _kickers = pairHand.Item2;
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

        private static List<int> NewMethod(List<int>[] _hsKicker)
        {
            return _hsKicker[(int)HandStrength.Pair];
        }


        public List<int> getCardNums(List<string> inp_cards)
    {
        List<int> ret = new List<int>();
        foreach (string c in inp_cards) {
            ret.Add( Convert.ToInt32( c.Split('|')[0] ));
        }
        return ret;
    }


    public Tuple<int,List<int>> allPairs(List<string> _cards)
    {
        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        List<int> num_cards = getCardNums(_cards);

        for (int i = 0; i <= 12; i++)
        {   
            if (num_cards.FindAll( s => s == i ).Count() == 2) {
                
                List<int> kickers = num_cards.FindAll( s => s != i );
                List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                ret = Tuple.Create( i , descKickers  );
            }
        }
        return ret;
    }



    public Tuple<int,List<int>> allTrips(List<string> _cards)
    {
        Tuple<int,List<int>> ret = Tuple.Create(-1,new List<int>());
        
        List<int> num_cards = getCardNums(_cards);

        for (int i = 0; i <= 12; i++)
        {   
            if (num_cards.FindAll( s => s == i ).Count() == 3) {
                
                List<int> kickers = num_cards.FindAll( s => s != i );
                List<int> descKickers = kickers.OrderByDescending(p => p).ToList();
                ret = Tuple.Create( i , descKickers  );
            }
        }
        return ret;
    }

}
}