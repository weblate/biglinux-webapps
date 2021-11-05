#!/usr/bin/env python3
import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtGui import QPalette

class Window(QWidget):
    """doc for class"""
    def __init__(self):
        super().__init__()

        Background = self.palette().color(QPalette.Window).name()

        Foreground = self.palette().color(QPalette.WindowText).name()

        Base = self.palette().color(QPalette.Base).name()

        AlternateBase = self.palette().color(QPalette.AlternateBase).name()

        ToolTipBase = self.palette().color(QPalette.ToolTipBase).name()

        ToolTipText = self.palette().color(QPalette.ToolTipText).name()

        PlaceholderText = self.palette().color(QPalette.PlaceholderText).name()

        Text = self.palette().color(QPalette.Text).name()

        Button = self.palette().color(QPalette.Button).name()

        ButtonText = self.palette().color(QPalette.ButtonText).name()

        BrightText = self.palette().color(QPalette.BrightText).name()

        Light = self.palette().color(QPalette.Light).name()

        Midlight = self.palette().color(QPalette.Midlight).name()

        Dark = self.palette().color(QPalette.Dark).name()

        Mid = self.palette().color(QPalette.Mid).name()

        Shadow = self.palette().color(QPalette.Shadow).name()

        Highlight = self.palette().color(QPalette.Highlight).name()

        HighlightedText = self.palette().color(QPalette.HighlightedText).name()

        Link = self.palette().color(QPalette.Link).name()

        LinkVisited = self.palette().color(QPalette.LinkVisited).name()

        COLORS = '''
<style>
body{
    background-color: %s;
}

#div2{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div3{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div4{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div5{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div6{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div7{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div8{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div9{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div10{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div11{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div12{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div13{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div14{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div15{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div16{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div17{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div18{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div19{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

#div20{
    background-color: %s;
    width:100px;
    height:80px;
    text-align:center;
    display: block;
}

</style>
<body>
%s
<div>
  <div id="div2">%s</div>
  <div id="div3">%s</div>
  <div id="div4">%s</div>
  <div id="div5">%s</div>
  <div id="div6">%s</div>
  <div id="div7">%s</div>
  <div id="div8">%s</div>
  <div id="div9">%s</div>
  <div id="div10">%s</div>
  <div id="div11">%s</div>
  <div id="div12">%s</div>
  <div id="div13">%s</div>
  <div id="div14">%s</div>
  <div id="div15">%s</div>
  <div id="div16">%s</div>
  <div id="div17">%s</div>
  <div id="div18">%s</div>
  <div id="div19">%s</div>
  <div id="div20">%s</div>
</div>
</body>
        ''' % (Background, Foreground, Base, AlternateBase, ToolTipBase,
               ToolTipText, PlaceholderText, Text, Button, ButtonText,
               BrightText, Light, Midlight, Dark, Mid, Shadow, Highlight,
               HighlightedText, Link, LinkVisited,
               Background, Foreground, Base, AlternateBase, ToolTipBase,
               ToolTipText, PlaceholderText, Text, Button, ButtonText,
               BrightText, Light, Midlight, Dark, Mid, Shadow, Highlight,
               HighlightedText, Link, LinkVisited)
        print(COLORS)
        sys.exit()


app = QApplication(sys.argv)
main = Window()
app.exec_()
