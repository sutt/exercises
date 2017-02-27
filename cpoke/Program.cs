using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;
 
namespace PokerApplication
{

    public class Helper
{
   
   public List<List<int>> allCombos()
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
                                      List<string> _common, 
                                      List<List<int>> _combos)
   {

        List<List<string>> ret = new List<List<string>>();

        List<string> c = new List<string>();
        c.AddRange(_hole);
        c.AddRange(_common);
        
        foreach (List<int> combo in _combos)
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



}

//end helper
            
    public class Program
    {
        public static void Main(string[] args)
        {
            
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
            Helper h = new Helper();
            List<List<int>> combos = h.allCombos();
            List<List<string>> hands = h.allHands(holeCards, commonCards, combos);

            Console.WriteLine("All Combos: ");
            //L.PrintOutList(combos, true);

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

