using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 正负非反操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            Not();
        }

        /// <summary>
        /// 正负操作符。
        /// 
        /// 正负操作符在C#程序设计和数学中相同的部分不再表现，此处仅呈现二者之间不同的地方。
        /// </summary>
        static void PlusAndMinus()
        {
            Console.WriteLine($"int类型的最大值是{int.MaxValue}");     //输出：2147483647
            int x = int.MinValue;
            Console.WriteLine($"int类型的最小值是{x}");                //输出：-2147483648
            checked
            {
                try
                {
                    int y = unchecked(-x);
                    Console.WriteLine($"int类型最小值的相反数是{y}");  //输出：-2147483648，最小值的相反数与最小值相同，说明发生溢出。
                    y = -x;     //溢出会在此处被捕捉到。
                    /*
                     * 关于溢出的产生，在求反操作符中进行详解。
                     */
                }
                catch (OverflowException)
                {
                    Console.WriteLine("发生了溢出。");
                }
            }
        }

        /// <summary>
        /// 求反操作符
        /// 
        /// 求反操作符的功能是对一个值在二进制级别上进行按位取反。
        /// </summary>
        static void Negate()
        {
            int x = 12345678;
            int y = ~x;
            Console.WriteLine($"{x}的取反结果为{y}。");    //12345678的取反结果为-12345679。

            string xBin = Convert.ToString(x, 2).PadLeft(32, '0');  //x的二进制表示。
            string yBin = Convert.ToString(y, 2).PadLeft(32, '0');  //y的二进制表示。
            Console.WriteLine($@"
原数：{xBin}；
取反：{yBin}。");       //计算机求相反数的方式：按位取反，再加一。
        }

        /// <summary>
        /// 取非操作符。
        /// 
        /// 取非操作符的基本功能不再演示，仅以一实际案例作为演示，此方法仅对实例进行调用，实际的代码编写在下方Student类中。
        /// </summary>
        static void Not()
        {
            Student student1 = new Student("Tom");  //调用Student类的实例构造器，传入“Tom”，正常。
            Console.WriteLine(student1.Name);
            Student student2 = new Student(null);   //调用Student类的实例构造器，传入null，抛出ArgumentException。
            Console.WriteLine(student2.Name);
        }
    }

    /// <summary>
    /// Student类，作为取非操作符的实例演示。
    /// </summary>
    class Student
    {
        public string Name;

        public Student(string initName)
        {
            if (!(string.IsNullOrEmpty(initName)))  //如果参数initName的传入值不是空值，则执行逻辑。
            {
                this.Name = initName;
            }
            else
            {
                throw new ArgumentException("initName cannot be null or empty.");
                //抛出“传入参数无效”异常，并提示参数不可为空。
            }
        }
    }
}
