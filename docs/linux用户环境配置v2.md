## 环境准备



### 配置 Vim

1. 更新 apt 源信息

   ```bash
   sudo apt update
   ```

2. 配置 vim: [Vim配置教程2](https://zhuanlan.zhihu.com/p/631968686)



### zsh 的安装及配置

Zsh（Z Shell）是一种UNIX命令行shell，它是Bash的替代品，并在许多Linux和Unix系统中广泛使用。Zsh提供了一个更强大、更友好、更可定制的命令行环境.

简单来说, Zsh是更高效的命令行shell.



1. 安装 zsh

```bash
sudo apt install zsh
```

2. 修改默认 shell 为 zsh

```bash
chsh -s /bin/zsh
```

3. 安装 oh-my-zsh

[Official Installation Guide][https://github.com/ohmyzsh/ohmyzsh#getting-started]

4. 安装 zsh-syntax-highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

5. 使用命令`vim .zshrc`打开.zshrc 文件，找到`pluguns=()`这一行，将 zsh-syntax-highlighting 添加进去

```bash
plugins=(git zsh-syntax-highlighting)
```

6. 安装其他插件

```bash
mkdir ~/.oh-my-zsh/plugins/incr
wget http://mimosa-pudica.net/src/incr-0.2.zsh -O ~/.oh-my-zsh/plugins/incr/incr.plugin.zsh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sudo apt install autojump
```

7. 使用命令`vim .zshrc`，打开后在最后插入以下内容：

```bash
autoload -U colors && colors
PROMPT="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg[yellow]%}%1~ %{$reset_color%}%# "
RPROMPT="[%{$fg[yellow]%}%?%{$reset_color%}]"
# Useful support for interacting with Terminal.app or other terminal programs
[ -r "/etc/zshrc_$TERM_PROGRAM" ] && . "/etc/zshrc_$TERM_PROGRAM"
source ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
source /usr/share/autojump/autojump.sh
source ~/.oh-my-zsh/plugins/incr/incr*.zsh
```



### ctags 安装与配置

`ctags` 是一个用于生成源代码标签文件的工具，用于协助程序员在大型代码库中导航和查找代码。这些标签文件包含源代码文件中各种符号（如函数、变量、类名）的位置信息，使得程序员能够在源代码中迅速定位和跳转到这些符号的定义和引用处。

`ctags` 通常与文本编辑器（如Vim、Emacs）和集成开发环境（IDE）一起使用，以提供更好的代码导航和开发体验。当程序员在编辑器中输入代码时，`ctags`可以帮助他们查找相关符号、查看函数的定义、跳转到函数的实现、查找变量的引用等操作，从而提高代码的可维护性和开发效率。

[ctags项目地址][https://github.com/universal-ctags]



1. 使用以下命令安装**ctags**

```bash
sudo apt install ctags
```

2. 打开Vim，然后运行以下命令来启用 `ctags` 支持

```bash
:set tags=tags
```

3. 在项目目录中使用命令`ctags -R`生成标签文件
4. 在Vim中，使用 `Ctrl-]` 跳转到光标下符号的定义，使用 `Ctrl-T` 返回。



ctags默认支持C代码, 但也可以支持Python, 具体拓展可以自己搜索.



### [C语言可选] 安装 glibc-doc

`glibc-doc` 是GNU C库（GNU C Library）的文档集合，用于提供有关GNU C库的详细信息和文档。GNU C库包含了许多C语言函数和系统调用的实现，以及其他与系统编程相关的功能。而`glibc-doc` 提供了对GNU C库的详细说明.

1. 使用以下命令安装

```bash
sudo apt install glibc-doc
```
