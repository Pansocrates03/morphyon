class Style:

    def __init__(self, styleObj = {}):

        self.accent_color = None
        self.align_content = None
        self.align_items = None
        self.align_self = None
        self.all = None
        self.animation = None
        self.animation_delay = None
        self.animation_direction = None
        self.animation_duration = None
        self.animation_fill_mode = None
        self.animation_iteration_count = None
        self.animation_name = None
        self.animation_play_state = None
        self.animation_timing_function = None
        self.aspect_ratio = None

        self.backdrop_filter = None
        self.backface_visibility = None
        self.background = None
        self.background_attachment = None
        self.background_blend_mode = None
        self.background_clip = None
        self.background_color = None
        self.background_image = None
        self.background_origin = None
        self.background_position = None
        self.background_position_x = None
        self.background_position_y = None
        self.background_repeat = None
        self.background_size = None
        self.border = None
        self.border_block = None
        self.border_block_color = None
        self.border_block_end = None
        self.border_block_end_color = None
        self.border_block_end_style = None
        self.border_block_end_width = None
        self.border_block_start = None
        self.border_block_start_color = None
        self.border_block_start_style = None
        self.border_block_start_width = None
        self.border_block_style = None
        self.border_block_width = None
        self.border_bottom = None
        self.border_bottom_color = None
        self.border_bottom_left_radius = None
        self.border_bottom_right_radius = None
        self.border_bottom_style = None
        self.border_bottom_width = None
        self.border_collapse = None
        self.border_color = None
        self.border_end_end_radius = None
        self.border_end_start_radius = None
        self.border_image = None
        self.border_image_outset = None
        self.border_image_repeat = None
        self.border_image_slice = None
        self.border_image_source = None
        self.border_image_width = None
        self.border_inline = None
        self.border_inline_color = None
        self.border_inline_end = None
        self.border_inline_end_color = None
        self.border_inline_end_style = None
        self.border_inline_end_width = None
        self.border_inline_start = None
        self.border_inline_start_color = None
        self.border_inline_start_style = None
        self.border_inline_start_width = None
        self.border_inline_style = None
        self.border_inline_width = None
        self.border_left = None
        self.border_left_color = None
        self.border_left_style = None
        self.border_left_width = None
        self.border_radius = None
        self.border_right = None
        self.border_right_color = None
        self.border_right_style = None
        self.border_right_width = None
        self.border_spacing = None
        self.border_start_end_radius = None
        self.border_start_start_radius = None
        self.border_style = None
        self.border_top = None
        self.border_top_color = None
        self.border_top_left_radius = None
        self.border_top_right_radius = None
        self.border_top_style = None
        self.border_top_width = None
        self.border_width = None
        self.bottom = None
        self.box_decoration_break = None
        self.box_reflect = None
        self.box_shadow = None
        self.box_sizing = None
        self.break_after = None
        self.break_before = None
        self.break_inside = None

        self.caption_side = None
        self.caret_color = None
        self.clear = None
        self.clip = None
        self.clip_path = None
        self.color = None
        self.color_scheme = None
        self.column_count = None
        self.column_fill = None
        self.column_gap = None
        self.column_rule = None
        self.column_rule_color = None
        self.column_rule_style = None
        self.column_rule_width = None
        self.column_span = None
        self.column_width = None
        self.columns = None
        self.content = None
        self.counter_increment = None
        self.counter_reset = None
        self.counter_set = None
        self.cursor = None

        self.direction = None
        self.display = None

        self.empty_cells = None

        self.filter = None
        self.flex = None
        self.flex_basis = None
        self.flex_direction = None
        self.flex_flow = None
        self.flex_grow = None
        self.flex_shrink = None
        self.flex_wrap = None
        self.float = None
        self.font = None
        self.font_family = None
        self.font_feature_settings = None
        self.font_kerning = None
        #self.font_language_override = None
        self.font_size = None
        self.font_size_adjust = None
        self.font_stretch = None
        self.font_style = None
        #self.font_synthesis = None
        self.font_variant = None
        #self.font_variant_alternates = None
        self.font_variant_caps = None
        #self.font_variant_east_asian = None
        #self.font_variant_ligatures = None
        #self.font_variant_numeric = None
        #self.font_variant_position = None
        self.font_weight = None

        self.gap = None
        self.grid = None
        self.grid_area = None
        self.grid_auto_columns = None
        self.grid_auto_flow = None
        self.grid_auto_rows = None
        self.grid_column = None
        self.grid_column_end = None
        self.grid_column_start = None
        self.grid_row = None
        self.grid_row_end = None
        self.grid_row_start = None
        self.grid_template = None
        self.grid_template_areas = None
        self.grid_template_columns = None
        self.grid_template_rows = None

        self.hanging_punctuation = None
        self.height = None
        self.hyphens = None
        self.hypenate_characters = None

        self.image_rendering = None
        self.initial_letter = None
        self.inline_size = None
        self.inset = None
        self.inset_block = None
        self.inset_block_end = None
        self.inset_block_start = None
        self.inset_inline = None
        self.inset_inline_end = None
        self.inset_inline_start = None
        self.isolation = None

        self.justify_content = None
        self.justify_items = None
        self.justify_self = None

        self.left = None
        self.letter_spacing = None
        self.line_break = None
        self.line_height = None
        self.line_style = None
        self.line_style_image = None
        self.line_style_position = None
        self.line_style_type = None

        self.margin = None
        self.margin_block = None
        self.margin_block_end = None
        self.margin_block_start = None
        self.margin_bottom = None
        self.margin_inline = None
        self.margin_inline_end = None
        self.margin_inline_start = None
        self.margin_left = None
        self.margin_right = None
        self.margin_top = None
        self.marker = None
        self.marker_end = None
        self.marker_mid = None
        self.marker_start = None
        self.mask = None
        self.mask_clip = None
        self.mask_composite = None
        self.mask_image = None
        self.mask_mode = None
        self.mask_origin = None
        self.mask_position = None
        self.mask_repeat = None
        self.mask_size = None
        self.mask_type = None
        self.max_height = None
        self.max_width = None
        self.max_block_size = None
        self.max_inline_size = None
        self.min_block_size = None
        self.min_inline_size = None
        self.min_height = None
        self.min_width = None
        self.mix_blend_mode = None

        self.object_fit = None
        self.object_position = None
        self.offset = None
        self.offset_anchor = None
        self.offset_distance = None
        self.offset_path = None
        self.offset_position = None
        self.offset_rotate = None
        self.opacity = None
        self.order = None
        self.orphans = None
        self.outline = None
        self.outline_color = None
        self.outline_offset = None
        self.outline_style = None
        self.outline_width = None
        self.overflow = None
        self.overflow_anchor = None
        self.overflow_wrap = None
        self.overflow_x = None
        self.overflow_y = None
        self.overscroll_behavior = None
        self.overscroll_behavior_block = None
        self.overscroll_behavior_inline = None
        self.overscroll_behavior_x = None
        self.overscroll_behavior_y = None

        self.padding = None
        self.padding_block = None
        self.padding_block_end = None
        self.padding_block_start = None
        self.padding_bottom = None
        self.padding_inline = None
        self.padding_inline_end = None
        self.padding_inline_start = None
        self.padding_left = None
        self.padding_right = None
        self.padding_top = None
        self.page_break_after = None
        self.page_break_before = None
        self.page_break_inside = None
        self.paint_order = None
        self.perspective = None
        self.perspective_origin = None
        self.place_content = None
        self.place_items = None
        self.place_self = None
        self.pointer_events = None
        self.position = None

        self.quotes = None

        self.resize = None
        self.right = None
        self.rotate = None
        self.row_gap = None

        self.scale = None
        self.scroll_behavior = None
        self.scroll_margin = None
        self.scroll_margin_block = None
        self.scroll_margin_block_end = None
        self.scroll_margin_block_start = None
        self.scroll_margin_bottom = None
        self.scroll_margin_inline = None
        self.scroll_margin_inline_end = None
        self.scroll_margin_inline_start = None
        self.scroll_margin_left = None
        self.scroll_margin_right = None
        self.scroll_margin_top = None
        self.scroll_padding = None
        self.scroll_padding_block = None
        self.scroll_padding_block_end = None
        self.scroll_padding_block_start = None
        self.scroll_padding_bottom = None
        self.scroll_padding_inline = None
        self.scroll_padding_inline_end = None
        self.scroll_padding_inline_start = None
        self.scroll_padding_left = None
        self.scroll_padding_right = None
        self.scroll_padding_top = None
        self.scroll_snap_align = None
        self.scroll_snap_stop = None
        self.scroll_snap_type = None
        self.scrollbar_color = None
        self.shape_outside = None

        self.tab_size = None
        self.table_layout = None
        self.text_align = None
        self.text_align_last = None
        self.text_combine_upright = None
        self.text_decoration = None
        self.text_decoration_color = None
        self.text_decoration_line = None
        self.text_decoration_style = None
        self.text_decoration_thickness = None
        self.text_emphasis = None
        self.text_emphasis_color = None
        self.text_emphasis_position = None
        self.text_emphasis_style = None
        self.text_indent = None
        self.text_justify = None
        self.text_orientation = None
        self.text_overflow = None
        self.text_shadow = None
        self.text_transform = None
        self.text_underline_offset = None
        self.text_underline_position = None
        self.text_wrap = None
        self.top = None
        self.transform = None
        self.transform_origin = None
        self.transform_style = None
        self.transition = None
        self.transition_delay = None
        self.transition_duration = None
        self.transition_property = None
        self.transition_timing_function = None
        self.translate = None

        self.unicode_bidi = None
        self.user_select = None

        self.vertical_align = None
        self.visibility = None

        self.white_space = None
        self.widows = None
        self.width = None
        self.word_break = None
        self.word_spacing = None
        self.word_wrap = None
        self.writing_mode = None

        self.z_index = None
        self.zoom = None

        for prop, value in styleObj.items():  # Use .items() to iterate over key-value pairs
            if hasattr(self, prop): 
                setattr(self, prop, value)
            else: 
                raise ValueError(f"Property {prop} is not supported")


    # SETTERS
    def set_property(self, property_name, value):
        if hasattr(self, property_name): setattr(self, property_name, value)
        else: raise ValueError(f"Property '{property_name}' is not supported.")
        return self
    
    def set_color(self, color):
        self.color = color
        return self
    def set_font_size(self, font_size):
        self.font_size = font_size
        return self

    def render(self, class_name):
        # Generate CSS style string
        css_properties = []
        for prop, value in self.__dict__.items():
            if value is not None:
                css_properties.append(f"{prop.replace('_', '-')}: {value};")
        css_string = "\n".join(css_properties)
        return f".{class_name} {{\n{css_string}\n}}\n"