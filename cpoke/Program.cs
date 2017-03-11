using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;


namespace PokerApplication
{
            
    public class Program
    {
        public static void Main(string[] args)
        {
            bool runTest = true;
            if (runTest) {
                TestClass tc = new TestClass();
                string[] my_args = {"PrintThere"};

                tc.RunTests(my_args);
                return;

                

            }
            Logging L = new Logging();
            
            // ---- Deal Cards -----------------
            Console.WriteLine("Deal me in, dealer!");
            DeckClass D = new DeckClass();
            Console.WriteLine("Cards in the deck: " 
                               + Convert.ToString( D.getDeck().Count() ) );
            L.PrintOut(D.getDeck() , "Your deck, sir: ");
            
            List<string> holeCards = D.dealHoleCards(1);
            List<string> commonCards = D.dealCommonCards();

            L.PrintOut(holeCards,"Hole Cards: ");
            L.PrintOut(commonCards,"Common Cards: ");            

            //string num1 = card1.Split('|' )[0];

            // ---- Evaluate Hands ----------
            HandClass H = new HandClass();
            
            List<List<int>> combos = H.getCombos();
            //L.PrintOutList(combos, true);
            
            List<List<string>> hands = H.allHands(holeCards, commonCards);

            var temp = H.evaluateHands2(holeCards,commonCards);
            
            List<int> _ns = new List<int>() {6, 8, 20};         
            foreach (int _n in _ns)
            {
                List<int> combosN = combos[_n];
                List<string> handsN = hands[_n];

                L.PrintOut(combosN, ("Combo #" + Convert.ToString(_n) + " ") );
                L.PrintOut(handsN, ("Hand #" + Convert.ToString(_n) + " ") );                
            }
            
            // ---- Misc and Testing ---------
            //Misc m = new Misc();
            //m.SelectManyEx2();
            //m.PrintListList(qqq);

            Console.WriteLine("done.");
        }

    }
    

}

