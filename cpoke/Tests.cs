using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace PokerApplication
{
    public class TestClass
    {

        public List<Tuple<int,bool>> Results = new List<Tuple<int,bool>>();
    
        public int RunTests(string[] args)
        {
        
        bool print = false;
        if (args[0] == "PrintThere") {
            Console.WriteLine("Start Tests");
            print = true;
        } 
        
        HandClass hc = new HandClass();


        List<string> cards;
        List<string> cards2;
        //List<string> cards3;

        Results = new List<Tuple<int,bool>>();
        bool tx;


        
    //There is a pair
        cards = new List<string> {"2|3","2|2"};
        tx = TestPairs(cards, 2, hc );
        ResultsUtil(tx, print);

    //No Pairs
        cards = new List<string> {"1|3","2|2"};
        tx = TestPairs(cards, -1, hc );
        ResultsUtil(tx, print);

    //Ignore Lower pair - 2's over 1's
        cards = new List<string> {"1|3","2|2"};
        cards2 = new List<string> {"2|1","1|2","4|2","5|2","6|1"};
        tx = TestIgnoreLowPair(cards, cards2, 2, hc );
        ResultsUtil(tx, print);

        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"2|1","1|2","4|2","5|2","6|1"};
        tx = TestIgnoreLowPair(cards, cards2, 2, hc );
        ResultsUtil(tx, print);

        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"1|1","2|2","4|2","5|2","6|1"};
        tx = TestIgnoreLowPair(cards, cards2, 2, hc );
        ResultsUtil(tx, print);

    //Trips, not a pair, should return tx=false
        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","4|2","5|2","6|1"};
        tx = TestIgnoreLowPair(cards, cards2, 2, hc );
        ResultsUtil(!tx, print);
    
    //Crappola, not even a pair
        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"5|1","6|3","7|2","10|2","11|1"};
        tx = TestNotEvenPair(cards, cards2, -1, hc );
        ResultsUtil(tx, print);

    //Test TwoPair

    //Test Trips
        cards = new List<string> {"0|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","2|2","5|2","6|1"};
        tx = TestTrips(cards,cards2,1,hc);
        ResultsUtil(tx, print);
        //TestArrayInit();

    //Test FullHouse
        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","2|2","5|2","6|1"};
        tx = TestFullHouse(cards,cards2,(1*100) + 2,hc);
        ResultsUtil(tx, print);

        cards = new List<string> {"2|3","7|2"};
        cards2 = new List<string> {"1|1","7|3","2|2","5|2","7|1"};
        tx = TestFullHouse(cards,cards2,(7*100) + 2,hc);
        ResultsUtil(tx, print);


    //Test FourOfAKind
        cards = new List<string> {"2|3","2|2"};
        cards2 = new List<string> {"1|1","1|3","2|0","2|2","6|1"};
        tx = TestFourOfAKind(cards,cards2,2,hc);
        ResultsUtil(tx, print);
        tx = TestFourOfAKind(cards,cards2,6,hc);
        ResultsUtil(!tx, print);

    //Test Kickers
        cards = new List<string> {"2|3","5|1"};    
        cards2 = new List<string> {"5|1","6|3","7|2","4|2","11|1"};    
        
        tx = TestKickers(cards,cards2,11,0,hc);
        ResultsUtil(tx, print);

        tx = TestKickers(cards,cards2,7,1,hc);
        ResultsUtil(tx, print);

        tx = TestKickers(cards,cards2,6,2,hc);
        ResultsUtil(tx, print);

    //BUG?
        //Better kicker but on a lower [two]pair bug?
        /*
        cards = new List<string> {"2|3","5|1"};    
        cards2 = new List<string> {"5|1","6|3","7|2","4|2","11|1"};    
        tx = TestKickers(cards,cards2,11,0,hc);
        ResultsUtil(tx, print);
        cards = new List<string> {"2|3","5|1"};    
        cards2 = new List<string> {"5|1","6|3","7|2","4|2","11|1"};    
        tx = TestKickers(cards,cards2,11,0,hc);
        ResultsUtil(tx, print);
        */

        //test kickers with trips
        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","3|2","5|2","6|1"};

        tx = TestKickers(cards,cards2,6,0,hc);
        ResultsUtil(tx, print);

        tx = TestKickers(cards,cards2,5,1,hc);
        ResultsUtil(tx, print);

        tx = TestKickers(cards,cards2,3,2,hc);
        ResultsUtil(!tx, print);    //trips dont have a thrid kicker, tx should be false

        //test kickers with fourofakind
        cards = new List<string> {"2|3","2|2"};
        cards2 = new List<string> {"1|1","3|3","2|0","2|2","6|1"};
        tx = TestKickers(cards,cards2,6,0,hc);
        ResultsUtil(tx, print);
        tx = TestKickers(cards,cards2,3,1,hc);
        ResultsUtil(!tx, print);     //quads dont have a 2nd kicker


    //Build the kicker module...
    //Logging L = new Logging();
    //cards = new List<string> {"2|3","1|2"};    
    //cards2 = new List<string> {"5|1","6|3","7|2","5|2","11|1"};
    //Tuple<int, List<int>> DemIn = hc.allPairs(cards2);
    //Console.WriteLine("The Kickers:");
    //L.PrintOut(DemIn.Item2);            

    Console.WriteLine(" ----------------------------------------------------- ");

        PrintOutResults();
        return 1;
    }

        public bool TestKickers(  List<string> inp_holeCards,
                                      List<string> inp_commonCards,
                                      int kicker_val,
                                      int kicker_ind,
                                      HandClass inp_hc )
        {
            
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);
            
            List<int> kickers = _hs.Item3;
            int ki;
            
            try {
                ki = kickers[kicker_ind];
            } 
            catch {
                return false;
            }
            
            return (ki == kicker_val);
        }


        public void ResultsUtil(bool x, bool print = false)
        {
            //Called after Results have been updated
            if (print & !x) {
                Console.WriteLine("False at Test Num" + Convert.ToString(Results.Count));
            }
            Results.Add( Tuple.Create( Results.Count + 1, x));
        }

        public bool TestNotEvenPair(  List<string> inp_holeCards,
                                      List<string> inp_commonCards,
                                      int exp_result,
                                      HandClass inp_hc )
        {
            
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);
            return _hs.Item1 == exp_result;
            
        }

        public bool TestIgnoreLowPair(List<string> inp_holeCards,
                                      List<string> inp_commonCards,
                                        int exp_result,
                                        HandClass inp_hc )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);

            bool isPair = _hs.Item1 == (int) HandClass.HandStrength.Pair;

            if (isPair) return _hs.Item2 == exp_result;
            return false;
        }

        public bool TestTrips(List<string> inp_holeCards,
                                List<string> inp_commonCards,
                                int exp_result,
                                HandClass inp_hc )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);

            bool isTrips = _hs.Item1 == (int) HandClass.HandStrength.Trips;

            bool isNumber =  _hs.Item2 == exp_result;
            
            if (isTrips & isNumber) return true;
            return false;

        }

        public bool TestFullHouse(List<string> inp_holeCards,
                                List<string> inp_commonCards,
                                int exp_result,
                                HandClass inp_hc )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);

            bool isHand = _hs.Item1 == (int) HandClass.HandStrength.FullHouse;

            //Fullhouse exp_reult: 100*(Trips-card-rank) + 1*(pair-card-rank)

            bool isNumber =  _hs.Item2 == exp_result;
            
            if (isHand & isNumber) return true;
            return false;

        }

        public bool TestFourOfAKind(List<string> inp_holeCards,
                                    List<string> inp_commonCards,
                                    int exp_result,
                                    HandClass inp_hc )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);

            bool isTrips = _hs.Item1 == (int) HandClass.HandStrength.FourOfAKind;

            bool isNumber =  _hs.Item2 == exp_result;
            
            if (isTrips & isNumber) return true;
            return false;

        }
            
        public bool TestPairs(List<string> inp_cards,
                              int exp_result,
                              HandClass inp_hc )
        {    
            Tuple<int,List<int>> ret = inp_hc.highNSet(inp_cards, 2);
            
            return (ret.Item1 == exp_result); 
            
        }

        public void PrintOutResults()
        {
            
            StringBuilder builder = new StringBuilder();
            int cntr = 0;
            
            Console.WriteLine("Out of Tests: " + Convert.ToString(Results.Count));

            foreach (var item in Results)
            {
                string s_item1 = Convert.ToString(item.Item1);
                string s_item2 = Convert.ToString(item.Item2);
                string s_item = s_item1 + " - " + s_item2;
                builder.Append(s_item).Append("\n");
                
                if (item.Item2 == true) cntr+= 1;
            }
            
            Console.WriteLine("Passed: " + Convert.ToString(cntr));
            
            string sData = builder.ToString();    
            Console.WriteLine(sData );

        }

    }
}