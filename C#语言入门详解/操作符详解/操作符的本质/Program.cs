using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// 操作符是函数、算法、运算的简记法，操作符依赖于数据类型（比如整数的“/”与浮点数的“/”是不同的除号）。
/// 但是从感性认识的角度而言，操作符的本质对我们依旧相对模糊。
/// C#中常用的操作符都是C#语言为我们准备好，即Microsoft的程序员为我们预先编写的。
/// 故而，本例中，将通过创建一个类型，并为此类型创建一个操作符，以使得我们能够清晰理解操作符的本质。
/// </summary>
namespace 操作符的本质
{
    class Program
    {
        static void Main(string[] args)
        {
            Person person1 = new Person();  //声明第一个人，命名为Deer。
            person1.Name = "Deer";

            Person person2 = new Person();  //声明第二个人，命名为May。
            person2.Name = "May";

            //List<Person> nation = Person.GetMarry(person1, person2);    //声明一个Person类列表nation（民族），让两人结婚。

            List<Person> nation = person1 + person2;    //通过“+”操作符，实现了与调用GetMarry方法一样的效果。

            foreach (var person in nation)  //输出“民族”中每个人的名字。
            {
                Console.WriteLine(person.Name);
            }

        }
    }
}
