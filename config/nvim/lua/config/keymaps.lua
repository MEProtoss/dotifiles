-- keymaps.lua 在 Lazy.nvim 启动之前自动加载。
-- 始终设置的默认按键映射: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- 在此添加其他按键映射
local map = vim.keymap.set

-- 向右移动光标
map("i", "<A-a>", "<right>", { desc = "向右移动一格光标", noremap = true })
-- 复制当前行
map("i", "<C-d>", "<esc>yyp$a", { desc = "复制当前行", noremap = true })
-- 退格键快速删除
map("n", "<bs>", '"_ciw', { desc = "快速删除", noremap = true })
-- 全选
map("n", "<A-a>", "ggVG", { desc = "全选", noremap = true })
-- Rnvimr插件
-- 在插入模式下使用 Alt + i 调整 Rnvimr 大小
vim.api.nvim_set_keymap("t", "<M-i>", "<C-\\><C-n>:RnvimrResize<CR>", { silent = true })
-- 在普通模式下使用 Alt + o 切换 Rnvimr 显示
vim.api.nvim_set_keymap("n", "<M-o>", ":RnvimrToggle<CR>", { silent = true })
-- 在 Rnvimr 中使用 Alt + o 切换显示
vim.api.nvim_set_keymap("t", "<M-o>", "<C-\\><C-n>:RnvimrToggle<CR>", { silent = true })
-- 打开chatgpt快捷键
vim.api.nvim_set_keymap("n", "<M-c>", ":ChatGPTEditWithInstructions<CR>", { desc = "打开chatgpt", silent = true })
