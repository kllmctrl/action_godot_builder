target="template_release"
debug_symbols="no"
optimize="size_extra"      # 极致体积优化 (Godot 4.5+ 特性)[citation:3]
lto="full"                 # 链接时优化，进一步减小体积

disable_3d="yes"
disable_advanced_gui="yes"
deprecated="no"
vulkan="no"
modules_enabled_by_default="no"
module_gdscript_enabled="yes"
module_text_server_fb_enabled="yes"
module_freetype_enabled="yes"
module_svg_enabled="yes"
module_webp_enabled="yes"
module_godot_physics_2d_enabled="yes"

# Godot 4.5 新增的独立裁剪选项
disable_navigation_2d="yes"
disable_navigation_3d="yes"
disable_xr="yes"
accesskit="no"