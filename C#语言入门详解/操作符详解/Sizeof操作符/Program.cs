using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// sizeof操作符用于获取一个对象在内存中所占用的字节数，在默认情况下只能用于获取基本数据类型（除string、object外）的实例所占用的字节数（结构体类型）。
/// 在非默认情况下，可以用于获取自定义的结构体类型实例的大小（即所占用字节数），但需要将其放在不安全的上下文中。
/// </summary>
namespace Sizeof操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            SizeofCustomType();
        }

        /// <summary>
        /// 对基本数据类型（结构体类型）使用sizeof操作符。
        /// </summary>
        static void SizeofBasicType()
        {
            int x = sizeof(decimal);
            Console.WriteLine(x);
        }

        /// <summary>
        /// 对自定义结构体数据类型使用sizeof操作符。
        /// 
        /// 执行如此操作需要：
        /// 1、使用unsafe关键字，将语句包含在不安全上下文内；
        /// 2、在“项目——生成”中勾选“允许不安全代码”；
        /// </summary>
        static void SizeofCustomType()
        {
            unsafe
            {
                int x = sizeof(Student);
                Console.WriteLine(x);
                /*
                 * x的值为16，而int类型和score类型的大小之和为12，这其中的差别涉及dotnet对内存管理的方式。
                 * 内存管理方式，已经超出了在C#入门课程中所需涉及之内容，故不进行展开。
                 */
            }
        }
    }

    /// <summary>
    /// 自定义结构体类型Student，用于演示sizeof操作符。
    /// </summary>
    struct Student
    {
        int ID;
        long Score;
    }
}
