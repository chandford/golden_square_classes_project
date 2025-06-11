from lib.make_diary import DiaryEntry

def test_diary_entry_has_correct_properties():
    entry = DiaryEntry("title", "contents")
    assert type(entry.title) == str
    assert type(entry.contents) == str
    assert entry.title == "title"
    assert entry.contents == "contents"

def test_format_returns_correctly_formatted_string():
    entry = DiaryEntry("My Title", "These are the contents")
    assert entry.format() ==  "My Title: These are the contents"
    entry_2 = DiaryEntry("Test Title 2", "More contents!")
    assert entry_2.format() == "Test Title 2: More contents!"

def test_count_words_returns_correct_integer():
    entry = DiaryEntry("My Title", "These are the contents")
    assert type(entry.count_words()) == int
    assert entry.count_words() == 4
    entry_2 = DiaryEntry("Test Title 2", "More contents!")
    assert type(entry_2.count_words()) == int
    assert entry_2.count_words() == 2

def test_reading_time_returns_expected_integer():
    entry = DiaryEntry("My Title", "These are the contents")
    assert type(entry.reading_time(4)) == int
    assert entry.reading_time(4) == 1
    contents_2 = "word "*30
    entry_2 = DiaryEntry("Title 2", contents_2)
    assert type(entry_2.reading_time(10)) == int
    assert entry_2.reading_time(10) == 3

# Is there any benefit to utilising round function ?? 
def test_reading_time_provides_accurate_estimate():
    contents = "word "*10
    entry = DiaryEntry("Title 2", contents)
    assert type(entry.reading_time(1000)) == int
    assert entry.reading_time(10) == 1

def test_reading_chunk_returns_correct_chunk_on_first_call():
    contents = "one two three four five six seven eight nine ten "*10
    entry = DiaryEntry("Entry Title", contents)
    assert entry.reading_chunk(4, 2) == "one two three four five six seven eight"
    assert type(entry.reading_chunk(4, 2)) == str

    contents_2 = "one two three four five "*10
    entry_2 = DiaryEntry("Entry Title 2", contents_2)
    assert entry_2.reading_chunk(2, 5) == "one two three four five one two three four five"

def test_reading_chunk_returns_next_chunk_when_recalled():
    contents = "one two three four five six seven eight nine ten "*2
    entry = DiaryEntry("Entry Title", contents)
    entry.reading_chunk(4, 2)
    assert entry.reading_chunk(4, 2) == "nine ten one two three four five six"
    assert entry.reading_chunk(4, 2) == "seven eight nine ten"
    assert entry.reading_chunk(4, 2) == "one two three four five six seven eight"


