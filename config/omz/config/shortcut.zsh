alias jo="joshuto"
alias vim="nvim"
alias n="nvim"
alias lag="lazygit"
alias zshshortcut="nvim ~/.config/omz/config/shortcut.zsh"
alias sourcezsh="source ~/.zshrc"
alias nvimkeymap="nvim ~/.config/nvim/lua/keymap.lua"
alias wm="nvim ~/workspace/dwm/config.h"
export PATH="/home/time/.local/share/gem/ruby/3.0.0/bin:$PATH"
alias tz="trans :zh"
alias 0.5="xrandr --output eDP-1 --brightness 0.5"
alias 0.8="xrandr --output eDP-1 --brightness 0.8"
alias 1="xrandr --output eDP-1 --brightness 1"
alias 0.3="xrandr --output eDP-1 --brightness 0.3"

alias sig="xrandr --output eDP-1 --mode 2560x1600 --pos 0x1440 --rotate normal --output HDMI-1 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output DP-5 --off"
alias ud144="xrandr --output HDMI-1 --mode 2560x1440 --rate 144 && xrandr --output HDMI-1 --above eDP-1 --primary && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias lr144="xrandr --output HDMI-1 --mode 2560x1440 --rate 144 && xrandr --output HDMI-1 --right-of eDP-1 --primary && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias ud75="xrandr --output HDMI-1 --mode 2560x1440 --rate 75 && xrandr --output HDMI-1 --above eDP-1 --primary && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias lr75="xrandr --output HDMI-1 --mode 2560x1440 --rate 75 && xrandr --output HDMI-1 --right-of eDP-1 --primary && feh --randomize --bg-fill ~/Pictures/wallpaper/*.png"
alias Eng="nvim /home/time/softwares/wudao-dict/wudao-dict/usr/notebook.txt"
alias vrc="nvim ~/.config/nvim/init.lua"
alias mus="musicfox"
alias ls="exa"
alias ra='ranger'
alias fas='random_number=$((RANDOM % 739 + 1)); fastfetch --logo ~/Pictures/anime/${random_number}.png --logo-type kitty --logo-width 30 --logo-height 17'

# 使用trash-cli命令行回收站工具 

alias rm="trash-put"
alias trashcan="cd ~/.local/share/Trash"
# 处理解压windows压缩文件的标题乱码问题
alias unzip="unzip -O CP936"

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
# docker 
alias dps='sudo docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}"'
alias dis='sudo docker images'
alias dv='sudo docker volume'
alias d='sudo docker'


