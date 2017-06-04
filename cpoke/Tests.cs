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

    //Misc functions
        List<int> a = new List<int>() {1,2};
        List<int> b = new List<int>() {1,2};
        tx = Enumerable.SequenceEqual(a.OrderBy(t =>t), b.OrderBy(t=>t));
        ResultsUtil(tx, print);
            
        List<int> c = new List<int>() {1,2};
        List<int> d = new List<int>() {1,3};
        tx = Enumerable.SequenceEqual(c.OrderBy(t =>t), d.OrderBy(t=>t));
        ResultsUtil(!tx, print);

        tx = Enumerable.SequenceEqual(a, b);
        ResultsUtil(tx, print);

    //There is a pair
        cards = new List<string> {"2|3","2|2"};
        cards2 = new List<string> {"5|1","6|3","7|2","10|2","11|1"};
        tx = TestHand(cards, cards2, 2, hc, HandClass.HandStrength.Pair );
        ResultsUtil(tx, print);

    //No Pairs
        cards = new List<string> {"1|3","2|2"};
        cards2 = new List<string> {"5|1","6|3","7|2","10|2","11|1"};
        tx = TestHand(cards, cards2, -1, hc, HandClass.HandStrength.Pair );
        ResultsUtil(!tx, print);

        tx = TestHand(cards, cards2, 0, hc, HandClass.HandStrength.HighCards );
        ResultsUtil(tx, print);

    //Test TwoPair
        cards = new List<string> {"0|3","1|2"};
        cards2 = new List<string> {"1|1","0|3","2|2","5|2","6|1"};
        tx = TestHand(cards,cards2,(100*1) + 0,hc,HandClass.HandStrength.TwoPair);
        ResultsUtil(tx, print);

    //Test Trips
        cards = new List<string> {"0|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","2|2","5|2","6|1"};
        tx = TestHand(cards,cards2,1,hc, HandClass.HandStrength.Trips);
        ResultsUtil(tx, print);
        //TestArrayInit();

    //Test Straight
        cards = new List<string> {"0|2","1|3"};
        cards2 = new List<string> {"2|2","3|3","4|2","7|0","8|0"};
        tx = TestHand(cards,cards2,4,hc,HandClass.HandStrength.Straight);
        ResultsUtil(tx, print);

        cards = new List<string> {"0|2","1|3"};
        cards2 = new List<string> {"2|2","3|3","9|2","7|0","12|0"};
        tx = TestHand(cards,cards2,3,hc,HandClass.HandStrength.Straight);
        ResultsUtil(tx, print);

        cards = new List<string> {"12|2","1|2"};
        cards2 = new List<string> {"11|2","10|3","9|2","8|0","12|1"};
        tx = TestHand(cards,cards2,12,hc,HandClass.HandStrength.Straight);
        ResultsUtil(tx, print);

        //high card from 6 card straight
        cards = new List<string> {"0|2","1|3"};
        cards2 = new List<string> {"2|2","3|3","4|2","7|0","12|0"};
        tx = TestHand(cards,cards2,4,hc,HandClass.HandStrength.Straight);
        ResultsUtil(tx, print);

    //Test Flush
        cards = new List<string> {"0|2","1|2"};
        cards2 = new List<string> {"1|2","1|3","2|2","5|2","6|2"};
        tx = TestHand(cards,cards2,0,hc,HandClass.HandStrength.Flush);
        ResultsUtil(tx, print);

    //Test FullHouse
        cards = new List<string> {"2|3","1|2"};
        cards2 = new List<string> {"1|1","1|3","2|2","5|2","6|1"};
        tx = TestHand(cards,cards2,(1*100) + 2,hc,HandClass.HandStrength.FullHouse);
        ResultsUtil(tx, print);

        cards = new List<string> {"2|3","7|2"};
        cards2 = new List<string> {"1|1","7|3","2|2","5|2","7|1"};
        tx = TestHand(cards,cards2,(7*100) + 2,hc,HandClass.HandStrength.FullHouse);
        ResultsUtil(tx, print);


    //Test FourOfAKind
        cards = new List<string> {"2|3","2|2"};
        cards2 = new List<string> {"1|1","1|3","2|0","2|2","6|1"};
        tx = TestHand(cards,cards2,2,hc,HandClass.HandStrength.FourOfAKind);
        ResultsUtil(tx, print);
        tx = TestHand(cards,cards2,6,hc, HandClass.HandStrength.FourOfAKind);
        ResultsUtil(!tx, print);

    //Test StraightFlush
         
        cards = new List<string> {"0|3","1|3"};
        cards2 = new List<string> {"2|3","3|3","4|3","7|0","8|0"};
        tx = TestHand(cards,cards2,4,hc,HandClass.HandStrength.StraightFlush);
        ResultsUtil(tx, print);
 
        //acelow
        cards = new List<string> {"0|1","1|1"};
        cards2 = new List<string> {"2|1","3|1","9|2","7|0","12|1"};
        tx = TestHand(cards,cards2,3,hc,HandClass.HandStrength.StraightFlush);
        ResultsUtil(tx, print);

        cards = new List<string> {"12|2","1|2"};
        cards2 = new List<string> {"11|2","10|2","9|2","8|2","12|1"};
        tx = TestHand(cards,cards2,12,hc,HandClass.HandStrength.StraightFlush);
        ResultsUtil(tx, print);

        //straight and flush but not straight flush
        cards = new List<string> {"12|2","1|2"};
        cards2 = new List<string> {"11|2","10|2","9|2","8|0","12|1"};
        tx = TestHand(cards,cards2,12,hc,HandClass.HandStrength.StraightFlush);
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

        cards = new List<string> {"0|3","1|2"};
        cards2 = new List<string> {"1|1","0|3","2|2","5|2","6|1"};
        tx = TestKickers(cards,cards2,6,0,hc);
        ResultsUtil(tx, print);

        //BUG? - Better kicker but on a lower [two]pair bug?
        cards = new List<string> {"2|3","2|1"};    
        cards2 = new List<string> {"6|1","0|3","3|2","4|2","6|1"};    
        tx = TestKickers(cards,cards2,4,0,hc);
        ResultsUtil(tx, print);
        cards = new List<string> {"6|3","6|1"};    
        cards2 = new List<string> {"2|1","0|3","3|2","4|2","2|1"};    
        tx = TestKickers(cards,cards2,4,0,hc);
        ResultsUtil(tx, print);
        cards = new List<string> {"6|3","6|1"};    
        cards2 = new List<string> {"2|1","1|3","3|2","2|2","4|1"};    
        tx = TestKickers(cards,cards2,4,0,hc);
        ResultsUtil(tx, print);

        //test HighCards kickers
        cards = new List<string> {"2|3","3|1"};    
        cards2 = new List<string> {"5|1","6|3","7|2","0|2","11|1"};    
        tx = TestKickers(cards,cards2,11,0,hc);
        ResultsUtil(tx, print);

        tx = TestKickers(cards,cards2,3,4,hc);
        ResultsUtil(tx, print);
        

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

        
    //Game Class
        Game g = new Game();

        List<List<string>> playerHoleCards = new List<List<string>>();
        List<string> player1 = new List<string> {"2|3","1|2"};
        List<string> player2 = new List<string> {"2|3","2|2"};
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        List<string> commonCards = new List<string> {"1|1","3|3","2|0","2|2","6|1"};

        
        //test better hand wins
        List<int> ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 1);
        ResultsUtil(tx, print);

        //test better rank wins
        player1 = new List<string> {"7|3","7|2"};
        player2 = new List<string> {"6|3","6|2"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"1|1","3|3","2|0","2|2","5|1"};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 0);
        ResultsUtil(tx, print);

        //test better kickers wins
        player1 = new List<string> {"6|3","10|2"};
        player2 = new List<string> {"6|3","9|2"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"1|1","3|3","2|0","2|2","6|1"};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 0);
        ResultsUtil(tx, print);

        //test better second-kicker wins
        player1 = new List<string> {"6|3","8|2"};
        player2 = new List<string> {"6|3","9|2"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"1|1","3|3","2|0","10|2","11|1"};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 1);
        ResultsUtil(tx, print);

        //test better kicker in worse hand loses
        player1 = new List<string> {"6|3","12|2"};
        player2 = new List<string> {"5|3","5|2"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"1|1","3|3","5|0","6|2","11|1"};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 1);
        ResultsUtil(tx, print);


        //test better flush kicker wins
        player1 = new List<string> {"7|0","8|0"};
        player2 = new List<string> {"6|0","9|0"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"1|1","1|0","2|0","10|0","11|0"};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestWinner(ret2, 1);
        ResultsUtil(tx, print);

        //test 6th-best kicker in flush doesn't matter
        player1 = new List<string> {"1|0","4|0"};
        player2 = new List<string> {"2|0","0|0"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        commonCards = new List<string> {"6|0","7|0","8|0","10|0","11|0"};
        List<int> exp_ret2 = new List<int>() {0,1};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestPotSplit(ret2, exp_ret2);
        ResultsUtil(tx, print);

        //test high card pot-split
        //test pot split 3-way with fourhands
        List<string> player3, player4;
        player1 = new List<string> {"1|0","4|0"};
        player2 = new List<string> {"2|0","4|0"};
        player3 = new List<string> {"2|3","1|1"};
        player4 = new List<string> {"1|2","4|1"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        playerHoleCards.Add(player3);
        playerHoleCards.Add(player4);
        commonCards = new List<string> {"0|1","7|1","8|0","10|0","11|2"};
        exp_ret2 = new List<int>() {0,1,3};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestPotSplit(ret2, exp_ret2);
        ResultsUtil(tx, print);

        //test potsplit for board beats all hands
        player1 = new List<string> {"1|0","4|0"};
        player2 = new List<string> {"2|0","4|0"};
        player3 = new List<string> {"2|3","1|1"};
        player4 = new List<string> {"1|2","4|1"};
        playerHoleCards = new List<List<string>>();
        playerHoleCards.Add(player1);
        playerHoleCards.Add(player2);
        playerHoleCards.Add(player3);
        playerHoleCards.Add(player4);
        commonCards = new List<string> {"5|1","7|1","8|0","10|0","11|2"};
        exp_ret2 = new List<int>() {0,1,3,2};
        ret2 = g.evalWinner(playerHoleCards,commonCards);
        tx = TestPotSplit(ret2, exp_ret2);
        ResultsUtil(tx, print);

    //Kitty splitting
        List<int> playersChips = new List<int>() {10,10};
        g.setKitty(49);
        exp_ret2 = new List<int>() {0};
        g.DivvyKitty(exp_ret2 ,ref playersChips);
        tx = (playersChips[0] == 59) ? true : false;
        ResultsUtil(tx, print);

        //TestPotSplit
        playersChips = new List<int>() {10,10,10};
        List<int> expPlayersChips = new List<int>() {34,34,10};
        g.setKitty(49);
        exp_ret2 = new List<int>() {0,1};
        g.DivvyKitty(exp_ret2 ,ref playersChips);
        tx = TestPlayerChip(playersChips, expPlayersChips);
        ResultsUtil(tx, print);


        Console.WriteLine(" ----------------------------------------------------- ");
        PrintOutResults();
        return 1;
    }

        public bool TestPlayerChip( List<int> inp_chips, List<int> exp_chips)
        {
            for (int i = 0; i< inp_chips.Count; i++)
            {
                if (inp_chips[i] != exp_chips[i]) return false;
            }
            return true;
        }
        public bool TestWinner( List<int> listWinners, int expWinner)
        {
            if (listWinners.Count() == 1) return (listWinners[0] == expWinner );
            return false;
        }

        public bool TestPotSplit( List<int> listWinners, List<int> expWinners)
        {
            foreach (int ew in expWinners) {
                if (!listWinners.Any(i => i == ew)) return false;   
            }
            foreach (int lw in listWinners) {
                if (!expWinners.Any(i => i == lw)) return false;   
            }
            return true;
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

        

        public bool TestHand(List<string> inp_holeCards,
                                List<string> inp_commonCards,
                                int exp_result,
                                HandClass inp_hc,
                                HandClass.HandStrength exp_hs )
        {
            var _hs = inp_hc.evaluateHands(inp_holeCards,inp_commonCards);

            bool isTrips = _hs.Item1 == (int) exp_hs;

            bool isNumber =  _hs.Item2 == exp_result;
            
            if (isTrips & isNumber) return true;
            return false;

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