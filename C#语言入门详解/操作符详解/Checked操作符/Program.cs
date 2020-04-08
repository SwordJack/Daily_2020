using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// checked操作符用于检查变量的值有没有产生溢出；而unchecked操作符则用于告诉编译器不用检查值的溢出。
/// </summary>
namespace Checked操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            uint x = uint.MaxValue;
            Console.WriteLine(x);                       //2^32 - 1 = 4294967295
            Console.WriteLine(Convert.ToString(x, 2));  //转化为二进制形式（32个1）。
            Console.WriteLine(x + 1);                   //由于发生了溢出，导致最终输出0。
        }
    }
}
