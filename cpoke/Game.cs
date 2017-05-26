using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Collections;


namespace PokerApplication
{
            
public class Game
{

    public static bool hello = true;

    public static bool RunGame()
    {
        DeckClass deck = new DeckClass();
        //deck.dealHoleCards();
        
        return hello;
    }

    public int[] evalWinner(List<List<string>> playerHoleCards, List<string> commonCards)
    {

        HandClass hc = new HandClass();

        int playerLen = playerHoleCards.Count;

        int[] ret = new int[] {};

        Tuple<int,int,List<int>>[] eval_ret2 = new Tuple<int,int,List<int>>[] {};
        int[] evalHand = new int[] {};
        int[] evalRank = new int[] {};
        List<int>[] evalKickers = new List<int>[] {};
        
        foreach (List<string> _holeCards in playerHoleCards) 
        {
            eval_ret2.Append( hc.evaluateHands( _holeCards, commonCards) );
            evalHand.Append( hc.evaluateHands( _holeCards, commonCards).Item1);
            evalRank.Append( hc.evaluateHands( _holeCards, commonCards).Item2);
            evalKickers.Append( hc.evaluateHands( _holeCards, commonCards).Item3);
        }

        for (int j=0; j< playerLen; j++)
        {
            //eval_ret2[j];
        }

        return ret;
    }

}
}
 