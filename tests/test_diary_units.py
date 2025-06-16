from lib.diary import *
from lib.diary_entry import DiaryEntry

def test_diary_entry_has_correct_public_properties():
    entry = DiaryEntry("title", "contents")
    assert type(entry.title) == str
    assert type(entry.contents) == str
    assert entry.title == "title"
    assert entry.contents == "contents"

def test_count_words_returns_int_for_content_word_count():
    entry = DiaryEntry("My Title", "These are the contents")
    assert type(entry.count_words()) == int
    assert entry.count_words() == 4
    entry_2 = DiaryEntry("Test Title 2", "More contents!")
    assert type(entry_2.count_words()) == int
    assert entry_2.count_words() == 2

def test_reading_time_returns_int_for_est_reading_time():
    entry = DiaryEntry("My Title", "These are the contents")
    assert type(entry.reading_time(4)) == int
    assert entry.reading_time(4) == 1
    contents_2 = "word "*30
    entry_2 = DiaryEntry("Title 2", contents_2)
    assert type(entry_2.reading_time(10)) == int
    assert entry_2.reading_time(10) == 3

def test_reading_chunk_returns_correct_string():
    contents = "one two three four five six seven eight nine ten "*2
    entry = DiaryEntry("Entry Title", contents)
    entry.reading_chunk(4, 2)
    assert entry.reading_chunk(4, 2) == "nine ten one two three four five six"
    assert entry.reading_chunk(4, 2) == "seven eight nine ten"
    assert entry.reading_chunk(4, 2) == "one two three four five six seven eight"



