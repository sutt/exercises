using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PokerApplication
{

    public class Logging
    {
        
        
        public void PrintOutList<T>(List<List<T>> inputData, bool printEnum = false )
        {   
            int cntr = 0;
            foreach (List<T> e in inputData)
            {
                string title = "";
                if (printEnum) title += (Convert.ToString(cntr) + ": ");  cntr += 1;         
                PrintOut(e, title);
            }
        }
         

        public void PrintOut<T>(List<T> inputData, string inpTitle = "")
        {
            
            StringBuilder builder = new StringBuilder();
            object iterData = new object();

            if (inputData.GetType() == typeof(List<string>) ) {
                iterData = inputData as List<string>; 
            }
            if (inputData.GetType() == typeof(List<int>) ) {
                iterData = inputData as List<int>; 
            }

            foreach (var item in inputData)
            {
                string s_item = Convert.ToString(item);
                builder.Append(s_item).Append(" - ");
            }
            
            string sData = builder.ToString();
                
            Console.WriteLine( inpTitle + sData );

        }
    }
}