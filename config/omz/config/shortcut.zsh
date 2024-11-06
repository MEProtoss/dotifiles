alias jo="joshuto"
alias vim="nvim"
alias n="nvim"
alias lag="lazygit"
alias zs="nvim ~/.config/omz/config/shortcut.zsh"
alias sour="source ~/.zshrc"
alias wm="nvim ~/workspace/dwm/config.h"
export PATH="/home/time/.local/share/gem/ruby/3.0.0/bin:$PATH"
alias 0.5="xrandr --output eDP-1 --brightness 0.5"
alias 0.8="xrandr --output eDP-1 --brightness 0.8"
alias 1="xrandr --output eDP-1 --brightness 1"
alias 0.3="xrandr --output eDP-1 --brightness 0.3"
alias ud144="xrandr --output eDP-1 --mode 2560x1600 --pos 0x1440 --rotate normal --output HDMI-1 --primary --mode 2560x1440 --rate 144 --pos 0x0 --rotate normal && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias ud75="xrandr --output eDP-1 --mode 2560x1600 --pos 0x1440 --rotate normal --output HDMI-1 --primary --mode 2560x1440 --rate 75 --pos 0x0 --rotate normal && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias Eng="nvim /home/time/workspace/wudao-dict/wudao-dict/usr/notebook.txt"
alias mus="musicfox"
alias zshshortcut="nvim ~/.config/omz/config/shortcut.zsh"

# exa --icons
# ls
alias ls='exa --icons'
alias l='exa --icons -lh'
alias ll='exa --icons -lah'
alias la='exa --icons -A'
alias lm='exa --icons -m'
alias lr='exa --icons -R'
alias lg='exa --icons -l --group-darectories-first'

alias ra='ranger'
alias fas='random_number=$((RANDOM % 739 + 1)); fastfetch --logo ~/Pictures/竖屏动漫/${random_number}.png --logo-type kitty --logo-width 25 --logo-height 18'
alias sig="xrandr --output eDP-1 --mode 2560x1600 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output DP-5 --off && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
# 快捷访问
alias c="cd ~/Code/"
alias p="cd ~/Pictures/"
alias d="cd ~/下载"
alias a="cd ~/Applications/"
alias nt="cd ~/文档/Notes/"
alias leetcode="nvim leetcode.nvim"
# python环境
alias gpt="source ~/workspace/shellgpt/chatgpt_cli/bin/activate"
alias acgpt="source ~/workspace/gpt_academic/myenv/bin/activate && python ~/workspace/gpt_academic/main.py" 

alias blog="cd ~/workspace/blog"
alias bm="cd ~/workspace/blog/source/_posts/"

# 常用软件
alias idea="idea.sh"
alias datagrip="datagrip.sh"
alias pycharm="pycharm.sh"
alias webstorm="webstorm.sh"

# blog快捷键
alias bgd="cd ~/workspace/blog && hexo g && hexo d"
# 快捷安装和删除
alias pinstall='sudo pacman -S'
alias upinstall='sudo pacman -Sy'
alias yinstall='yay -S'
# 美化输出
alias cat="bat"
# docker快捷键
# 查看运行中的容器
alias dps='sudo docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}"'
# 查看所有容器
alias dpsa='sudo docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}"'
# 查看容器详细信息
alias di='sudo docker inspect'
# 查看镜像
alias dim='sudo docker images'
# 使用trash-cli命令行回收站工具 
alias rm="trash-put"
alias trashcan="cd ~/.local/share/Trash"
# 处理解压windows压缩文件的标题乱码问题
# alias unzip="unzip -O CP936"
#
# On-demand rehash
zshcache_time="$(date +%s%N)"

autoload -Uz add-zsh-hook

rehash_precmd() {
  if [[ -a /var/cache/zsh/pacman ]]; then
    local paccache_time="$(date -r /var/cache/zsh/pacman +%s%N)"
    if (( zshcache_time < paccache_time )); then
      rehash
      zshcache_time="$paccache_time"
    fi
  fi
}
