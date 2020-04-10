using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// checked/unchecked是用于检查/不检查变量的值溢出的操作符，也可作为上下文关键字使用。
/// </summary>
namespace Checked操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            CheckedContext();
        }

        /// <summary>
        /// checked操作符用于检查变量的值有没有产生溢出；而unchecked操作符则用于告诉编译器不用检查值的溢出。
        /// 
        /// （此静态方法仅作为代码的容器使用，不具有实际功能）
        /// </summary>
        static void CheckedOperator()
        {
            uint x = uint.MaxValue;
            Console.WriteLine(x);                       //2^32 - 1 = 4294967295
            //Console.WriteLine(Convert.ToString(x, 2));  //转化为二进制形式（32个1）。

            //Console.WriteLine(x + 1);                   //由于发生了溢出，导致最终输出0。
            Console.WriteLine(checked(x + 1));      //添加了checked操作符，程序会在此处抛出System.OverflowException异常，可用try……catch捕捉。
            Console.WriteLine(unchecked(x + 1));    //使用unchecked操作符，程序即不再检查此处的溢出，可见C#是默认使用unchecked的。
        }

        /// <summary>
        /// checked作为上下文关键字，其下的语句块中所有的溢出都会被检查到并抛出。
        /// 如使用unchecked作为上下文关键字，则语句块中的所有溢出都不会被检查和抛出。
        /// 
        /// （此静态方法仅作为代码的容器使用，不具有实际功能）
        /// </summary>
        static void CheckedContext()
        {
            checked
            {
                try
                {
                    uint x = uint.MaxValue;
                    Console.WriteLine(x + 1);
                }
                catch(OverflowException ex)
                {
                    Console.WriteLine($"发生了溢出，{ex}");
                }
            }
        }
    }
}
