using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 强制类型转换操作符
{
    class Animal
    {
        public void Eat()
        {
            Console.WriteLine("Eating ……");
        }
    }

    class Human : Animal
    {
        public void Think()
        {
            Console.WriteLine("Who I am?");
        }
    }

    class Teacher : Human
    {
        public void Teach()
        {
            Console.WriteLine("I teach programming.");
        }
    }
}
