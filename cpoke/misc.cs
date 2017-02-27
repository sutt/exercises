using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PokerApplication
{

public class Misc
{
    class PetOwner
    {
        public string Name { get; set; }
        public List<String> Pets { get; set; }
    }


    public string outputData(List<int> inputData, bool int_item = false)
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
                string s_item = Convert.ToString(item);
                builder.Append(s_item).Append(" - ");
            }
            string sData = builder.ToString();
                
        return sData;
    }

        public int PrintListList(List<List<int>> input, bool new_way = true) {
                foreach (var sublist in input)
                {
                
                if (new_way) 
                {
                    string thisHand = outputData(sublist);
                    Console.WriteLine(thisHand);
                }
                else
                {
                    foreach (var obj in sublist) {
                        Console.WriteLine(Convert.ToString(obj));
                    }
                }
                }
            return 1;
        }

        public int SelectManyEx2()
        {
            PetOwner[] petOwners = 
                { new PetOwner { Name="Higa, Sidney", 
                    Pets = new List<string>{ "Scruffy", "Sam" } },
                new PetOwner { Name="Ashkenazi, Ronen", 
                    Pets = new List<string>{ "Walker", "Sugar" } },
                new PetOwner { Name="Price, Vernette", 
                    Pets = new List<string>{ "Scratches", "Diesel" } } };

            // Query using SelectMany().
            IEnumerable<string> query1 = petOwners.SelectMany(petOwner => petOwner.Pets);

            Console.WriteLine("Using SelectMany():");

            // Only one foreach loop is required to iterate 
            // through the results since it is a
            // one-dimensional collection.
            foreach (string pet in query1)
            {
                Console.WriteLine(pet);
            }

            // This code shows how to use Select() 
            // instead of SelectMany().
            IEnumerable<List<String>> query2 =
                petOwners.Select(petOwner => petOwner.Pets);

            Console.WriteLine("\nUsing Select():");

            // Notice that two foreach loops are required to 
            // iterate through the results
            // because the query returns a collection of arrays.
            foreach (List<String> petList in query2)
            {
                foreach (string pet in petList)
                {
                    Console.WriteLine(pet);
                }
                Console.WriteLine();
            }
            return 1;
        }
        //int ret = SelectManyEx2();
        //this.SelectManyEx1();

        // DEMO ----------------------------------------------------

}
}