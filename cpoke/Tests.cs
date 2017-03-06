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
    
        //TestArrayInit();

        PrintOutResults();
        return 1;
    }

        enum MyEnum
        {
            num1,
            num2,
            num3
        }

        public void TestArrayInit()
        {
            int[] _arr = new int[(System.Enum.GetValues(typeof(MyEnum)).Length)];
            foreach (int i in _arr)
            {
                Console.WriteLine(Convert.ToString(i));
            }

            Console.WriteLine(Convert.ToString(_arr[2] > -1));
        }

        public void ResultsUtil(bool x, bool print = false)
        {
            //Called after Results have been updated
            if (print & !x) {
                Console.WriteLine("False at Test Num" + Convert.ToString(Results.Count));
            }
            Results.Add( Tuple.Create( Results.Count + 1, x));
        }

        public bool TestIgnoreLowPair(List<string> inp_holeCards,
                                      List<string> inp_commonCards,
                                        int exp_result,
                                        HandClass inp_hc )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);
            
            

            bool isPair = _hs.Item1 == (int) HandClass.HandStrength.Pair;

            if (isPair) {
                bool ret = _hs.Item2 == exp_result;
                return ret;
            } else {
            return false;
            }
        }

            
        public bool TestPairs(List<string> inp_cards,
                              int exp_result,
                              HandClass inp_hc )
        {    
            List<int> ret = inp_hc.allPairs(inp_cards);
            
            if (ret.Count > 0) return (ret.Max() == exp_result); 
            if (ret.Count == 0) {
                try {
                    int temp = ret.Max();
                }
                catch (InvalidOperationException)
                {
                    //no pairs; no max
                    return (exp_result == -1);
                }
            }
            return false;  //should not get here
            
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