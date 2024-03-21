-- 用于linux系统，fcitx输入法环境，在退出insert模式时，自动切换至英文
return {
  "yaocccc/vim-fcitx2en",
  setup = function()
    vim.g.fcitx_on_events = "InsertLeave,InsertEnter"
  end,
  event = { "InsertLeave", "InsertEnter" },
}
