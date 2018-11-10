#coding=utf-8
from __future__ import division, unicode_literals, print_function
import colorsys
import cairo

class Block(object):
    def __init__(self, name, height, width):
        self.height = height
        self.width = width
        self.name = name
        self.x = 0
        self.y = 0
    
    def draw(self, cr):
        
        image = cairo.ImageSurface.create_from_png ("%s.png" % self.name)  #不同的图片
        cr.set_source_surface ( image, self.x,self.y)
        cr.rectangle(self.x + 5, self.y + 5, self.width-10, self.height-10 )
        cr.fill_preserve()     #导入图
        
        cr.set_source_rgb(0,0,0)
        cr.stroke()   #画方框

        xbearing, ybearing, width, height, xadvance, yadvance = cr.text_extents(self.name)
        cr.move_to(self.x + self.width/2.- xbearing - width/2., self.y + self.height/2. - ybearing - height/2., ) 
        cr.set_source_rgb(0,0,0)
        cr.show_text(self.name)
        cr.stroke()   #画名字

PARAM = [                      
    ("曹操",200,200),
    ("赵云",100,200),
    ("黄忠",100,200),
    ("马超",100,200),
    ("张飞",100,200),
    ("关羽",200,100),
    ("甲1",100,100),
    ("乙2",100,100),
    ("丙3",100,100),
    ("丁4",100,100)
]
    
INIT_POS = [
    ("曹操",200,100),
    ("赵云",100,100),
    ("黄忠",100,300),
    ("马超",400,100),
    ("张飞",400,300),
    ("关羽",200,300),
    ("甲1",100,500),
    ("乙2",200,400),
    ("丙3",300,400),
    ("丁4",400,500)
]

class HuarongStatus(object):     
    def __init__(self, block_param):
        self.blocks = {}
        for n, w, h in block_param:    #赋值长宽
            self.blocks[n]=Block(n, height=h, width=w)

    def set_pos(self, pos):            #赋值位置
        for n, x, y in pos:
            self.blocks[n].x = x
            self.blocks[n].y = y
    
    def draw(self,cr):                 
        for b in self.blocks.itervalues():
            b.draw(cr)                  #执行自身的draw函数 

    

def prepare_cr():                       #画图的设置
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 500, 600)    
    cr = cairo.Context(ims)
    
    cr.select_font_face("微软雅黑", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(20)
    cr.set_line_width(2)
    cr.rectangle(0,0,500,600)
    cr.stroke()
    #cr.scale(100, 100)      #缩放比例  1:100
    cr.translate (-5, -5)
    return cr, ims

def test_drawbox():
    cr, ims = prepare_cr()
    c = Block("曹操", 200, 200)
    c.x = 100
    c.y = 100
    c.draw(cr)
    ims.write_to_png("boxa.png")

def test_draw_status():
    cr, ims = prepare_cr()

    h = HuarongStatus(PARAM)
    h.set_pos(INIT_POS)
    
    h.draw(cr)
    ims.write_to_png("statusC.png")

if __name__ == "__main__":
    test_draw_status()

