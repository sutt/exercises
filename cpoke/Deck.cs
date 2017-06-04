using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PokerApplication
{

    public class DeckClass
    {

        private Random _rnd = new Random();

        public List<string> myDeck = CreateDeck();

        public List<string> getDeck()  {return myDeck;}

        public static List<string> CreateDeck()
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


        public int randomSample(List<string> deck, Random rand)
        {
            int cardInd = rand.Next(deck.Count - 1);
            return cardInd;
        }

        public List<string> removeCard(List<string> _deck, int ind)
        {
            _deck.RemoveAt(ind);
            return _deck; 
        }


        public List<string> dealNCards(int N)
        {
            List<string> data = new List<string>();
            for (int i = 1; i <= N; i++)
            {
                int randInt = randomSample(myDeck, _rnd);
                string thisCard = myDeck[randInt];
                data.Add(thisCard);
                myDeck = removeCard(myDeck, randInt);
            }
            return data;
        }

        public List<List<string>> dealHoleCards(int players, int N = 2)
        {
            List<List<string>> ret = new List<List<string>>();
            for (int i = 0;i < players; i++) {
                ret.Add( dealNCards(N) )
            }
            return ret ;
        }

        public List<string> dealCommonCards(int N)
        {
            return dealNCards(N);
        }

    }
}