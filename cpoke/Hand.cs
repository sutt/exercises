using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

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

        
        public int evaluateHands( List<string> holeCards, List<string> commonCards)
        {
            List<List<string>> _hands = allHands(holeCards, commonCards);
            
            int HighPair = -1;
            int HighTrip = -1;

            foreach (List<string> _hand in _hands)
            {
                List<int> pairs = allPairs(_hand);
                if (pairs.Count() > 0) {
                    int _highPair = pairs.Max();
                    if (_highPair > HighPair) HighPair = _highPair;
                }

                List<int> trips = allTrips(_hand);
                if (trips.Count() > 0) {
                    int _highTrip = trips.Max();
                    if (_highTrip > HighTrip) HighTrip = _highTrip;
                }

            }

            return 1;
        }

        public List<int> allPairs(List<string> _cards)
        {
            List<int> ret = new List<int>();
            
            return ret;
        }

        public List<int> allTrips(List<string> _cards)
        {
            List<int> ret = new List<int>();

            return ret;
        }

    }
}