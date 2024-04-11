return {
	-- 一个用于ranger和nvim通讯的插件
	{
		"kevinhwang91/rnvimr",
	},

	-- 用于linux系统，fcitx输入法环境，在退出insert模式时，自动切换至英文
	{
		"yaocccc/vim-fcitx2en",
		setup = function()
			vim.g.fcitx_on_events = "InsertLeave,InsertEnter"
		end,
		event = { "InsertLeave", "InsertEnter" },
	},

	-- add symbols-outline 查看代码大纲
	{
		"simrat39/symbols-outline.nvim",
		cmd = "SymbolsOutline",
		keys = { { "<leader>cs", "<cmd>SymbolsOutline<cr>", desc = "Symbols Outline" } },
		config = true,
	},
}
