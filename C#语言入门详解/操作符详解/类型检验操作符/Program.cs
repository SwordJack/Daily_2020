using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 类型检验操作符，主要指is和as操作符。
/// </summary>
namespace 类型检验操作符
{
    class Program
    {
        static void Main(string[] args)
        {
        }

        /// <summary>
        /// is操作符功能演示。
        /// </summary>
        static void IsOperatorIllustration()
        {
            Teacher t = new Teacher();
            //var result = t is Teacher;  //true。此处检验的并非变量，而是变量所引用的实例。倘使赋值t=null，则此处就会返回false。
            var result = t is Human;    //true。Teacher由Human类派生，且说老师是人类，也完全合理。不过反过来说Human是Teacher就不行了。
            Console.WriteLine(result);
        }

        /// <summary>
        /// as操作符功能演示。
        /// </summary>
        static void AsOperatorIllustration()
        {
            object o = new Teacher();
            Teacher t = o as Teacher;   //as操作符，如果o是Teacher类的实例，则返回实例地址；否则返回null。
            if (t != null)
            {
                t.Teach();
            }
        }
    }

    class Human
    {

    }

    class Teacher : Human
    {
        public void Teach()
        {
            Console.WriteLine("I teach programming.");
        }
    }

    class Car
    {

    }
}
