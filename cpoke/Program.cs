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

   public string outputData(List<string> inputData, bool int_item = false)
   {
        StringBuilder builder = new StringBuilder();
        
        /*object iterData = new object();

        if (inputData.GetType() == typeof(List<string>) ) {
            List<string> iterData = inputData as List<string>; 
        }

        if (inputData.GetType() == typeof(List<int>) ) {
            List<int> iterData = inputData as List<int>; 
        }*/
        
        foreach (var item in inputData)
        {
            string s_item;
            if (int_item) {s_item = Convert.ToString(item);}
            else {s_item = item;}

            builder.Append(s_item).Append(" - ");
        }
        string sData = builder.ToString();
            
       return sData;
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

   public List<List<int>> allHands(List<string> _common, List<string> _hole)
   {
       var ret = new List<List<int>>();
       int N = 7;

       for (int i = 0; i < N; i++) {
           var ij = new List<int>();
           ij.Add(i);
           for (int j = 0; j < N; j++) {
               if (j == i) continue;
               ij.Add(j);
           }
           ret.Add(ij);
       }
       return ret;
   }
   public void WriteToConsole(IEnumerable items)
    {
        /*  //this is not working right now
        if ( (items[0].GetType == typeof(string)) or 
              (items[0].GetType == typeof(int)) 

        foreach (object o in items)
        {
            if ( (o.GetType == typeof(string)) or o.GetType == typeof(int)) {

            } 
            Console.WriteLine(o);
        }
         */
    }

   //public List<string> Card(int num, Suit suit)
   public int Card(int num, int suit) 
   {
       //var splits = new List<Tuple<string, string>>();
       //cc = Suit.Clubs;
       string num_string = num.ToString();
       return 2;
    }

}
    public class Program
    {
        public static void Main(string[] args)
        {
            Helper h = new Helper();
            int iClubs = (int)Helper.Suit.Clubs;
            Console.WriteLine("the int of Clubs is:" + iClubs );        
            
            //int q = h.Card(1, 1);
            //Cards card = Cards();
            //int q = Helper.Card(1,Suit.Clubs)
            //string sq = Convert.ToString(q );
            //Cards cs = new Cards();
            //int jj = cs.unique_func();
            
            
            Console.WriteLine("Deal me in, dealer!");
            
            List<string> myDeck = h.Deck();

            int howManyCards = myDeck.Count;
            Console.WriteLine("There are this many cards in the deck: " + Convert.ToString(howManyCards));

            //string sDeck = h.outputData(myDeck);
            //Console.WriteLine("Your deck, sir: " + sDeck);

            /*
            int theCard = 17;

            string myCard = myDeck[theCard];
            Console.WriteLine("Your first hole card: " + myCard);

            myDeck.RemoveAt(theCard);
            string sDeck = h.outputData(myDeck);
            Console.WriteLine("The remaining deck: " + sDeck);
            */

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
            
            string myHoleCards = h.outputData(holeCards);
            string myCommonCards = h.outputData(commonCards);

            Console.WriteLine("Hole cards: " + myHoleCards );
            Console.WriteLine("Common cards: " + myCommonCards );

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

            List<List<int>> qqq = h.allHands(holeCards,commonCards);
            var www = h.allHands(holeCards,commonCards);
            
            var qqq1 = qqq[0];
            h.WriteToConsole(qqq);
            //var out2 = h.outputData(qqq1,true);
            //Console.WriteLine("qqq1: ", out2);
            


        }
    }

}

