#放在家目录下
source ~/.config/omz/omz.zsh


[ $(tty) = "/dev/tty1" ] && cd ~ && startx

PATH="/home/time/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/time/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/time/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/time/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/time/perl5"; export PERL_MM_OPT;

export JAVA_8_HOME=/usr/lib/jvm/java-8-openjdk
export JAVA_17_HOME=/usr/lib/jvm/java-17-openjdk

export JAVA_HOME=$JAVA_17_HOME
export PATH=$PATH:/opt/maven/bin
export LOMBOK_JAR=/home/time/Downloads/idea-IU-232.9559.62/plugins/lombok/lib/lombok.jar
export PATH=$PATH:~/.local/bin
export EDITOR=/usr/bin/nvim

wds() {
       wd $*
       espeak-ng "$*"
}

eval $(thefuck --alias)
