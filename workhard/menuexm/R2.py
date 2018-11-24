import cairo

WIDTH=400
HEIGHT=400
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)      
ctx.set_font_size(28)
ctx.set_source_rgb(0, 0, 0)     #RGB
ctx.move_to( 140,  220)
ctx.show_text("Hello World!" )
surface.write_to_png ("R3.png") 