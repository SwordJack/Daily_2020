using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

/// <summary>
/// delegate作为一个关键字，其最主要的用途是用于声明委托，而非作为关键字使用。
/// 此处仅呈现其作为操作符使用的方式，但此方式的使用较为少见，如今一般使用lambda表达式代替之。
/// </summary>
namespace Delegate操作符
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            //this.myButton.Click += MyButton_Click;  //输入到“+=”之后，双击Tab键，VS即会自动生成事件处理器。

            this.myButton.Click += delegate (object sender, RoutedEventArgs e)  //不考虑方法重用时，可直接使用delegate关键字挂接匿名方法作为事件处理器。
            {
                //throw new NotImplementedException();
                this.myTextBox.Text = "Hello World! ";
            };

            this.myButton.Click += (sender, e) =>   //delegate关键字声明的匿名方法已经是一种过时方法，如今进一步演化为lambda表达式，不再需要声明参数类型，而是由C#编译器自行推断。
            {
                this.myTextBox.Text += "Hello Lambda!";
            };
        }

        private void MyButton_Click(object sender, RoutedEventArgs e)
        {
            //throw new NotImplementedException();
            this.myTextBox.Text = "Hello World!";
        }
    }
}
