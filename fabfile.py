from fabric.api import *
from fabric.contrib.console import confirm
from fabric.colors import green, red

## install software
softwares = ['git',
             'vim',
             'vim-gnome',
             'emacs',
             'aria2',
             'uget',
             'zsh',
             'fish',
             'curl',]

def install_software():
    local('sudo apt-get update')
    local('sudo apt-get install -y %s' % ' '.join(softwares))
    local('git config --global user.email janken.wang@hotmail.com')
    local('git config --global user.name shjanken')

    #input method
    with settings(hide('stderr'), warn_only=True):
        isGnome = local('gnome-shell --version')
        if isGnome.failed and confirm('Is the desktop enviroment Gnome?'):
            local('sudo apt-get install ibus-rime')
        else:
            local('sudo apt-get install fcitx-rime')

def create_workspace():
    dir = '~/workspace'
    with settings(hide('stderr'), warn_only=True):
        ls_result = local('ls ~/workspace/')
        if ls_result.failed:
            local('mkdir ~/workspace')
            print(green('workspace directory was created!'))

def git_pull():
#    local('git clone https://git.coding.net/shjanken/mydotfile.git ~/workspace/mydotfile')
#    local('git clone https://git.coding.net/shjanken/fsl-client.git ~/workspace/fsl-client')
#    local('git clone https://git.coding.net/shjanken/CrimanalIntent.git ~/workspace/CrimanalIntent')
    local('git clone git@git.coding.net:shjanken/mydotfile.git ~/workspace/mydotfile/')
    local('git clone git@git.coding.net:shjanken/fsl-client.git ~/workspace/fsl-client/')
    local('git clone https://github.com/shjanken/vimperator_backup.git ~/.vimperator')

def init_oh_my_zsh():
    local('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')

def init_spacemacs():
    ls_result = local('ls ~/.emacs.d')
    if ls_result.failed:
        local('git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d')
    else:
        local('mv ~/.emacs.d ~/.emacs.d.bak')
        local('git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d')

def init_vim_spf13():
    local('curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh')

def install_oracle_jdk():
    local('sudo add-apt-repository ppa:webupd8team/java')
    local('sudo apt-get update')
    local('sudo apt-get install oracle-jdk8-installer')


def install_flash_plugin():
    local('sudo apt-get install falshplugin-installer')

def setup_my_computer():
    install_software()
    create_workspace()

    print(green('pull my projects-------'))
    git_pull()

    print(green('pull other dotfiles'))
    init_oh_my_zsh()
    init_spacemacs()
    init_vim_spf13()
    install_oracle_jdk()
    install_flash_plugin()
