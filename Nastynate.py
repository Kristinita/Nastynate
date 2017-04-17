# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-03-28 16:42:04
# @Last Modified time: 2017-04-17 07:17:52
"""Modules of Nastynate.

"""
import sublime_plugin

import sublime

import time


def plugin_loaded():
    """Console log.

    Description:
    If Nastynate load, you'll see in Sublime Text console key and mouse
    log and commands.
    http://stackoverflow.com/a/29771703/5951529
    http://bit.ly/OdatNurdLoggingAndInput
    Example console output:

    key evt: enter
    command: nastya_wave

    Usage:
        Open Sublime Text console — http://stackoverflow.com/q/13965877/5951529
    """
    sublime.log_commands(True)
    sublime.log_input(True)


class ViewEncodingCommand(sublime_plugin.TextCommand):
    """View encoding Sublime Text command.

    Description:
    View encoding of current file in a Sublime Text Console. It implemented in
    Sublime Text by default, by SublimeLinter and packages for git
    fill all status bar. See
    https://github.com/SublimeTextIssues/Core/issues/1642 for more details.

    Work with unsaved buffers.

    Usage:
        Ctrl+Shift+P (<kbd>⌘⇧p</kbd> for Mac) →
        Suricate: Nastynate: View Encoding → open Sublime Text console and view
        encoding.

    Extends:
        sublime_plugin.TextCommand

    """

    def run(self, edit):
        current_view = self.view.id()
        if current_view:
            encoding = self.view.encoding()
            print(encoding)


class SendCurrentTimeToFileAltCommand(sublime_plugin.TextCommand):
    """Send Current Time To File Sublime Text command.

    Description:
    Send current time to file Output.txt by trigger. I use it for debugging
    with KateLogger program.

    Usage:
        Ctrl+Shift+P (<kbd>⌘⇧p</kbd> for Mac) → Suricate: Nastynate: Send
        Current Time To File → open Output.txt, that to see result.

    Extends:
        sublime_plugin.TextCommand
    """

    def run(self, view):
        current_view = self.view.id()
        if current_view:
            # Get current time
            # http://stackoverflow.com/a/28576383/5951529
            current_time = time.ctime()
            print(current_time)
            # Send text to file
            # http://stackoverflow.com/a/5214587/5951529
            # Don't rewrite file
            # http://stackoverflow.com/a/22441810/5951529
            text_file = open("D:\\OutputAlt.txt", "a", encoding='utf-8')
            print(text_file)
            # Write text to new line
            # http://stackoverflow.com/a/2918375/5951529
            text_file.write(current_time + " Alt" + "\n")
            text_file.close()


# Temporarily class for Mahou


class SendCurrentTimeToFileCapsCommand(sublime_plugin.TextCommand):

    def run(self, view):
        current_view = self.view.id()
        if current_view:
            # Get current time
            # http://stackoverflow.com/a/28576383/5951529
            current_time = time.ctime()
            print(current_time)
            # Send text to file
            # http://stackoverflow.com/a/5214587/5951529
            # Don't rewrite file
            # http://stackoverflow.com/a/22441810/5951529
            text_file = open("D:\\OutputCaps.txt", "a", encoding='utf-8')
            print(text_file)
            # Write text to new line
            # http://stackoverflow.com/a/2918375/5951529
            text_file.write(current_time + " Caps" + "\n")
            text_file.close()
