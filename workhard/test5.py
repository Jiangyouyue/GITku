import cairo

WIDTH=1000
HEIGHT=700
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)      
ctx.set_source_rgb(1, 1, 1)     #RGB
ctx.move_to( 140,  220)
ctx.rectangle(0,0,1000,20)
ctx.fill()
ctx.rectangle(0,20,20,680)
ctx.fill()
ctx.rectangle(20,320,980,380)
ctx.fill()
ctx.rectangle(420,20,580,300)
ctx.fill()
surface.write_to_png ("blank.png") 