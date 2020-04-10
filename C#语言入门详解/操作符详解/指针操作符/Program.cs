using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 类似C和C++，C#一样有指针的存在。但是由于指针操作是直接操作内存，故必须放在不安全的上下文中进行使用，并在“项目——生成”中勾选“允许不安全代码”。
/// “->”是指针操作符，使用格式为“指针变量->所指向之结构体实例的字段”。
/// 
/// “->”操作符，包括与之相关的“&”、“*”操作符，是在C#开发中使用较少的操作符。
/// </summary>
namespace 指针操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            PointerOperation();
        }

        /// <summary>
        /// 指针操作。
        /// </summary>
        static void PointerOperation()
        {
            Student student;    //声明Student结构体的实例并初始化。
            student.ID = 1;
            student.Score = 99;
            Console.WriteLine($"student-{student.ID}: {student.Score}");        //输出student-1: 99。
            unsafe
            {
                Student* pStu = &student;           //&操作符，获取实例student的内存地址。
                pStu->Score = 100;                  //通过指针对字段的值进行修改。
                (*pStu).ID = 2;                     //*操作符，引用指针pStu指向的实例，但由于“.”的运算优先级较高，故应当加上括号。
                Console.WriteLine($"student-{student.ID}: {student.Score}");    //输出student-2: 100。
            }
        }
    }

    /// <summary>
    /// 声明一个结构体，作为“->”操作符的演示。
    /// 
    /// C#有着严格的规定，即指针操作、取地址操作、用指针访问成员的操作只可以用于操作结构体类型，而不可用于引用类型（例如：类类型）。
    /// </summary>
    struct Student
    {
        public int ID;
        public long Score;
    }
}
