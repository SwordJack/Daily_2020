using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// default操作符的功能是帮助我们获取一个类型的默认值。
/// 在此着重体现default操作符对结构体类型、引用类型和枚举类型的操作。
/// 其中结构体类型和枚举类型是值类型，而引用类型是和值类型相对的另一种类型。
/// </summary>
namespace Default操作符
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = default(int);   //当default操作符操作的类型是结构体类型（如int、double等）时，会返回内存块中为0的值。
            Console.WriteLine(x);

            ExampleClass example = default(ExampleClass);   //当default操作符操作的类型是引用类型时，会返回内存块中为0的值，表现为null。
            Console.WriteLine(example == null);

            //注：default(string)也返回null值。

            Level level = default(Level);   //当default操作符操作的类型是枚举类型时，会返回此枚举类型下索引为0的值，默认为第一个值。
            Console.WriteLine(level);

            IndexedLevel indexedLevel = default(IndexedLevel);  //当default操作符操作的类型是枚举类型时，会返回此枚举类型下索引为0的值。
            Console.WriteLine(indexedLevel);
        }
    }

    /// <summary>
    /// 一个ExampleClass类，作为default操作符操作引用类型的示例。
    /// </summary>
    class ExampleClass
    {
        public string Statement;

        public ExampleClass()
        {
            Statement = "I am an example.";
        }
    }

    /// <summary>
    /// 一个枚举类型，作为default操作符操作枚举类型的示例。
    /// </summary>
    enum Level
    {
        Low,
        Mid,
        High
    }

    /// <summary>
    /// 一个赋给了索引值的枚举类型，作为default操作符操作枚举类型的示例。
    /// 应当注意，当类型中不存在赋给了0值的项时，会使得default操作符返回0，引发可能的逻辑错误。
    /// </summary>
    enum IndexedLevel
    {
        Low = 2,
        Mid = 1,
        High = 0,
    }
}
