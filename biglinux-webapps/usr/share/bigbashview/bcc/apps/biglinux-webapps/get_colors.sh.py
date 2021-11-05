#!/usr/bin/env python3
import sys, math
from PySide2.QtWidgets import QWidget, QApplication, QPushButton
from PySide2.QtGui import QPalette, QFont

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
        FontFamily = QFont().family()
        FontSize = QFont().pointSize()
        NamesWeight = { 0 : "Thin", 12 : "ExtraLight", 25 : "Light", 50 : "Normal", 57 : "Medium",
                        63 : "DemiBold", 75 : "Bold", 81 : "ExtraBold", 87 : "Black" }
        FontWeight = NamesWeight[QFont().weight()]
        FontStyle = QFont().styleName()
        ButtonQt = QPushButton().rect()

        COLORS = '''
<title>Colors Qt</title>
<style>
body{
    background-color: %s;
}

</style>
<body>
<b>Font Info</b><br>
font-family: %s<br>
font-size: %spt<br>
font-weight: %s<br>
font-style: %s<br>
<hr>
background-color: %s
<table cellspacing="15">
  <tr>
    <td id="div2" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Foreground: %s</font></td>
    <td id="div3" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Base: %s</font></td>
    <td id="div4" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">AlternateBase: %s</font></td>
    <td id="div5" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">ToolTipBase: %s</font></td>
  </tr>
  <tr>
    <td id="div6" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">ToolTipText: %s</font></td>
    <td id="div7" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">PlaceholderText: %s</font></td>
    <td id="div8" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Text: %s</font></td>
    <td id="div9" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Button: %s</font></td>
  </tr>
  <tr>
    <td id="div10" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">ButtonText: %s</font></td>
    <td id="div11" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">BrightText: %s</font></td>
    <td id="div12" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Light: %s</font></td>
    <td id="div13" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Midlight: %s</font></td>
  </tr>
  <tr>
    <td id="div14" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Dark: %s</font></td>
    <td id="div15" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Mid: %s</font></td>
    <td id="div16" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Shadow: %s</font></td>
    <td id="div17" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Highlight: %s</font></td>
  </tr>
  <tr>
    <td id="div18" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">HighlightedText: %s</font></td>
    <td id="div19" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">Link: %s</font></td>
    <td id="div20" style="background-color:%s;width:200px;height:100px;text-align:center;vertical-align:center">
        <font color="orange">LinkVisited: %s</font></td>
  </tr>
</table>

%s
</body>
        ''' % (Background, FontFamily, FontSize, FontWeight, FontStyle,
               Background, Foreground, Foreground, Base, Base, AlternateBase, AlternateBase,
               ToolTipBase, ToolTipBase, ToolTipText, ToolTipText, PlaceholderText,
               PlaceholderText, Text, Text, Button, Button, ButtonText, ButtonText,
               BrightText, BrightText, Light, Light, Midlight, Midlight, Dark, Dark,
               Mid, Mid, Shadow, Shadow, Highlight, Highlight, HighlightedText, HighlightedText,
               Link, Link, LinkVisited, LinkVisited, ButtonQt)
        print(COLORS)
        sys.exit()


app = QApplication(sys.argv)
main = Window()
app.exec_()

