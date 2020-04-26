using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 强制类型转换操作符，用于将一个高精度、占用较大内存空间的类型实例转换为一个低精度、占用较小内存空间的类型实例。
/// </summary>
namespace 强制类型转换操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            ConversionOperator();
        }

        /// <summary>
        /// 隐式类型转换的演示。
        /// 
        /// 此处主要演示子类向父类的隐式转换，基本类型的隐式转换不再呈现。
        /// </summary>
        static void ImplicitTypeConversion()
        {
            Teacher t = new Teacher();
            Human h = t;    //此语句包含了t的类型（Teacher）向其父类类型（Human）的隐式转换。

            t.Teach();  //实例t包含Teach方法。
            //h.Teach();  //实例h虽指向同实例t相同的地址，但是C#只允许访问到h的类型所包含的成员，故h不具有Teach方法。
        }

        /// <summary>
        /// 显式类型转换的演示。
        /// 
        /// 显式类型转换时有导致精度丢失的情况发生，这被称之为cast（v. 铸造，即表示将一个比较大的变量放入一个比较小的容器）。
        /// 因此，这种转换的进行需要开发者用(T)x操作符明确地告知编译器。
        /// 
        /// 这里不演示利用Convert类的方法进行类型转换的操作。
        /// </summary>
        static void ExplicitTypeConversion()
        {
            int x = 65536;          //int是一个32位的整数类型，最大值为2^32-1。
            Console.WriteLine(x);   //输出：65536
            ushort y;               //ushort是一个16位的整数类型，最大值位65535。
            //y = x;                //缺少强制类型转换，编译不通过。
            y = (ushort)x;          //强制将y赋以x转换为ushort的值。在这个过程中，int类型的低16位可以被放入ushort中，高16位则被舍弃。
            Console.WriteLine(y);   //0。
        }

        /// <summary>
        /// 字符串和数值类型之间转换的演示。
        /// </summary>
        static void StringAndNumerical()
        {
            string input = Console.ReadLine();

            //double x = double.Parse(input);     //数值类型的Parse方法，可以使得符合数值形式要求的字符串被解析为数值，但是Parse方法遇到不符合要求的字符串会发生FormatException异常。

            double x;
            bool isParsed = double.TryParse(input, out x);  //数值类型的TryParse方法，返回一个指示是否成功解析字符串的布尔值，同时提高输出参数来获得解析字符串的结果。

            double y = x + 5;

            Console.WriteLine(y.ToString());    //ToString方法，将实例转换为一个字符串，是object类型的实例方法，这也就使得每一个类型的实例都具有这个方法（一些类型会对这个方法进行重写）。
        }

        /// <summary>
        /// 应用自定义的强制类型转换操作符演示强制类型转换，这里使用Stone和Monkey两个类（见诸Stone.cs）进行演示。
        /// </summary>
        static void ConversionOperator()
        {
            Stone stone = new Stone();
            stone.Age = 5000;
            Monkey monkey = (Monkey)stone;
            Console.WriteLine($"猴子的年龄是{monkey.Age}");
        }
    }
}
