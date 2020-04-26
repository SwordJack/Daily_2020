using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 强制类型转换操作符
{
    /// <summary>
    /// “石头”类
    /// </summary>
    class Stone
    {
        /// <summary>
        /// 年龄
        /// </summary>
        public int Age;

        /// <summary>
        /// 石头历经了几千年，具有了灵性，蹦出来一只石猴。
        /// 那么在这个逻辑下，石头向猴子进行类型转换，也就顺理成章了。
        /// 
        /// 注1：显式类型转换操作符的样式和实例构造器有点相似，而在某种意义上，它也确实起到一个实例构造器的作用。
        /// 注2：隐式类型转换操作符的定义和显式类型转换操作符的定义是很相似的，只需要将修饰符中的explicit更改为implicit即可，于是在调用隐式类型转换操作符的时候，就不需要加上(Monkey)了。
        /// </summary>
        /// <param name="stone">Stone类的实例</param>
        public static explicit operator Monkey(Stone stone)
        {
            Monkey monkey = new Monkey();
            monkey.Age = stone.Age / 500;
            return monkey;
        }
    }

    class Monkey
    {
        /// <summary>
        /// 年龄
        /// </summary>
        public int Age;
    }
}
