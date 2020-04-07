using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// new操作符的主要功能是在内存中创建一个类型的实例，并立刻调用这个类的实例构造器（构造函数）。
/// </summary>
namespace New操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            ExampleClass example = new ExampleClass()
            /*
             * 此处，new操作符执行的操作是：
             * 1、创建了ExampleClass类的新实例；
             * 2、调用了ExampleClass类的实例构造器；
             * 3、返回实例的内存地址，并将此地址通过赋值符号赋值给访问此实例的变量example。
             */
            {
                Statement = "I am another example.",
                Description = "Just say something."
                /*
                 * 这是new操作符的附加功能，可以调用实例的初始化器，即在构造器后加上花括号，为实例的公有字段和属性设置值。
                 * 初始化器中可对构造函数中所赋的值进行覆盖，但不可改变只读字段或属性的值。
                 * 初始化器后亦可以接成员访问操作符“.”（名字空间.类.方法()）调用其方法或访问其字段，这在一些仅调用一次的实例（如一些窗体实例）的使用中有应用。
                 */
            };

            Console.WriteLine(example.Statement);
        }

        /// <summary>
        /// 基本类型的语法糖。
        /// （此静态方法仅作为代码的容器使用，不具有实际功能）
        /// 
        /// 语法糖体现了C#语言在某些场合的灵活性，即在创建某些类型的实例时，可以选择使用或不使用new操作符。
        /// </summary>
        static void SyntacticSugarForBasicTypes()
        {
            string name = "Tom";
            /*
             * string类型作为一个类类型（相对于是结构体类型的int、char等），按理在声明的时候需要调用new操作符，但是在实际编写时，从来不用去调用new操作符。
             * 这是因为，string类型是一个非常基本的类型，Microsoft在创建C#语言时，为了统一基本类型的使用体验，有意隐藏了new操作符，令我们可以像使用int类型一样去使用string类型。
             * 当然，使用创建类的方式来声明string类型也是可以的，如：
             * string varName = new string(params);
             */

            int[] arr1 = new int[3];    //整型数组（int[]）的构造器比较特殊，其后不需要添加圆括号“()”
            int[] arr2 = { 1, 2, 3, };  //这里可以不使用new操作符，而是直接写上了整形数组的元素，编译器亦可以编译通过。这同样是一个语法糖。
        }


    }

    /// <summary>
    /// 一个ExampleClass类，作为new操作符操作引用类型的示例。
    /// </summary>
    class ExampleClass
    {
        public string Statement;
        public string Description;

        public ExampleClass()
        {
            Statement = "I am an example.";
        }
    }
}
