#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual(string, string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(string, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        # In Python strings, the backslash "\" is a special character, also called the "escape" character.
        # Prefixing a quote with "\" turns it into an ordinary character (rather than a closing quote).
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
# In Python, a backslash ( \ ) is a continuation character, and if it is placed at the end of a line,
#  it is considered that the line is continued, ignoring subsequent newlines.
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
# String literals inside triple quotes, """ or ''',
# can span multiple lines of text. Python strings are "immutable"
#  which means they cannot be changed after they are created
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual(string, string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(string, string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual(string, string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        # The + operator is used both for adding numbers and strings;
        # in programming we say that the operator is overloaded.
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        # The easiest way of concatenating strings is to use the + or the += operator.
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual(__, original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(__, len(string))
