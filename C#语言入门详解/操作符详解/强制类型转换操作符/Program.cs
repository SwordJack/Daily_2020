using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 强制类型转换操作符
{
    class Program
    {
        static void Main(string[] args)
        {

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
    }
}
