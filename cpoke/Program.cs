using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;
 
namespace PokerApplication
{

    public class Helper
{
   public enum Suit
   {
        Spades,
        Hearts,
        Clubs,
        Diamonds
   };

   public List<string> Deck()
   {
       List<string> data = new List<string>();
       for (int cardnum = 0; cardnum <= 12; cardnum++)
       {
           for (int suit = 0 ; suit <= 3; suit++ )
           {
            string card = Convert.ToString(cardnum) + "|" + Convert.ToString(suit);
            data.Add(card);
           }
       }
       return data;
   }


   public int dealCard2(Random inpRand)
   {
       int ret = inpRand.Next(10);
       return ret;
   }

   public int dealCard3(List<string> deck, Random rand)
   {
       int cards = deck.Count;
       int card = rand.Next(cards - 1);
       return card;
   }

   public List<string> removeCard(List<string> _deck, int ind)
   {
       _deck.RemoveAt(ind);
       return _deck; 
   }

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


   public int Card(int num, int suit) 
   {
       //var splits = new List<Tuple<string, string>>();
       //cc = Suit.Clubs;
       string num_string = num.ToString();
       return 2;
    }

}

//end helper
            
    public class Program
    {
        public static void Main(string[] args)
        {
            Helper h = new Helper();
            int iClubs = (int)Helper.Suit.Clubs;
            Console.WriteLine("the int of Clubs is:" + iClubs );        
            
            Logging L = new Logging();
            
            Console.WriteLine("Deal me in, dealer!");
            
            List<string> myDeck = h.Deck();

            int howManyCards = myDeck.Count;
            Console.WriteLine("There are this many cards in the deck: " + Convert.ToString(howManyCards));
            L.PrintOut(myDeck , "Your deck, sir: ");


            Random _rnd = new Random();
            
            List<string> holeCards = new List<string>();
            for (int i = 1; i <= 2; i++)
            {
                int randInt = h.dealCard3(myDeck, _rnd);
                string thisCard = myDeck[randInt];
                holeCards.Add(thisCard);

                myDeck = h.removeCard(myDeck, randInt);
                
            }

            List<string> commonCards = new List<string>();
            for (int i = 1; i <= 5; i++)
            {
                int randInt = h.dealCard3(myDeck, _rnd);
                string thisCard = myDeck[randInt];
                commonCards.Add(thisCard);

                myDeck = h.removeCard(myDeck, randInt);
                
            }
            
            //string myHoleCards = h.outputData(holeCards);
            //string myCommonCards = h.outputData(commonCards);

            //Console.WriteLine("Hole cards: " + myHoleCards );
            //Console.WriteLine("Common cards: " + myCommonCards );

            string card1 = holeCards[0];
            string card2 = holeCards[1];

            string num1 = card1.Split('|' )[0];
            string num2 = card2.Split('|' )[0];

            Console.WriteLine("Hole1 num:" + num1);
            Console.WriteLine("Hole2 num:" + num2);

            bool HolePair = (num1 == num2);

            if (HolePair)
            { Console.WriteLine("Pair!" + HolePair.ToString()); }
            else 
            {Console.WriteLine("Nah " + HolePair.ToString());}

            // ---- Evaluate Hands ----------
            List<List<int>> combos = h.allCombos();
            
            List<List<string>> hands = h.allHands(holeCards, commonCards, combos);

            Console.WriteLine("All Combos: ");
            //List<string> dList = new List<string>();
            L.PrintOutList(combos, true);

            /*
            foreach (List<int> c in combos)
            {
                L.PrintOut(c, "");
            } */

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

