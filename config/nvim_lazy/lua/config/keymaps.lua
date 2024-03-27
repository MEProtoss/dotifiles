-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local map = vim.keymap.set

-- insert mode
-- 向右移动光标
map("i", "<A-a>", "<right>", { desc = "向右移动一格光标", noremap = true })
-- 复制当前行
map("i", "<C-d>", "<esc>yyp$a", { desc = "复制当前行", noremap = true })
-- 退格键快速删除
map("n", "<bs>", '"_ciw', { desc = "快速删除", noremap = true })
-- map("v", "<c-h>", rhs, opts)
-- normal mode
