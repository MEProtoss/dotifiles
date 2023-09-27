# dotifiles
如何管理自己的dotfiles？

* 首先找个地方创建一个文件
```bash
mkdir dotfiles //创建一个dotfiles的文件夹放在你喜欢的地方
cd dotfiles
pwd //看看文件夹位置
/Users/luolei/Dropbox/dotfiles  //我放在dropbox里
git init //创建git
```

* 下面来把系统里的那些dotfiles软连接到这个文件夹
```bash
cd ~/ 去到根目录
mv .vimrc ~/Users/luolei/Dropbox/dotfiles/vimrc
mv .zshrc  ~/Users/luolei/Dropbox/dotfiles/zshrc
ln -s ~/Users/luolei/Dropbox/dotfiles/vimrc .vimrc
ln -s ~/Users/luolei/Dropbox/dotfiles/zshrc .zshrc
```
以上举例软链接了.vimrc , .zshrc到dotfiles，其他的文件类似。

* 软链接做好了后，接下来，你可把这些推到github上（首先要在github上创建一个repo），记得添加一个.gitignore。
```bash
cd ~/Users/luolei/Dropbox/dotfiles/
git add .
git commit -m '创建dotfils'
git remote add origin git@github.com:username/dotfiles.git
git push -u origin master
```

* 好啦，备份完了，现在，由于你努力学习工作，终于神舟换IBM，mini换rmbp，要恢复下dotfiles。
```bash
git clone git@github.com:username/dotfiles.git dotfiles
rm -rf .vimrc .zshrc //首先删除自身机器上原有的dotfiles
ln -s dotfiles/vimrc .vimrc
ln -s dotfiles/zshrc .zshrc
```
