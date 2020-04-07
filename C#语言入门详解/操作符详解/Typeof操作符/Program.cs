using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// typeof操作符可以帮助我们去查看类型的内部结构，亦即Metadata；
/// Metadata：元数据，包含这个数据类型的名字、所属名字空间、父类、属性、事件等基本信息。
/// </summary>
namespace Typeof操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            Type t = typeof(int);           //声明一个“类”类型，使用typeof操作符为其赋值。

            Console.WriteLine(t.Namespace); //类型所属的名字空间。
            Console.WriteLine(t.FullName);  //类型的全名。
            Console.WriteLine(t.Name);      //类型的名称。

            System.Reflection.MethodInfo[] methods = t.GetMethods();   //GetMethods方法返回一个MethodInfo数组

            Console.WriteLine("{0}类型包含{1}个公共方法：", t.Name, methods.Length);  //Length属性获取其长度，即得此类型的公共方法数目。
            foreach (var method in methods)
            {
                Console.WriteLine(method.Name);  //打印其每个公共方法的名称。
            }
        }
    }
}
