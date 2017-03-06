using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//using System.Math;


namespace PokerApplication
{
    public class HandClass
    {

        public  List<List<int>> combos = allCombos();
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
            Trips,
            Straight,
            Flush,
            FullHouse,
            FourOfAKind,
            StraightFlush
        }        

        public Tuple<int,int,List<string>> evaluateHands( List<string> holeCards, 
                                                            List<string> commonCards)
        {
            List<List<string>> _hands = allHands(holeCards, commonCards);

            int hs_len = System.Enum.GetValues(typeof(HandStrength)).Length;
            int[] _HandStrength = new int[hs_len] ;
            for (int i = 0; i < hs_len; i++)
            {
                _HandStrength[i] = -1;
            }

            
            foreach (List<string> _hand in _hands)
            {
                List<int> pairs = allPairs(_hand);
                if (pairs.Count() > 0) {
                    int _high = pairs.Max();
                    _HandStrength[(int)HandStrength.Pair] = 
                        Math.Max(_high,
                                 _HandStrength[(int)HandStrength.Pair]);
                }

                //TODO: these can be  made into functions stndard functions
                List<int> trips = allTrips(_hand);
                if (trips.Count() > 0) {
                    int _high = trips.Max();
                    _HandStrength[(int)HandStrength.Trips] = 
                        Math.Max(_high,
                                 _HandStrength[(int)HandStrength.Trips]);
                }
            }

            int _topHand = -1;
            for (int i = 0; i < hs_len; i++)
            {
                if (_HandStrength[i] > -1) _topHand = i;
            }
            
            int _topHandNum = -1;
            if (_topHand > -1) _topHandNum = _HandStrength[_topHand];

            List<string> temp = new List<string>();
            Tuple<int,int,List<string>> bestHand = 
                Tuple.Create(_topHand,_topHandNum,temp);

            return bestHand;
            
        }

        

        public List<string> getCardNums(List<string> inp_cards)
        {
            List<string> ret = new List<string>();
            foreach (string c in inp_cards) {
                ret.Add(c.Split('|')[0]);
            }
            return ret;
        }

        public List<int> allPairs(List<string> _cards)
        {
            List<int> ret = new List<int>();
            List<string> num_cards = getCardNums(_cards);

            for (int i = 0; i <= 12; i++)
            {
                string s_i = Convert.ToString(i);
                if (num_cards.FindAll( s => s.Equals(s_i) ).Count() == 2) {
                    ret.Add(i);
                }
            }
            return ret;
        }

        public List<int> allTrips(List<string> _cards)
        {
            List<int> ret = new List<int>();
            List<string> num_cards = getCardNums(_cards);

            for (int i = 0; i <= 12; i++)
            {
                string s_i =Convert.ToString(i);
                
                if (num_cards.FindAll( s => s.Equals(s_i) ).Count() == 3) {
                    ret.Add(i);
                }
            }
            return ret;
        }

    }
}