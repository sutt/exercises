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


        public List<string> dealNCards(int N)
        {
            List<string> data = new List<string>();
            for (int i = 1; i <= N; i++)
            {
                int randInt = dealCard3(myDeck, _rnd);
                string thisCard = myDeck[randInt];
                data.Add(thisCard);

                myDeck = removeCard(myDeck, randInt);
            }
            return data;
        }

        public List<string> dealHoleCards(int players)
        {
            return dealNCards(2);
        }

        public List<string> dealCommonCards()
        {
            return dealNCards(5);
        }

    }
}