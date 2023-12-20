vim.api.nvim_set_hl(0, "FlashCurrent", { fg = "#FF0000", bg = "#FF0000" })
vim.api.nvim_set_hl(0, "FlashLabel", { fg = "#FBF3CB", bg = "#FF007C" })
vim.api.nvim_set_hl(0, "FlashMatch", { fg = "#000000", bg = "#000000" })

return {
  -- gruvbox主题
  { "ellisonleao/gruvbox.nvim" },

  -- monokai 主题
  {
    "malbernaz/monokai.nvim",
    -- config = function()
    --   require("monokai").setup({
    --     custom_hlgroups = {
    --       FlashCurrent = { fg = "#FF0000", bg = "#FF0000" },
    --       FlashLabel = { fg = "#FBF3CB", bg = "#FF007C" },
    --       FlashMatch = { fg = "#000000", bg = "#000000" },
    --     },
    --   })
    -- end,
  },

  {
    "neanias/everforest-nvim",
    version = false,
    lazy = false,
  },

  -- Configure LazyVim to load gruvbox
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "gruvbox",
    },
  },

  -- 使您正在编辑的代码的非活动部分变暗。 该插件深受 Limelight 的启发，但使用 TreeSitter 来实现更好的调光效果。 与禅宗模式完美搭配。
  {
    "folke/twilight.nvim",
    opts = {
      -- your configuration comes here
      -- or leave it empty to use the default settings
      -- refer to the configuration section below
      --
      dimming = {
        alpha = 0.25, -- amount of dimming
        -- we try to get the foreground from the highlight groups or fallback color
        color = { "Normal", "#ffffff" },
        term_bg = "#000000", -- if guibg=NONE, this will be used to calculate text color
        inactive = false, -- when true, other windows will be fully dimmed (unless they contain the same buffer)
      },
      context = 10, -- amount of lines we will try to show around the current line
      treesitter = true, -- use treesitter when available for the filetype
      -- treesitter is used to automatically expand the visible text,
      -- but you can further control the types of nodes that should always be fully expanded
      expand = { -- for treesitter, we we always try to expand to the top-most ancestor with these types
        "function",
        "method",
        "table",
        "if_statement",
      },
      exclude = {}, -- exclude these filetypes
    },
  },
}
