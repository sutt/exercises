using System;
using System.Collections.Generic;
using System.Text;
using System.Collections;
using System.Linq;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            
            //needs: using System.Collections.Generic;
            List<string> myList = new List<string>();
            myList.Add("Bri");
            myList.Add("Anna");
                        
            string trythis = myList.ToString();
            Console.WriteLine("with two:" + trythis);

            //List<string> myList2 = new {"a","b"};
            //needs: using System.Text
            StringBuilder builder = new StringBuilder();
            
            myList.Add("Jack");
            foreach (string item in myList)
            {
                builder.Append(item).Append("|");
            }
            string result = builder.ToString();
            Console.WriteLine("sList:" + result);
            
            string[] mymy = {"q|w", "a|b"};

            int len_mymy = mymy.GetLength(0);
            Console.WriteLine(" len: " + Convert.ToString(len_mymy) );

            List<string> q = new List<string>();
            q.Add("1");
            var w = new List<string>();
            w.Add("2");
            w.Add("3");
            q.AddRange(w);

            StringBuilder builder2 = new StringBuilder();
            foreach (string item in q)
            {
                builder2.Append(item).Append("|");
            }
            string result2 = builder2.ToString();
            Console.WriteLine("q: " + result2);

            List<List<string>> qq = new List<List<string>>();
            
            var list = new List<int>(Enumerable.Range(0, 50));
            list.ForEach(Console.WriteLine);
            //private Dictionary<string, int> candidates = new Dictionary<string, int>();
            //System.

        }
    }
}
