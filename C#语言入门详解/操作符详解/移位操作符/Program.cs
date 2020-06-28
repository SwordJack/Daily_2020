using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 移位操作符，将数据在内存中的二进制结构向左或向右进行一定位数的平移。
/// </summary>
namespace 移位操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            RightShift();
        }

        /// <summary>
        /// 左移，即将数据在内存中的二进制结构向左移动，并在右侧补0，此处以左移一位为例。
        /// 
        /// 由于二进制的特性，左移一位，相当于将数值乘以2；若左移超出此数据类型的最高位，则触发溢出。
        /// </summary>
        static void LeftShift()
        {
            int x = 7;
            var y = x << 1;
            string strX = Convert.ToString(x, 2).PadLeft(32, '0');
            string strY = Convert.ToString(y, 2).PadLeft(32, '0');
            Console.WriteLine(strX);
            Console.WriteLine(strY);
            Console.WriteLine(y);
        }

        /// <summary>
        /// 右移，即将数据在内存中的二进制结构向右移动，此处以右移一位为例。
        /// 
        /// 右移存在最高位补位的问题，此处的惯例是，正数最高位补0，负数最高位补1。
        /// 由于二进制的特性，右移一位，相当于将数值除以2（向下圆整）；若左移超出此数据类型的最高位，则在checked上下文中会触发溢出。
        /// </summary>
        static void RightShift()
        {
            int x = -13;
            var y = x >> 1;
            string strX = Convert.ToString(x, 2).PadLeft(32, '0');
            string strY = Convert.ToString(y, 2).PadLeft(32, '0');
            Console.WriteLine(strX);
            Console.WriteLine(strY);
            Console.WriteLine(y);
        }
    }
}
