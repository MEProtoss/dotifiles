-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local map = vim.keymap.set

-- insert mode
map("i", "<A-a>", "<right>", { desc = "向右移动一格光标", remap = true })
map("i", "<C-d>", "<esc>yyp$a", { desc = "复制当前行", remap = true })
map("n", "<bs>", '"_ciw', { desc = "快速删除", remap = true })
-- map("v", "<c-h>", rhs, opts)
-- normal mode
