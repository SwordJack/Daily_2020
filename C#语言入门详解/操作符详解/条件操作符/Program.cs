using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 条件操作符指“与”（&&）和“或”（||）操作符。
/// 
/// 这里不演示操作符的基本功能，仅对其“短路”效应进行演示。
/// </summary>
namespace 条件操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            ShortCircuit();
        }

        /// <summary>
        /// 演示条件“与”和“或”操作符的“短路”效应。
        /// </summary>
        static void ShortCircuit()
        {
            int x = 3;
            int y = 4;
            int a = 3;
            if (x > y && a++ > 3)
            {
                Console.WriteLine("Hello 'And' Circuit 01.");
            }
            Console.WriteLine(a);   //x > y为false，即发生短路效应，不输出语句，不再执行a++，故输出3。
            
            a = 3;
            if (x < y && a++ > 3)
            {
                Console.WriteLine("Hello 'And' Circuit 02.");
            }
            Console.WriteLine(a);   //x < y为true，但a++是后置自增，a>3不满足，故不输出语句，但执行a++，故输出4。
            
            a = 3;
            if (x < y || a++ > 3)
            {
                Console.WriteLine("Hello 'Or' Circuit 01.");
            }
            Console.WriteLine(a);   //x < y为true，即发生短路效应，输出语句，但不执行a++，故输出3。

            a = 3;
            if (x > y || a++ > 3)
            {
                Console.WriteLine("Hello 'Or' Circuit 02.");
            }
            Console.WriteLine(a);   //x > y为false，但a++是后置自增，a>3不满足，故不输出语句，但执行a++，故输出4。
        
            /*
             * 如果上面的a++变成++a，则情形会有所不同，不再赘述。
             * 
             * 自增自减符号，是“bug制造机”，名不虚传。
             */
        }
    }
}
