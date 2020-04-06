using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 操作符的本质
{
    /// <summary>
    /// 因“给我一个支点，我就能撬动地球”（阿基米德）这句话，而引申出“给我一个姑娘，我就能创造一个名字”的笑谈。
    /// 借此笑谈，创建一个Person类，并编写“创造一个民族”的方法。
    /// </summary>
    class Person
    {
        public string Name;     //人的名字


        /// <summary>
        /// 两个人结婚，然后就可以创造民族了。
        /// </summary>
        /// <param name="p1">婚姻中的一方</param>
        /// <param name="p2">婚姻中的另一方</param>
        /// <returns></returns>
        public static List<Person> GetMarry(Person p1, Person p2)
        {
            List<Person> people = new List<Person>();   //新建一个Person类的列表people。

            people.Add(p1);     //先把婚姻双方加进去。
            people.Add(p2);
            for (int i = 0; i < 11; i++)    //不妨生一个足球队（一个足球队11个人上场）。
            {
                Person child = new Person();
                child.Name = p1.Name + " & " + p2.Name + "'s child";     //孩子的名字姑且就叫“p1和p2的孩子”。
                people.Add(child);  //将孩子加入people列表。
            }
            return people;
        }

        /// <summary>
        /// 此处创建操作符“+”，替代静态函数GetMarry，实现两人结婚然后创造民族。
        /// 此处为偷懒，通过调用GetMarry方法实现操作符的执行。在操作符的花括号内编写函数体亦是可以的。
        /// </summary>
        /// <param name="p1">婚姻中的一方</param>
        /// <param name="p2">婚姻中的另一方</param>
        /// <returns></returns>
        public static List<Person> operator +(Person p1, Person p2)
        {
            return GetMarry(p1, p2);
        }
    }
}
